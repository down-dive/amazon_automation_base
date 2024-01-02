*** Settings ***
Library    SeleniumLibrary    chrome_driver=drivers/macos/chromedrivermac    alias=SL
*** Variables ***
${BROWSER}        Chrome
${URL}            https://demoqa.com/upload-download
${FILE_PATH}      /Users/yevgeniyaterlyuk/Documents/Projects/Amazon_automation/Pages/Yev_session.docx
*** Test Cases ***
Upload File Test
    Open Browser   To Upload Page
    Upload File
*** Keywords ***
Open Browser To Upload Page
    Open Browser    ${URL}    ${BROWSER}

Upload File
    Choose File    id=file-upload    ${FILE_PATH}
    Click Button   id=submit-button
