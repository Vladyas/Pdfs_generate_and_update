'''
python required modules installation:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install pyside6
'''

GENERATION_CHECK = {
'creds':'Залогигились в Google Drive...',
}

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/spreadsheets.readonly']
APP_CREDENTIALS_FILE = 'credentials.json'
RANGE = 'A1:A'