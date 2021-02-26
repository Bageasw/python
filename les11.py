from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
print(type(response))  # <class 'requests.models.Response'>
print(dir(response))
