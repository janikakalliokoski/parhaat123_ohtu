*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To AddRef Page

*** Test Cases ***
Add RefPage Is Open
    Add RefPage Should Be Open

Book With Correct Input Added
    Add Book With Correct Input  
    Home Page Should Be Open
    Page Should Contain  Viite luotu onnistuneesti!

*** Keywords ***

Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Submit Form 
    Click Button  Lisää viite

Add Book With Correct Input 
    ${keyword} =  Generate Random String
    Set Input Field  keyword  ${keyword}
    Set Input Field  author_surname  mallikas
    Set Input Field  author_name  mikko
    Set Input Field  title  parhaat123
    Set Input Field  year  2020
    Set Input Field  publisher  Otava
    Submit Form
