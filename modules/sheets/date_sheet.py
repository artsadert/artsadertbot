from os import path, getenv
from dotenv import load_dotenv
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Класс который работает с google sheets api
class Sheets:
    def __init__(self, spreadsheet_id_a2: str, spreadsheet_id_dates: str, path_creds: str):
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

        # Два гугл документа
        self.spreadsheet_id_a2 = spreadsheet_id_a2
        self.spreadsheet_id_dates = spreadsheet_id_dates
        
        # Создание реквизитов для входа
        self.credentials = None

        # Проверка на то, что токен существует
        if path.exists("token.json"):
            self.credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

        # Проверка на то что токена не существует или на то, что он устарел
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            # Аунтефикация
            else:
                flow = InstalledAppFlow.from_client_secrets_file(path_creds, SCOPES)
                self.credentials = flow.run_local_server(port=0)

            # Запись обновленного или нового токена
            with open("token.json", "w") as token:
                token.write(self.credentials.to_json())

        # Подгрузка всех таблиц
        self.service = build("sheets", "v4", credentials=self.credentials)
        self.sheets = self.service.spreadsheets()


        # Получим длину всех елементов столбца A
        try:
            result = self.sheets.values().get(spreadsheetId=self.spreadsheet_id_dates, range="A:A").execute()
            values = result.get("values", [])
            self.position = len(values)
        except HttpError as error:
            print(error)
            quit(1)
    
    # Функция, которая достает значение из ячейки
    def get_value(self, value: str = "A2"):
        try:
            result = self.sheets.values().get(spreadsheetId=self.spreadsheet_id_a2, range=value).execute()
            values = result.get("values", [])

            return values[0][0]
        except HttpError as error:
            print(error)

    # Функция, которая записывает значение в следующую ячейку
    def next_value(self, value: str):
        self.sheets.values().update(spreadsheetId=self.spreadsheet_id_dates, range=f"A{self.position+1}", valueInputOption="USER_ENTERED", body={"values": [[value]]}).execute()
        self.position += 1
