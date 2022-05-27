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
    try:
        service = build('drive', 'v3', credentials=creds)
        results = service.files().list(q=f"mimeType='{SPREADSHEET_MIMETYPE}'",
                                       pageSize=1000,
                                       fields="files(id, name, ownedByMe, owners, trashed)").execute()
        items = results.get('files', [])
        # Exclude trashed spreadsheets
        items = sorted(filter(lambda x: not x['trashed'], items), key=lambda x: x['name'])
    except:
        print('Google Api exception при работе get_spreadsheets()')
    return items


def get_sheet_range(creds, spreadsheet_id, range):
    try:
        service = build('sheets', 'v4', credentials=creds)
        include_grid_data = False
        request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range)
        response = request.execute()
        if 'values' in response.keys():
            result = [x[0] for x in response['values'] if x]
            result = set(result)
        else:
            result = set()
    except :
        print('Google Api exception при работе get_sheet_range()')

        result = None
    return result


def get_treeWidget_dict(creds, spreadsheets):
    tree_data = []
    if spreadsheets:
        service = build('sheets', 'v4', credentials=creds).spreadsheets()
        for i in spreadsheets:
            sheets = service.get(spreadsheetId=i['id']).execute().get('sheets')
            d = {'name': i['name'], 'sheet1': sheets[0]['properties']['title'],
                 'owner': i['owners'][0]['displayName'], 'id': i['id'], 'sheets': []}
            for s in sheets:
                d['sheets'].append(s['properties']['title'])
            tree_data.append(d)
    else:
        tree_data = None
    return tree_data


if __name__ == '__main__':
    pass
    # c = get_creds()
    # pprint(get_treeWidget_dict(c, get_spreadsheets(c)))
    # spreadsheet_id = '1JPq0dXba_TYvfYdj_L6EqelChki4hi-es2dEyUDnK98'
    # ranges = 'Лист1!A2:A'
    # print(get_sheet_range(c, spreadsheet_id, ranges))
