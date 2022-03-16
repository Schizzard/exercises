# Step 3

# Solve 1 (my)
from pip._vendor import requests

url_pref = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as inf:
    resp_file = requests.get(inf.readline().strip())
    text = resp_file.text

while text[:2] != 'We':
    resp_file = requests.get(url_pref + text)
    text = resp_file.text
    print(text)

# Solve 2 (from comments)
url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
while name[:2] != 'We':
    name = requests.get(url + name).text
print(name)