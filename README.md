
### PPIII: Python Essentials
# Simple Surveys 

#### This is a Python module that allows users to access and participate in a set of surveys defined in Google Sheets and see the results, as well as possibilty to see te curret status of all surveys!

|**CONTENT**                  |                              |               |
| :---------------------------| :----------------------------| :-------------|
|*PRODUCT*                    |*DEVELOPMENT*                 |*CREDITS*      |
|[Features](#features)        |[Technologies](#technologies) |[Code Used](#code-used)|
|[Requirements](#requirements) |[Languages](#languages)       | [Acknowledgments](#acknowledgments)|
|[Design](#design)            |[Deployment](#deployment)
|[UX](#ux)                    |[Testing](#testing)|
||||


## PRODUCT
See the live page [here](https://nb1355pp3.herokuapp.com/)
#

### Features

* Defined users can participate in up to five surveys.
* Users have access to up to five surveys at a time.
* The top/current survey should be accessed separetely.
* View the vote results of five survays. 

### Requirements

* Run in a terminal or command prompt.
*  Prompt to enter username and password to authenticate access to the application (3 attempts allowed)
* In case of successful authentication, dispaly the options.
* Options to navigate through the application:
    - Option 1: Clear the screen and return to the main menu.
    - Option 2: Vote on the current survey (if available/only onece permitted).
    - Option 3: Choose a survey from the available options and vote.
    - Option 4: View the details and results of all surveys.
    - Option 0: Exit the application.

#### Out of Scope
  - Full user authentication, i.e. the correct user pass combination is required to access.
  - Multiple questions in each survay.
#### Future Improvement
  - Option to manage add new user account
  - Upgrade to multiple questions in each survey.
  - Replace google sheets with a proper database structure


### UX
* The requirement is to run the code in a terminal, design elements are limited.
* Improvement in UX is limited to providing users with messages based on actions and options available.

![Alt text](_docs/screenshots/docUX.jpg)
### Design 
#### Data Structure
A simple data structure in Google Sheets, including one for users and five for each survey. 

"PP3-data-sets" will be used to store survey data. The sheet is shared with the service account specified in the `creds.json` file.


![Alt text](_docs/screenshots/docUsers.jpg)

![Alt text](_docs/screenshots/docSurveys.jpg)

#### Menue Settings
To add a more flexibility to make changes in naming and order of functions appearing in the menu the name and order of the functions can be changed in `seting.json` file.
![Alt text](_docs/screenshots/docSetings.jpg)

## <br> DEVELOPMENT

### Technologies

### Languages
Python3 is the main language used as required, others are shown in the GitHub language summary belong to the template used for Heroku deployment. 

### Frameworks, Libraries & Programs
- [GitHub](https://github.com/) for hosting repositories.
- [GitPod](https://www.gitpod.io/) as coding environment.
- [Heroku](https://www.heroku.com/) for depolyment.
- [GoogleSheets](https://www.google.ie/?gws_rd=ssl) as trmporaray data structure.
- [p3-deployment-template](https://github.com/Code-Institute-Org/p3-template) for deploying a Python command line by CodeInstitute.
- `gspread` : A Python library for accessing Google Sheets.
- `google-auth` : A Python library for handling OAuth 2.0 authentication.
- `pandas` : A data manipulation and analysis library.
- `pyinputplus` : A library for validating user input.
- `tabulate` : A library for creating formatted tables.

### Deployment
Heroku is used for deployment; specific setup instructions can be found in the source template provided by CodeInstitute.







