import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/662.txt')

array = r.text.splitlines()

print(len(array))
