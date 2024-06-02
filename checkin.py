"""
@File : checkin.py
@Author : Liaoweiming
@Date : 2024/6/1 0:20
"""
import requests

def check_in(cookies):
    check_in_url = "https://neworld.cloud/user/checkin"
    check_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "0",
        "Cookie": cookies,
        "Origin": "https://neworld.cloud",
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    response_checkin = requests.post(check_in_url, headers=check_headers, verify=False)
    print(response_checkin.text)


def login(user, password):
    url = 'https://neworld.cloud/auth/login'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_pk_id.1.86b2=9c41cc0eac5d13af.1684203936.; intercom-id-sh7mjuq3=b559e5c3-1f87-4f32-92a4-ea64a84c82ef; intercom-device-id-sh7mjuq3=88077d2f-4636-4e2e-8317-c2be2ca5e4dc; intercom-session-sh7mjuq3=',
        'Origin': 'https://neworld.cloud',
        'Referer': 'https://neworld.cloud/auth/login',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'code': '',
        'email': user,
        'passwd': password,
        'fingerprint': 'dc372f07a01dc0baa781b3796fc56d57'
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    # 将Set-Cookie头拆分为单个cookie条目
    entries = response.headers.get('Set-Cookie').split("path=/")
    cookies = {}
    for entry in entries:
        if entry == "":
            continue
        key, value = entry.split("; ")[0].split("=")
        cookies[key.replace(",", "")] = value
    return cookies


add_cookies = {"intercom-device-id-sh7mjuq3": "88077d2f-4636-4e2e-8317-c2be2ca5e4dc", "intercom-id-sh7mjuq3": "b559e5c3-1f87-4f32-92a4-ea64a84c82ef", "_pk_id.1.86b2": "9c41cc0eac5d13af.1684203936."}
cookies = login("1325844611@qq.com", "1325844611")
cookies.update(add_cookies)
result = "; ".join([f"{key}={value}" for key, value in cookies.items()])
check_in(result)
