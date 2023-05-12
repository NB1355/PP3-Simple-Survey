
import gspread
from google.oauth2.service_account import Credentials
import json
import pandas as pd
import pyinputplus as pyip
from tabulate import tabulate
import numpy as np
from io import StringIO


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

        global username
        username = pyip.inputPassword(
            prompt='Enter your username: ', mask=None)
        password = pyip.inputPassword(prompt='Enter your password: ', mask='*')

        userkey = str(username) + '_' + str(password)
        # check_value('users', 'user_key', userkey)

        if check_value('users', 'user_key', userkey) == 'exist':
            print('\nWait for the program to load ...')
            attempts = 0
            break

        else:
            attempts -= 1
            if attempts == 0:
                print('\nAuthentication failed\nE X I T !')
                exit()

            print('\nLogin data is not valid,  ' +
                  str(attempts) + '  attempt/s remaimed!!!\n')


def get_surveys():

    print('\nSurvey List:')
    srv_list = []
    srv_menu = []
    # ['ID', 'Query', 'Status' , 'User Vote']
    for row in range(1, 6):
        sublist = []
        for col in range(1):
            srv_id = 'S' + f'{row:02d}'
            srv_qs = SHEET.worksheet(srv_id).cell(2, 5).value
            srv_st = SHEET.worksheet(srv_id).cell(2, 4).value
            srv_us = check_value(srv_id, 'user', username)
            sublist.append(srv_id)
            sublist.append(srv_qs)
            sublist.append(srv_st)
            sublist.append(srv_us)
            srv_menu.append(srv_qs)

        srv_list.append(sublist)

    # print(pd.DataFrame(srv_list))
    # srv_filt = srv_list.


def get_vote(sht):

    value_list = get_query(sht, 'QA', 1)

    if check_value(sht, 'user', username) != 'exist':
        ## Run the current survey  ##
        print('\n>> '+value_list[1]+'\n')

        ansr = pyip.inputMenu([value_list[3], value_list[2]],
                              numbered=True)
        update_data(sht, [username, ansr])
        print('> Your Choice: '+ansr)

        print('\nSurvey Results:\n'+value_list[1])
        print(tabulate(get_query(sht, 'stat', [0, 2])))

        print('Thanks for taking part!\n\nB A C K  T O  M E N U !')
    else:
        print('> You have voted befor!')

        print('\nSurvey Results:\n'+value_list[1])
        print(tabulate(get_query(sht, 'stat', [0, 2])))

        print('\n\nB A C K  T O  M E N U !')
        options_run()


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


def update_data(sht, data):

    ## Update survey sheet with the vote ##

    worksheet_to_update = SHEET.worksheet(sht)
    worksheet_to_update.append_row(data)


def f_00():

    ## Exit the program  ##
    exit('\nG O O D B Y !\n')


def f_01():
    # Clear the viable screen, CRED: https://stackoverflow.com/users/9704496/mario-palumbo  ##
    print("\033c", end='')
    options_next()


def f_02():

    ## Run the current survey if the user vote doesn't exist, else show the result  ##
    for row in range(5):
        if srv[row][2] == 'current':
            current = srv[row][0]
    # print(current)
    ## Run the current survey if the user vote doesn't exist, else show the result  ##
    get_vote(current)
    options_run()


def f_03():
    print('\nexecuting function 3')
    # data = SHEET.fetch_sheet_metadata(params=None)
    get_surveys()
    exit()


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

    get_user_pass()
    get_surveys()
    print('\nW E L C O M E !')
    options_run()


main()
