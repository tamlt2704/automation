import urllib3
import xml.etree.ElementTree as ET
import pandas as pd
import os

# create data folder if not exist
data_folder = 'data'
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# get data
http = urllib3.PoolManager()
r = http.request('GET', "https://www.vietcombank.com.vn/ExchangeRates/ExrateXML.aspx")

# parse xml
root = ET.fromstring(r.data)
date = None
arr = []
for child in root:
    tag, attrib = child.tag, child.attrib
    if tag == 'DateTime':
        date = child.text
    elif tag == 'Exrate':
        arr.append(child.attrib)
        
# convert to dataframe and save to file
df = pd.DataFrame(arr)
df['date'] = date
df['date'] = pd.to_datetime(df['date'])
dt = str(df['date'].iloc[0])[:10]
filepath = "{}/{}.csv".format(data_folder, dt)
df.to_csv(filepath)
print("save", df.shape[0], "rows to ", data_folder)
