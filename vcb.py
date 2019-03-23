import urllib3

http = urllib3.PoolManager()
r = http.request('GET', "https://www.vietcombank.com.vn/ExchangeRates/ExrateXML.aspx")
print(r.data)
