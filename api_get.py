import requests

# res = requests.get(url, headers=headers, params=params)

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
if 'application/json' in res.headers['Content-Type']:
    res.json()
else:
    res.text

print(res.text)
print(res.json())
print(res.status_code)
