# Step 2

# Solve 1 (my)
from pip._vendor import requests

a = requests.get('https://stepic.org/media/attachments/course67/3.6.2/373.txt')
text = a.text
b =text.splitlines()
print(len(b))


# Solve 2 (from comments)
with open('dataset_3378_2.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))