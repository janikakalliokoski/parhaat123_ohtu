*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Is Open
    Home Page Should Be Open

Select Book Reference
    Select Radio Button  type  kirja
    Create Reference

Book With Correct Input Added
    Create Reference
    Add Book With Correct Input
    Page Should Contain  Viite luotu onnistuneesti!

Added Books Are Shown In Human Readable Format
    Create Reference
    Add Book With Correct Input
    Page Should Contain  Kirjailijan sukunimi: mallikas
    Page Should Contain  Kirjailijan etunimi: mikko
    Page Should Contain  Otsikko: parhaat123
    Page Should Contain  Julkaisuvuosi: 2020
    Page Should Contain  Julkaisija: Otava

Added Books Are Shown In Bibtex Format
    Create Reference
    Add Book With Correct Input
    Page Should Contain  author = {mikko, mallikas}
    Page Should Contain  title = {parhaat123}
    Page Should Contain  year = {2020}
    Page Should Contain  publisher = {Otava}

*** Keywords ***
Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Create Reference
    Click Button  Luo viite

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
