# 네이버에 검색을 하면 검색어를 기준으로 이미지 500개를 다운로드하기

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import os

# 키워드 입력
keyword = pyautogui.prompt("검색어를 입력하세요.")

# 주소창
url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"

# 폴더 생성
if not os.path.exists(f"이미지"):
    os.mkdir(f"이미지")



# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.implicitly_wait(5)   # 웹 페이지가 로딩 될때까지 5초는 기다림
browser.maximize_window()    # 화면 최대화
browser.get(url)

# 무한 스크롤 처리
# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    
    # 맨 아래로 스크롤을 내린다
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if before_h == after_h:
        break

    before_h = after_h

# 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, "._image._listImage")

for i, img in enumerate(imgs):

    # 각 이미지의 태그 주소
    img_src = img.get_attribute("src")
    print(i, img_src)

    urllib.request.urlretrieve(img_src, f"이미지\{i}.png")