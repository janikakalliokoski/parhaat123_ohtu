*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Is Open
    Home Page Should Be Open

Book With Correct Input Added
    ${keyword} =  Generate Random String
    Set Input Field  keyword  ${keyword}
    Set Input Field  author  mluukkai
    Set Input Field  title  parhaat123
    Set Input Field  year  2020
    Set Input Field  publisher  Otava
    Submit Form
    Home Page Should Be Open

*** Keywords ***
Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Set Input Keyword
    ${ret}  =  Generate Random String 
    Input Text  keyword  

Submit Form 
    Click Button  Lisää viite