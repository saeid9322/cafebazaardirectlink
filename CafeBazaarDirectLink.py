import requests
import hashlib
import json
import time

class CofeBazaar:
    def __init__(self,PackageName):
        self.Packagename =PackageName

    def hash(string):
        hash1 = b'{"7cc78271-e338-4edc-849c-b105c5d51ba5":["getAppDownloadInfo","' + string + b'"' + b',19]}'
        m = hashlib.sha1()
        m.update(hash1)
        return (str(m.hexdigest()))
    def GettLink(packagename):
        package = packagename.encode()
    
    
    
    
        url = 'http://ad.cafebazaar.ir/json/getAppDownloadInfo'
        data = {"id":1,
                "hash":CofeBazaar.hash(package),
                "packed":"xzrBQdWmJqg\/BQN+4Ll+XCuNIhYwIpWmFRH+I1wjEKfb2NwtXaU4OO6LmDY+dcNKPh6v1a2GdLYcCdZ6NliD0nbYjcglOT7OYB9fefCL5Ec=",
                "iv":"UFDpSQCua3LwOKb8QWW4dS2PNSfMQ3ua1eWAuJY1G8xcaTS+Md+gbGMCSG3C5QJLmoiSFyOv\/QRFv6hWYsrA31ji0fGhWNGiqY9sWltqBst7YKoCqPLG0fCjoPKWPhvVhxKhjO8yT3RPalmDuPKpqGwW2fdHH+xPnuCDU51uUaE=",
                "p2":"r7oshN8AYo64PZDDlJg8TmiEiXrrBjKlwPQITF94s\/3tKsyB1PJRJM5cD\/JZBEHK\/wWvGb\/jyj0GrOgbEMONHBoLCMR\/X6RWeC59LaItQaDk\/uY3+2cEisuBw3VCAkKL887SebW0xmB\/16rNl3LxLL5\/vgCZ4jaUvIb1dj0JEH4=",
                "p1":"Kvn\/n9BLGkFAcpAWBQsAVbcF8SVnS6f3XGulLM\/J6a3SQOS5q8CagfCm2zbzQxHT0kRb9z90eCIBP9huKDth0Mu9JaAuNn9SiV7pBTs6C3hVlolY41W93hKPwhBfNyWCATymDnSjqcX\/KKNcKn3fvMU7zR0w9h\/WM\/sUkccX8pg=",
                "enc_resp":False,
                "method":"getAppDownloadInfo",
                "non_enc_params":"{\"device\":{\"mn\":260,\"abi\":\"x86\",\"sd\":19,\"bv\":\"7.12.2\",\"us\":{},\"cid\":0,\"lac\":0,\"ct\":\"\",\"id\":\"YGrrXv9TQkGyRwo6GaU0kw\",\"dd\":\"hlteatt\",\"co\":\"\",\"mc\":310,\"dm\":\"samsung\",\"do\":\"SAMSUNG-SM-N900A\",\"dpi\":160,\"abi2\":\"armeabi-v7a\",\"sz\":\"l\",\"dp\":\"hlteuc\",\"bc\":701202,\"pr\":\"\"},\"referer\":{\"name\":\"page_home|!EX!PaidRowTest|!VA!empty_key|referrer_slug=home|row-2-Best New Updates|3|test_group=A|not_initiated\"}}",
                "params":[]
        }
    
        header = {'user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SAMSUNG-SM-N900A Build/KOT49H)',
            'content-type':'application/json',
            'connection':'Keep-Alive',
            'expect':''}
        a =requests.post(url=url,headers=header,data=json.dumps(data))
    
    
        current_milli_time = lambda: int(round(time.time() * 1000))
        json1_data = json.loads(a.text)
        name = json1_data['result']['t']
        baseurl =json1_data['result']['cp'][0]
        link = (baseurl+'apks/'+name+'.apk?rand='+str(current_milli_time()))
        if name == "398047176807":
            print("err")
        else:
            return (link)
