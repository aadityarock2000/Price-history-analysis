import requests
from   bs4 import BeautifulSoup

url = 'https://fcainfoweb.nic.in/reports/report_menu_web.aspx'

headers = { 'User-Agent': 'Mozilla/5.0' }

s = requests.Session()
s.headers.update(headers)

data = {
    '__EVENTTARGET': 'ctl00$MainContent$Rbl_Rpt_type$0',
    '__VIEWSTATEENCRYPTED': '',
    'ctl00$MainContent$Ddl_Rpt_type': 'Retail',
    'ctl00$MainContent$ddl_Language': 'English',
    'ctl00$MainContent$Rbl_Rpt_type': 'Price report',
}

r = s.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data['__VIEWSTATE']          = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']
data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
data['__EVENTVALIDATION']    = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']

"""Select Price Report"""
r = s.post(url, data=data)

soup = BeautifulSoup(r.content, 'html.parser')
data['__VIEWSTATE']          = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']
data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
data['__EVENTVALIDATION']    = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']

"""Select Daily Prices"""
data['__EVENTTARGET'] = 'ctl00$MainContent$Ddl_Rpt_Option0'
data['ctl00$MainContent$Ddl_Rpt_Option0'] = 'Daily Prices'

r = s.post(url, data=data)

soup = BeautifulSoup(r.content, 'html.parser')

data['__VIEWSTATE']          = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']
data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
data['__EVENTVALIDATION']    = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']

data['__EVENTTARGET'] = ''
data['ctl00$MainContent$Txt_FrmDate']  = '25/07/2022'
data['ctl00$MainContent$btn_getdata1'] =  'Get Data'

"""Select Date + Get Data"""
r = s.post(url, data=data)