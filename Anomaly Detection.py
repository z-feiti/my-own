# -*- coding: utf-8 -*-
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None
except Exception as e:
    print('请求列表页异常：', e, url)
    return None