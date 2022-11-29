*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Is Open
    Home Page Should Be Open

Book with correct input added
    Set Input Field  title  parhaat123
    Set Input Field  author  mluukkai
    Set Input Field  keyword  123
    Set Input Field  year  2020
    Set Input Field  publisher  Otava
    Submit Form
    Home Page Should Be Open

*** Keywords ***
Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id} ${text}

Submit Form 
    Click Button  Lisää viite
