import json
import time

import requests




# replasce with your hearders
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://www.terabox.com/sharing/link?surl=xxxxx',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"'
}

jsToken = 'replace_with_your_token'
dplogid = 'replace_with_your_id'
app_id = 'replace_with_your_app_id'
in_put_path = "replace with your file path"

def get_info(short_urlin):
    short_url = short_urlin.strip().split("/")[-1]
    url = "https://www.terabox.com/api/shorturlinfo?app_id={}&web=1&channel=dubox&clienttype=0&jsToken={}&dp-logid={}&shorturl={}&root=1&scene=".format(
        app_id, jsToken, dplogid, short_url
    )
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    respons_json = json.loads(response.text)
    shareid = respons_json['shareid']
    shareuk = respons_json['uk']

    fs_id = respons_json['list'][0]['fs_id']
    server_filename = (respons_json['list'][0]['server_filename']).encode('utf-8')
    print("start trans: {}|{}".format(short_url, server_filename))

    transurl = "https://www.terabox.com/share/transfer?app_id={}&web=1&channel=dubox&clienttype=0&jsToken={}&dp-logid={}&ondup=newcopy&async=1&scene=purchased_list&bdstoken=&shareid={}&from={}".format(
        app_id, jsToken, dplogid, shareid, shareuk
    )

    transpayload = 'fsidlist=%5B%22{}%22%5D&path=%2F'.format(fs_id)

    transresponse = requests.request("POST", transurl, headers=headers, data=transpayload)
    time.sleep(2)

def loop_main():
    with open(in_put_path, 'r') as f:
        for i in f.readlines():
            print("start trans {}".format(i))
            try:
                get_info(i)
                print("finish trans {}".format(i))
            except:
                print("error trans {}".format(i))
        f.close()

def loop_one():
    short_ulr = 'https://www.terabox.com/s/1tGTMma7AgoifWYjHN1k4Gw'
    get_info(short_ulr)

if __name__ == '__main__':
    loop_main()



