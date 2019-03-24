import urllib3
import xml.etree.ElementTree as ET


http = urllib3.PoolManager()
r = http.request('GET', "https://www.vietcombank.com.vn/ExchangeRates/ExrateXML.aspx")

tree = ET.fromstring(r.data)
root = tree.getroot()
for child in root:
    print(child.tag, child.text)
