# 구글 검색해서 이미지 다운로드 하기
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

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 키워드 입력
# keyword = pyautogui.prompt("검색어를 입력하세요.")

# 주소창
# url = f"https://www.google.com/search?{keyword}&rlz=1C5CHFA_enKR1012KR1012&sxsrf=APwXEddiSCxFtvrgh4QNfsCDdurING6L8A:1683967299095&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiw2bOF8_H-AhVBEHAKHdDsC0IQ_AUoAXoECAEQAw&biw=1440&bih=711&dpr=2"
url = "https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&rlz=1C5CHFA_enKR1012KR1012&biw=1440&bih=666&tbm=isch&source=hp&biw=&bih=&ei=ylBfZJuuM-2w2roPyYeW0AQ&iflsig=AOEireoAAAAAZF9e2lQytwdz8CKyRrFXdW0ZF5IObXcq&ved=0ahUKEwibu6y09vH-AhVtmFYBHcmDBUoQ4dUDCAc&uact=5&oq=%EA%B3%A0%EC%96%91%EC%9D%B4&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIFCAAQgARQwgFYrgdgqgloAXAAeACAAWmIAZoFkgEDNS4ymAEAoAEBqgELZ3dzLXdpei1pbWewAQA&sclient=img"

# 현재 경로
current_path = os.getcwd()

# 폴더 생성
savepath = current_path + "/" + "이미지" + "/" + "고양이"
if not (os.path.isdir(savepath)):
    os.makedirs(os.path.join(savepath))

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

# 섬네일 이미지 태그 추출
thum_imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i, thum_img in enumerate(thum_imgs):

    # 이미지를 클릭하기
    thum_img.click()

    # 시간 기다리기
    time.sleep(1)

    # 큰 이미지 주소 추출
    target = browser.find_element(By.CSS_SELECTOR, "img.r48jcc")
    img_src = target.get_attribute("src")

    # 이미지 다운로드시 403 forhidden이 발생함
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)

    # 이미지 다운로드
    urllib.request.urlretrieve(img_src, f"{savepath}/{i}.png")