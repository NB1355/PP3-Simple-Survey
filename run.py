
import gspread
from google.oauth2.service_account import Credentials
import json
import pandas as pd
import pyinputplus as pyip
from tabulate import tabulate


# ..........................................TEMP: tests for adding new features
from tests import test01


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PP3-data-sets')


def check_value(sht, col, val):
    # Check whether a given value exists in a given column in connected sheet #
    data = SHEET.worksheet(sht).get_all_records()
    df = pd.DataFrame(data).astype('string')
    valset = df[col].values
    if val in valset:
        out = 'exist'
    else:
        out = 'does not exis!'
    return out


def get_user_pass():

    print('\nYou need valid cidentials to enter the program!')
    print('3 attemps allowed!\n')

    attempts = 3
    while attempts > 0:

        username = pyip.inputPassword(
            prompt='Enter your username: ', mask=None)
        password = pyip.inputPassword(prompt='Enter your password: ', mask='*')

        userkey = str(username) + '_' + str(password)
        check_value('user', 'user_key', userkey)

        if check_value('user', 'user_key', userkey) != 'exist':
            attempts -= 1
            print('\nLogin data is not valid,  ' +
                  str(attempts) + '  attempt/s remaimed!!!\n')
        else:

            print('\nW E L C O M E !')
            print('\nChoose an option to proceed.')
            options_run()
            continue


def get_options():

    ## Open the file seting.json ##
    with open('setings.json') as json_file:
        data = json.load(json_file)

    ## Extract the defined options ##
    options = data['options']

    ## Use Panda DataFrame to format the output ##
    df = pd.DataFrame(options)
    dfp = df.drop('id', axis=1)

    # print('\n',dfp.to_string(header=False,index=False))

    print(tabulate(dfp, showindex=False))

    ## Options list rows to define the Max of unput range ##
    return len(options)


def get_query(sht, rng, col):

    data = SHEET.worksheet(sht).get_values(rng)
    df = pd.DataFrame(data).astype('string')

    # --------------------------------------------------------------- print(df)
    valset = df[col].values
    # ---------------------------------------------------------------print(valset)
    return valset


def f_00():

    ## Exit the program  ##
    exit('\nG O O D B Y !\n')

def f_01():
    # Clear the viable screen, CRED: https://stackoverflow.com/users/9704496/mario-palumbo  ##
    print("\033c", end='')
    options_next()

def f_02():
    print('.............. execute function 2')
    options_next()



def f_03():
    print('.............. execute function 3')
    options_next()


def options_next():
    # Show the menue0
    print('\nChoose an option to proceed.')
    options_run()


def options_run():

    ## Executes the function corresponding to the user input ##
    try:
        op = pyip.inputInt('\n> ', min=0, max=get_options()-1,)
        match op:
            case 0:
                f_00()
            case 1:
                f_01()
            case 2:
                f_02()
            case 3:
                f_03()

    except KeyboardInterrupt:
        print('\n\nO O P S! something went wrong...\nB A C K  T O  M E N U !')

    options_next()


def main():

    options_run()

    # print('\nW E L C O M E ! \n.... Choose form options below to proceed\n')


main()
