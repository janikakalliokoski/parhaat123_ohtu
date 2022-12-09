*** Settings ***
Library  SeleniumLibrary
Library  String

*** Variables ***
${SERVER}  https://parhaat123.fly.dev/
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  ${SERVER}
${ADDREF URL}  ${SERVER}/uusi

*** Keywords ***
Go To Home Page
    Go To  ${HOME URL}

Go To AddRef Page
    Go To  ${ADDREF URL} 

Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Viiteapuri

Add RefPage Should Be Open
    Title Should Be  Lisää viite
