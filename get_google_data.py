import os
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import *


def get_creds():
    creds = None
    if os.path.exists(TOKEN):
        creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                APP_CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN, 'w') as token:
            token.write(creds.to_json())

    return creds


def get_spreadsheets(creds):
    service = build('drive', 'v3', credentials=creds)
    results = service.files().list(q=f"mimeType='{SPREADSHEET_MIMETYPE}'",
                                   pageSize=1000,
                                   fields="files(id, name, ownedByMe, owners, trashed)").execute()
    items = results.get('files', [])
    # Exclude trashed spreadsheets
    items = sorted(filter(lambda x: not x['trashed'], items), key=lambda x: x['name'])
    return items


def get_treeWidget_dict(creds, spreadsheets):
    tree_data = []
    if spreadsheets:
        service = build('sheets', 'v4', credentials=creds).spreadsheets()
        for i in spreadsheets:
            sheets = service.get(spreadsheetId=i['id']).execute().get('sheets')
            d = {'name': i['name'], 'sheet1': sheets[0]['properties']['title'],
                 'owner': i['owners'][0]['displayName'], 'id': i['id'], 'sheets':[]}
            for s in sheets:
                d['sheets'].append(s['properties']['title'])
            tree_data.append(d)
    else:
        tree_data = None
    return tree_data


def get_sheet_range(spreadsheet_id, range):
    pass


if __name__ == '__main__':
    # print(get_spreadsheets(get_creds()))
    c = get_creds()
    pprint(get_treeWidget_dict(c, get_spreadsheets(c)))
