import json

json_text = '{"message":"And this is a second message"}'
obj = json.loads(json_text)

key = "message"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")


# https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37