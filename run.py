
import gspread
from google.oauth2.service_account import Credentials
import json
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PP3-data-sets')


def instructions():
    # Opening JSON file
    with open('setings.json') as json_file:
        data = json.load(json_file)
    options = data['options']

    # load data into a DataFrame object:
    df = pd.DataFrame(options).set_index('Op')
    dfp = df.drop('id', axis=1)

    print(dfp.to_string(header=False))
    print('------------------------------------')


def f_00():
    print(' ... execute function 0')

def f_01():
    print(' ... execute function 1')

def f_02():
    print(' ... execute function 2')

def f_03():
    print(' ... execute function 3')

def options_run():
    #get the user input and executs functions based on the user input
    instructions()
    op = int(input('Your option: '))
    match op:
        case 0:
            f_00()  
        case 1:
            f_01()
        case 2:
            f_02()
        case 3:
            f_03()


def main(): 
    print('\nW E L C O M E ! \nChoose form options below to proceed...')
    options_run()


    print('\nD O N E ! \n                                    python3 run.py')
main()
