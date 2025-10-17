import requests
from bs4 import BeautifulSoup

# response = requests.get('https://httpbin.org/basic-auth/foo/bar')
# print(response.status_code)
# response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
# print(response.status_code)
# print(response.request.headers['Authorization'])


# response = requests.get('https://httpbin.org/bearer')
# print(response.status_code)
# headers = {'Authorization': 'Bearer some_token'}
# response = requests.get('https://httpbin.org/bearer', headers=headers)
# print(response.status_code)


# url = 'https://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)


# url = 'https://httpbin.org/ip'
# proxies = {
#     'http': 'http://47.245.89.162:1011',
#     'https':  'https://184.95.235.194:1080'

# }
# response = requests.get(url, proxies=proxies)
# print(response)


# response = requests.get('https://avatars.mds.yandex.net/i?id=d019e29612c445c17722ed65d4609d09fc9aa865-10024314-images-thumbs&ref=rim&n=33&w=477&h=300')
# with open('nigger', 'wb') as nigga_boobs:
#     nigga_boobs.write(response.content)


# response = requests.get('https://httpbin.org/cookies', cookies= {'foo': 'bar'})
# print(response.text)

# response = (requests.get('https://httpbin.org/cookies/set/testcookie/135790'))
# print(response.cookies['testcookie'])



url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.txt, 'lxml')
quotes = soup.find_all('span', class_='txt')
print(quotes)


# url = 'https://litlife.club/genres/72-trillery'

# headers = {
#     'User-Agent': 'Opera/9.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
# }

# response = requests.get(url, headers=headers)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, 'html.parser')