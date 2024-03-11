#    Copyright © 2021 Andrei Puchko
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os.path

from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
import json
import webbrowser


class q2googledrive:
    def __init__(self, token="token.json", secrets="credentials.json", service_account_key=""):
        self.SCOPES = [
            "https://www.googleapis.com/auth/drive.metadata.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive.appdata",
        ]
        self.drive = None
        self.token = None
        self.token_data = token
        self.secrets = secrets
        self.service_account_key = service_account_key
        self.google_sheets = None
        if self.service_account_key or self.secrets:
            if not self.login():
                self.login()

    def login(self):
        self.get_token_service_account()
        if self.token is None:
            self.get_token_oauth()
        if self.token is None:
            return False
        try:
            self.drive = build("drive", "v3", credentials=self.token)
        except HttpError as error:
            self.drive = None
            print(f"An error occurred: {error}")
            return False
        return True

    def get_token_service_account(self):
        # Service account credentials - first
        if isinstance(self.service_account_key, str) and os.path.exists(self.service_account_key):
            self.token = service_account.Credentials.from_service_account_file(
                self.service_account_key, scopes=self.SCOPES
            )
        elif isinstance(self.service_account_key, str) and self.service_account_key != "":
            self.token = service_account.Credentials.from_service_account_info(
                json.loads(self.service_account_key), scopes=self.SCOPES
            )
        elif isinstance(self.service_account_key, dict):
            self.token = service_account.Credentials.from_service_account_info(
                self.service_account_key, scopes=self.SCOPES
            )
        if self.token:
            self.token_data = None
            self.secrets = None

    def get_token_oauth(self):
        #  OAuth client ID credentials
        if isinstance(self.token_data, str) and os.path.exists(self.token_data):
            self.token = Credentials.from_authorized_user_file(self.token_data, self.SCOPES)
        elif isinstance(self.token_data, str) and self.token_data != "":
            try:
                self.token_data = json.loads(self.token_data)
                self.token = Credentials.from_authorized_user_info(self.token_data)
            except Exception as error:
                print(f"An error occurred while jsonify token data: {error}")
        elif self.token_data:
            self.token = Credentials.from_authorized_user_info(self.token_data)

        if not self.token or not self.token.valid:
            if self.token and self.token.expired and self.token.refresh_token:
                try:
                    self.token.refresh(Request())
                except RefreshError as error:
                    self.token_data = None
                    self.token = None
                    print(f"An error occurred while refreshing token: {error}")
                    return False
            else:
                if isinstance(self.secrets, str) and os.path.exists(self.secrets):
                    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                elif isinstance(self.secrets, str):
                    flow = InstalledAppFlow.from_client_config(json.loads(self.secrets), self.SCOPES)
                else:
                    flow = InstalledAppFlow.from_client_config(self.secrets, self.SCOPES)
                self.token = flow.run_local_server(port=0)
            # Save the credentials for the next run
            if os.path.exists(self.secrets):
                with open("token.json", "w") as token:
                    token.write(self.token.to_json())
            else:
                self.token_data = self.token.to_json()

    def dir(self, q=""):
        return (
            self.drive.files()
            .list(
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
                q=q,
                fields="files(id, name, mimeType, size, modifiedTime)",
            )
            .execute()
            .get("files", [])
        )

    def get(self, id):
        return self.drive.files().get(fileId=id, fields="*").execute()

    def open_sheet(self, id):
        webbrowser.open(f"https://docs.google.com/spreadsheets/d/{id}/edit#gid=0")

    def open_document(self, id):
        webbrowser.open(f"https://docs.google.com/document/d/{id}/edit#gid=0")

    def load_docs(self, id):
        return self.load(id, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    def load_odt(self, id):
        return self.load(id, "application/vnd.oasis.opendocument.text")

    def load_xlsx(self, id):
        return self.load(id, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    def load_ods(self, id):
        return self.load(id, "application/x-vnd.oasis.opendocument.spreadsheet")

    def load(self, id, mimeType):
        return self.drive.files().export(fileId=id, mimeType=mimeType).execute()

    def n2c(self, n):
        return chr(n + 64) if n <= 26 else self.n2c((n - n % 26) // 26) + self.n2c(n % 26)

    def open_sheets(self):
        if self.google_sheets is None:
            if self.secrets:
                self.google_sheets = gspread.oauth(credentials_filename=self.secrets)
            else:
                self.google_sheets = gspread.authorize(self.token)
        return self.google_sheets

    def load_spreadsheet_dict(self, id):
        self.google_sheets = self.open_sheets()

        if self.google_sheets is None:
            return None

        sheet = self.google_sheets.open_by_key(id)
        rez = {}
        for worksheet in sheet.worksheets():
            rez[worksheet.title] = {}
            for row_number, row in enumerate(sheet.worksheet(worksheet.title).get_all_values()):
                rez[worksheet.title][row_number + 1] = {}
                for column_number, cell in enumerate(row):
                    rez[worksheet.title][row_number + 1][self.n2c(column_number + 1)] = cell
        return rez

    def load_sheet_row_dict(self, id, sheet_number, row_number):
        self.google_sheets = self.open_sheets()

        if self.google_sheets is None:
            return None
        sheet = self.google_sheets.open_by_key(id)
        worksheet = sheet.get_worksheet(sheet_number)
        rez = {worksheet.title: {row_number: {}}}
        for column_number, cell_value in enumerate(worksheet.row_values(row_number)):
            rez[worksheet.title][row_number][self.n2c(column_number + 1)] = cell_value
        return rez
