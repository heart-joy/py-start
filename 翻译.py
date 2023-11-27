import requests
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
         "Cookie": "your cookie"}

url = "https://fanyi.baidu.com/sug"
def change(s):
    dat={
        "kw":s
        }
    resp = requests.post(url,data = dat,headers = header)
    ch = resp.json()
    resp.close()
    dic_length = len(ch['data'])
    for i in range(dic_length):
        print("词:"+ch['data'][i]['k']+ " "+"单词意思:"+ch['data'][i]['v'])

while 1:
    s = input("英文单词:")
    if(s == "p"):
        break
    else:
        change(s)
