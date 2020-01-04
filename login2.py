import requests

# post 방식 Site : http://pythonscraping.com/pages/files/form.html
url = 'http://pythonscraping.com/pages/files/processing.php'

html = requests.post(url, {'firstname' : 'an', 'lastname' : 'kiwoong'})

print(html.text)
print(html.request.body)