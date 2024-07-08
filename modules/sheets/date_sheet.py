from os import path, getenv
from dotenv import load_dotenv
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

class Sheets:
    def __init__(self, spreadsheet_id_a2: str, spreadsheet_id_dates: str, path_creds: str):
        self.spreadsheet_id_a2 = spreadsheet_id_a2
        self.spreadsheet_id_dates = spreadsheet_id_dates
        # create credentials
        self.credentials = None
        if path.exists("token.json"):
            self.credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(path_creds, SCOPES)
                self.credentials = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(self.credentials.to_json())

        self.service = build("sheets", "v4", credentials=self.credentials)
        self.sheets = self.service.spreadsheets()
        try:
            result = self.sheets.values().get(spreadsheetId=self.spreadsheet_id_dates, range="A:A").execute()
            values = result.get("values", [])
            self.position = len(values)
        except HttpError as error:
            print(error)
            quit(1)

    def get_value(self, value: str = "A2"):
        try:
            #service = build("sheets", "v4", credentials=self.credentials)
            #sheets = service.spreadsheets()

            result = self.sheets.values().get(spreadsheetId=self.spreadsheet_id_a2, range=value).execute()
            values = result.get("values", [])

            return values[0][0]
        except HttpError as error:
            print(error)

    def next_value(self, value: str):
        #service = build("sheets", "v4", credentials=self.credentials)
        #sheets = service.spreadsheets()

        self.sheets.values().update(spreadsheetId=self.spreadsheet_id_dates, range=f"A{self.position+1}", valueInputOption="USER_ENTERED", body={"values": [[value]]}).execute()
        self.position += 1

if __name__ == "__main__":
    load_dotenv()
    sheets = Sheets(str(getenv("SPREADSHEET_A2")), str(getenv("SPREADSHEET_DATES")), "../../creds.json")
    print(sheets.get_value())
    sheets.next_value("14.02.2020")
    time.sleep(20)
    print(sheets.get_value())
