*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Is Open
    Home Page Should Be Open

Book With Correct Input Added
    Select Book Reference
    Add Book With Correct Input
    Page Should Contain  Viite luotu onnistuneesti!

Added Books Are Shown In Human Readable Format
    Create Reference
    Add Book With Correct Input
    Page Should Contain  Kirjailijan nimi: Martin, Robert
    Page Should Contain  Otsikko: Clean Code: A Handbook of Agile Software Craftsmanship
    Page Should Contain  Julkaisuvuosi: 2008    

Added Books Are Shown In Bibtex Format
    Create Reference
    Add Book With Correct Input
    Page Should Contain  @book

*** Keywords ***
Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}


Select Book Reference
    Select Radio Button  type  kirja
    Create Reference

Select Website Reference
    Select Radio Button  type  verkkosivu
    Create Reference

Create Reference
    Click Button  Luo viite

Submit Form
    Click Button  Lisää viite

Add Book With Correct Input
    ${keyword} =  Generate Random String
    Set Input Field  keyword  ${keyword}
    Set Input Field  author_surname  Martin
    Set Input Field  author_name  Robert
    Set Input Field  title  Clean Code: A Handbook of Agile Software Craftsmanship
    Set Input Field  year  2008
    Set Input Field  publisher  Prentice Hall
    Submit Form
