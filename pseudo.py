import requests

r = requests.get('http://www.ccel.org/ccel/easton/ebd2.xml')

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)