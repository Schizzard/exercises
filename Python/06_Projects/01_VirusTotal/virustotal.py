import requests
import json
from types import SimpleNamespace
import sys
import hashlib


def get_hash(filename):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def request_analysis(hash):
    apikey = "1aa0790c6e992458a82ae9dfc51f27c660be6ccf8ab86e054d80a4845ad5b938"
    url = "https://www.virustotal.com/api/v3/files/"
    headers = {
        "Accept": "application/json",
        "x-apikey": apikey
    }
    response = requests.request("GET", url+hash, headers=headers)
    return response


file = sys.argv[1]
hash = get_hash(file)
response = request_analysis(hash)

print('hash:', hash)
print()

if response.status_code == 200:
    json_resp2 = json.loads(
        response.text, object_hook=lambda d: SimpleNamespace(**d))
    print('Вредоносный:', json_resp2.data.attributes.last_analysis_stats.malicious)
    print('Подозрительный:', json_resp2.data.attributes.last_analysis_stats.suspicious)
    print('Безвредный:', json_resp2.data.attributes.last_analysis_stats.undetected)
    print()
    input('Нажмите Enter чтобы выйти')
elif response.status_code == 404:
    print('Файл не найден')
    print()
    input('Нажмите Enter чтобы выйти')
else:
    print('Ошибка', response.status_code, '-', response.reason)
    print()
    input('Нажмите Enter чтобы выйти')
