import pandas as pd
import json
import requests

def get_stream(url):
    s = requests.Session()
    sum_usd=0
    #Enter your API authentification key from zapper.fi 
    with s.get(url, timeout=(15,5), auth=('YOUR-API-KEY', ''), headers=None, stream=True) as resp:
        
        for line in resp.iter_lines():
            if line:
                data=line.strip()
                if data.decode('utf-8').find('data: ')!=-1:
                    totals=json.loads(data.decode('utf-8').replace('data: ',''))
                    
                    if 'totals' in totals:
                        if totals['totals']!=[]:
                            #Adding USD balances in all assets (defi, lending, staking, hard assets, NFTs etc..)
                            for i in range(0,len(totals['totals'])):
                                sum_usd+=totals['totals'][i]['balanceUSD']
                            
                        
                    
    return sum_usd
def loadusdbalance():
    # OS Location of Twitter CSV file with all addresses
    df = pd.read_csv('/xxxxx/xxxxxx/crypto_twitterAddress.csv')
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    crypto_list = df.values.tolist()
    crypto_address={}

    for i in range(0,len(crypto_list)):
        try:
            address=crypto_list[i][9].lower()
            url="https://api.zapper.fi/v2/balances?addresses%5B%5D="+address
            

            result=get_stream(url)

            crypto_address[address]={}
            crypto_address[address]['id']=int(crypto_list[i][0])
            crypto_address[address]['name']=crypto_list[i][1]
            crypto_address[address]['ens']=crypto_list[i][2]
            crypto_address[address]['handle']=crypto_list[i][3]
            crypto_address[address]['followers']=crypto_list[i][4]
            crypto_address[address]['verified']=crypto_list[i][5]
            crypto_address[address]['ranking']=crypto_list[i][8]
            crypto_address[address]['balanceUSD']=result

        except Exception as e:
            print(e)
        

         
    print(crypto_address)
    return "done"

x=loadusdbalance()
