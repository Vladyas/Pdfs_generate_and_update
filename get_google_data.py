from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import *

def get_creds():
    flow = InstalledAppFlow.from_client_secrets_file(
        APP_CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def get_spreadsheets(creds):
    pass

def get_sheet_range(spreadsheet_id, range):
    pass