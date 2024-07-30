# Import required packages
import pandas as pd
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Prepare auth json for google connection
cred_json = os.environ['SERVICE_ACCOUNT_CREDENTIALS_JSON']
s_char = cred_json.index('~~~')
e_char = cred_json.index('%%%')
service_account_cred = eval(cred_json[s_char+3:e_char])

# Connect to the google service account
scope = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(
                              info=service_account_cred, 
                              scopes=scope)
service = build('drive', 'v3', credentials=credentials)

# Read in File
url = 'https://drive.google.com/file/d/1PKDzrurOqfIDkdD8NK5edTBC3Hu1xkfg/view?usp=drive_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
game_log = pd.read_csv(path)

# Changes
game_log.loc[0,'Opp'] = 'CHA'
game_log.loc[1,'Team'] = 'CHA'

# Write File
t_csv_stream = io.StringIO()
game_log.to_csv(t_csv_stream, sep=";")

# Upload File
returned_fields="id, name, mimeType, webViewLink, exportLinks, parents"
file_metadata = {'name': 'test_fake.csv',
                'parents':['1GTyaZ1tRX1Wrh9LpHGRNoGJo6MWLEqsQ']}
media = MediaIoBaseUpload(t_csv_stream,
                        mimetype='text/csv')
file = service.files().create(body=file_metadata, media_body=media,
                              fields=returned_fields).execute()
