from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from config import *
import time

def try_errorhandling():
    try:

        x = 10 / 0

    except (ZeroDivisionError, TypeError) as err:

        print('QQ!: {0}'.format(err))

def test_getcreds():
    creds = None
    # if os.path.exists(TOKEN):
    #     creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                APP_CREDENTIALS_FILE, SCOPES, )
            creds = flow.run_local_server(port=0, success_message='QQ!Authorization is OKAY!!')
        # Save the credentials for the next run
        # with open(TOKEN, 'w') as token:
        #     token.write(creds.to_json())

    return creds

if __name__ == '__main__':
    pass