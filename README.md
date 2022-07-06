**This framework is mainly set up for assessment done by, Muhammad Abdullah.**

---

## Setup Framework

1. Clone this repository.
2. Open it in PyCharm studio. (Install pycharm if you do not have already from https://www.jetbrains.com/pycharm/download)
3. Install Python. (Install python if you don't have and setup environment variables > https://www.python.org/downloads)
4. Set up the interpreter for python. (Take help from here: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env)
5. Run below command to install all necessary packages and libraries. `pip install -r reqruirements.txt`
6. If above command cause problem then try installing all modules ony by one from `requirement.txt` file.

---

## Run Tests

1. Open terminal run command `pytest` in home directory to run all tests. You can see results in the terminal.
2. OR, open each test file in `testCases/*`, and click on the **play** button at the left of each test, which will run single test at a time.

Other commands can be found here: 
https://docs.pytest.org/en/6.2.x/usage.html

--- 

## Run Tests with Allure Reports

1. Open terminal run command `allure/bin/allure generate`. (It will generate the **allure-report** directory if not existing already.)
2. Then `pytest --alluredir=allure-report/` to run all tests and write results to above directory.
3. To view the report, enter `allure serve allure-report/` command. (It will give a detailed view of the report)

Other allure commands can be found here: 
https://docs.qameta.io/allure/#_python

---

## Create a new test

To create new tests: 

1. Go to **testCases** directory and create a new python file. (Convention: test_<your test name>.py)
2. Go to **pageObjects** directory and create a new object python file. (Convention: YourTestObject.py)
3. **pageObjects** file contains locators and functions.
4. There is base file in common directory in **pageObjects** directory for all common functions. (Like click, type etc)
5. Use these functions in your objects files.

---
