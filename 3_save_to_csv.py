import pandas as pd
import requests
import json



date= "2024-07-07"
url="https://vegetablemarketprice.com/api/dataapi/market/delhi/daywisedata?date="+str(date)+""
  
header={
       "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "JSESSIONID=B996C5FEEF5F71FAA879510F6CE9AFDC; _ga=GA1.1.535926437.1720420786; __gads=ID=7673b94fb107ab94:T=1720420985:RT=1720420985:S=ALNI_MZaMdMCI5z42qCo_9s6_iB2ypAYDQ; __gpi=UID=00000e86b68b21eb:T=1720420985:RT=1720420985:S=ALNI_MZfzGgSlxFImJ_lyzPSJj_A7ChXTA; __eoi=ID=8326e63330e6f562:T=1720420985:RT=1720420985:S=AA-AfjYcXGdhgxLcbO91Dln4iXv6; _ga_2RYZG7Y4NC=GS1.1.1720420786.1.1.1720420843.0.0.0; FCNEC=%5B%5B%22AKsRol9HaOJf02fJNprg3yCx_nxuucr1ZviVEst1uKkpGfGV0e-Ep06fngjTP8pPbM4Rl3TaZDRHvttV3pb1N92aNVqOV_ZGDAmWjA4iBlf9YkajjHt1wxvyrUbzlNI7hqQYbwK4OwszjCySNujnGYskYUZ2C4NpOw%3D%3D%22%5D%5D",
    "Referer": "https://vegetablemarketprice.com/market/delhi/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

data=requests.get(url,headers=header)
print(data)


js_data=json.loads(data.text)

js_arr=[]
for api in js_data["data"]:
    print(api)
    veg_name=str(api["vegetablename"])
    price=str(api["price"])
    retail_price=str(api["retailprice"])
    unit=str(api["units"])
    mall_price=str(api["shopingmallprice"])
    new_js= {
        "date":str(date),
        "veg_name":veg_name,
        "price":price,
        "retail_price":retail_price,
        "mall_price":mall_price,
        "unit":unit,
    }


df=pd.DataFrame(js_arr)
df.to_csv("out.csv")
