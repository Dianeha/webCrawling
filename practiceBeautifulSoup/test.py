# urllib을 사용한 Request 보내기
import urllib.request
from bs4 import BeautifulSoup
 
url = "http://www.naver.com/"
req = urllib.request.urlopen(url) # url에 대한 연결요청
res = req.read() # 연결요청에 대한 응답

soup = BeautifulSoup(res,'html.parser') # BeautifulSoup 객체생성
keywords = soup.find_all('span', class_='ah_k') # 데이터에서 태그와 클래스를 찾는 함수
# print(keywords, '\n=====================================================\n', keywords[:20])


#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거
#[:20]의 이유? 인기검색어의 중복을 막고 20위까지만 출력하기 위함
keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
print(keywords)
