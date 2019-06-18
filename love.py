# -*- coding: utf-8 -*-
# Nola

import requests
from lxml import etree


url = 'https://www.qingshiwang.com/yinwenqingshi/57.html'  # 入口url
refer = 'https://www.qingshiwang.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def source_datas():
    res = requests.get(url, headers=headers)
    # print(res.content.decode('utf-8'))
    contents = res.content.decode('utf-8')
    html = etree.HTML(contents)

    link_title = {}
    for i in [2, 3, 5, 6]:
        x = '//*[@id="SideBar"]/div[{}]/div/ul/li/a/@href'
        t = '//*[@id="SideBar"]/div[{}]/div/ul/li/a/text()'
        x = x.format(str(i))
        t = t.format(str(i))
        links = html.xpath(x)  # 获取连接
        titles = html.xpath(t)  # 获取标题
        link_title.update(dict(zip(links, titles)))
    return  link_title


if __name__ == '__main__':
    l = source_datas()
    print(l)



# '//*[@id="node-8890"]/div[2]/p/text()'  # 获取文章内容
