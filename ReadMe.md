# What
Use this python scirpt to save the multi terabox share links.

# How to use
## Step1. install the requirements.
`pip install requirements.txt`

## Step2. save the links into file
For example, your file path is `/home/user/TeraboxFilesTransfer/linksfile.txt`
And the file shoud be like
```txt
https://www.terabox.com/s/aaa
https://www.terabox.com/s/bbb
```

One link in one line.

## Step3. Replace the config the TeraboxFilesTransfer.py 

First, use `F12` to open the develop tools in Chrome.
Then, open a share link in Chrome and save to your terabox.
There will be a shorturlinfo API call, just like
![shorturlinfo API ](<shorturlinfo.png>)

```
curl 'https://www.terabox.com/api/shorturlinfo?app_id=**&web=1&channel=dubox&clienttype=0&jsToken=**B&dp-logid=**&shorturl=**&root=1&scene=' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: ****' \
  -H 'Referer: https://www.terabox.com/sharing/link?surl=***' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```

Copy the app_id,jsToken,dp-logid in the URL and replace them in the TeraboxFilesTransfer.py
Copy the headers of this call, and replace the headers in the TeraboxFilesTransfer.py

## Step4. Run
`python TeraboxFilesTransfer.py`
![run](<run.png>)


# Tips
## Target Dir
By default, the script will save the file to root dir.
If you need to save to specific dir, please change the value of `transpayload`

## There are more than 1 file in the share link
Need to enhance this part, add all the files into fs_id.
```
    fs_id = respons_json['list'][0]['fs_id']
    server_filename = (respons_json['list'][0]['server_filename']).encode('utf-8')
    print("start trans: {}|{}".format(short_url, server_filename))
```