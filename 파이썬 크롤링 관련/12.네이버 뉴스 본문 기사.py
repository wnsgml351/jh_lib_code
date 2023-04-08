import requests

from bs4 import BeautifulSoup

import time



response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%86%8D%EA%B5%AC")

html = response.text

soup = BeautifulSoup(html, 'html.parser')

articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출

for article in articles:

    links = article.select("a.info")

    if len(links) >= 2: # 링크가 2개 이상이면

        url = links[1].attrs['href'] # 두번째 링크의 href 추출

        # 다시 request를 날려 준다

        # header는 User-agent인 경우는 인터넷사이트에서 봇을 막는 부분을 해결할 수 있다.
        response = requests.get(url)
        # response = requests.get(url, headers={'User-agent' : 'Mozila/5.0'})

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        # content = soup.select_one("#content")

        # 연예뉴스 또는 스포츠뉴스는 사이트의 생김새가 다르다

        # 즉 select 시 오류가 날 수 있다.

        # print(content.text)

        time.sleep(0.3)