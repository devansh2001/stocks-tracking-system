import requests
import pprint
import pandas
import json

tech = [
        'MSFT,AAPL,FB,AMZN,GOOGL',
        'GOOG,SNAP,TWTR,TSLA,IRBT',
        '3IINFOTECH.NS,BIDU,TCS.NS,VIDEOIND.NS,INFY',
    ]

reliance = [
        'RCOM.NS,RELIANCE.NS,RS,RELCAPITAL.NS'
    ]

oilGasPower = [
        '533096.BO,533098.BO,533106.BO,BPCL.NS,GIPCL.NS',
        'JINDALSTEL.NS,RPOWER.NS,SAIL.NS,ONGC.NS,IOC.NS'
    ]

airlines = [
        'JBLU,AAL'
    ]

financeUSA = [
        'MER-K,GBTC,JPM,GS,BAC'
    ]

financeIndia = [
        '533171.BO,AXISBANK.NS,BANKBARODA.NS,DCBBANK.NS,HDFCBANK.NS',
        'IDBIBANK.NS,ICICIBANK.NS,SBIN.NS,YESBANK.NS,KOTAKBANK.NS'
    ]

#sectorList = [tech, reliance, oilGasPower, airlines, financeIndia, financeUSA]

sectorList = [airlines]
URL = 'https://www.worldtradingdata.com/api/v1/stock'

#key = 'CanZbO9eJSha0tW6zREL349yldJMzEy9zGGyCE2n06CP2yDf8V76zpuAmZx9'

for sector in sectorList:
    for companies in sector:
        param = {
            'symbol' : companies,
            'api_token' : key
        }
        r = requests.get(url = URL, params = param)
        data = json.dumps(r.json())
        result = json.loads(data)
        print (result['data'][0]['shares'])
        print ("*********************************")
        pprint.pprint(data, indent=2)
        print ("***********************\n\n")
        for keyList, value in (result['data'][0]).items():
            print keyList + '\t' + value
    print ("%%%%%%%%%%%%%%%%%%%%%%%%\nMoving On\n\n\n\n")
print ("Done")

