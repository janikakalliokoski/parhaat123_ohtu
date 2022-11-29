*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}

*** Keywords ***
Go To Home Page
    Go To  ${HOME URL}

Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Viiteapuri
localhost:5000