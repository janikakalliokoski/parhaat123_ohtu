*** Settings ***
Library  SeleniumLibrary
Library  String

*** Variables ***
${SERVER}  http://parhaat123.fly.dev/
${BROWSER}  headlesschrome
${DELAY}  0.5 seconds
${HOME URL}  ${SERVER}

*** Keywords ***
Go To Home Page
    Go To  ${HOME URL}

Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Viiteapuri
