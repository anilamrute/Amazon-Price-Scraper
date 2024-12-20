import csv
import datetime
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

def check_price():

    URL = 'https://www.amazon.com/dp/B00OTYRITE/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B00OTYRITE&pd_rd_w=JUPjn&content-id=amzn1.sym.7446a9d1-25fe-4460-b135-a60336bad2c9&pf_rd_p=7446a9d1-25fe-4460-b135-a60336bad2c9&pf_rd_r=NRZT5H87WH4MVHTJB60E&pd_rd_wg=s1gKI&pd_rd_r=1f31b2ed-fc36-49fd-b32a-8aefa47a2070&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "DNT": "1", 
        "Connection": "close", 
        "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(class_='a-offscreen').get_text().strip()[1:]

    today = datetime.date.today()

    # Ensure header is a list of strings
    header = ["Title", "Price","Date"]

    # Ensure data is a list of the actual values for each column
    data = [title, price,today]

    # Open the CSV file in append mode so it does not overwrite existing data
    with open("AmazonDataset.csv", 'a+', newline='', encoding='UTF8') as f:
        write = csv.writer(f)
        # write.writerow(header)  # Correctly writing headers
        write.writerow(data)    # Writing the scraped data


while True:
    check_price()
    time.sleep(5)



df=pd.read_csv(r"D:\Anil\Python\Anaconda\AmazonDataset.csv")

print(df)


