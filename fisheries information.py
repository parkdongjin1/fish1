from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from xml.etree import ElementTree
import pandas as pd 



skey = 'sKRiKRJCRwSMLo29UDG5%2Fsi%2F05OhIMj4csMjhbzgZPE5RElkyQOqHRGOpbf8Lf139ri6XJ8o%2BUNtJgscBeL8Gg%3D%3D'

url = 'http://apis.data.go.kr/1520635/OceanMensurationService/getOceanMesurationListrisa'
Params = '?' + 'ServiceKey=' + skey + '&' + \
urlencode({quote_plus('STA_CDE') : '',     
        quote_plus('GRU_NAM') : '003',
        quote_plus('SDATE') : '20210501', 
        quote_plus('EDATE') : '20210524'
        })
print(url+Params)

getOceanMesurationListrisa="timeline15"
request = Request(url + Params)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
#print (response_body) 

root = ElementTree.fromstring(response_body)

df = pd.DataFrame()
for item in root.iter('item'):
        item_dict = []
        item_dict['cdt_1'] = item.find('cdt_1').text
        item_dict['dox_1'] = item.find('dox_1').text 
        item_dict['gruNam'] = item.find('gruNam').text 
        item_dict['obsDtm'] = item.find('obsDtm').text 
        item_dict['obsTim'] = item.find('obsTim').text 
        item_dict['staCde'] = item.find('staCde').text 
        item_dict['staNamKor'] = item.find('staNamKor').text
        item_dict['wtrTmp_1'] = item.find('wtrTmp_1').text
        item_dict['resultMsg'] = item.find('resultMsg').text
        item_dict['resultCode'] = item.find('resultCode').text
        df = df.append(item_dict,ignore_index=True)
df




