import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출
for article in articles:
    links = article.select("a.info")
    if len(links) >= 2: # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href 추출
        # 다시 request를 날려 준다
        response = requests.get(url, headers={'User-Agent' : 'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 연예 뉴스 체크
        if "entertain" in response.url: 
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        else: 
            title = soup.select_one(".media_end_head_headline")
            content = soup.select_one("#newsct_article")

        print("=======링크======= \n", url)
        print("=======제목======= \n", title.text.strip())
        print("=======본문======= \n", content.text.strip())