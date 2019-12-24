import requests

url = 'https://openapi.naver.com/v1/search/movie.json?query='
request = urllib.request.Request(url)
client_id = 
client_secret = 
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
res = requests.get(url, headers=headers)