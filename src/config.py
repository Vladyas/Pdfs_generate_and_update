'''
python required modules installation:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install pyside6
pip install PyPDF2

'''
APP_CREDENTIALS_FILE = 'credentials.json'
TOKEN = 'token.json'

SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_MIMETYPE = 'application/vnd.google-apps.spreadsheet'
RANGE = '!A1:A'

FILE_UNIQ_NUMBERS = 'uniq_numbers.csv'