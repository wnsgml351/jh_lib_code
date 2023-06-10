import requests
from bs4 import BeautifulSoup

url = "https://www.toyoko-inn.com/korea/search/"

data_obj = {
    'lcl_id': 'ko',
    'prcssng_dvsn': 'dtl',
    'sel_dtl_cndtn': '',
    'sel_area_txt': '한국',
    'chck_in': '2023/06/10',
    'inn_date': '1',
    'sel_area': '8',
    'rsrv_num': '1',
    'sel_ldgngPpl': '1'
}

response = requests.post(url, data= data_obj)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

beds = soup.select('ul.btnLink03')
for bed in beds:
    links = bed.select('a')
    if len(links) > 0:
        print('잔실 있음')

