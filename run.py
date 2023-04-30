import gspread
from google.oauth2.service_account import Credentials
# import urllib.request
import webbrowser


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PP3-data-sets')


data = (SHEET.worksheet('instruction')).get_all_values()

print(data)



# get_url= urllib.request.urlopen('https://www.google.com/')

# print("Response Status: "+ str(get_url.getcode()) )
# print(get_url.read())

get_url= webbrowser.open('https://nb1355.github.io/PP1-Mountaineering-Global/',2)

