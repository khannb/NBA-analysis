import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
url='https://china.nba.com/'


def crawl_scroll_img():
    pageText = requests.get(url=url, headers=headers).text
    tree = etree.HTML(pageText)
    liList = tree.xpath('//*[@id="index-scrollImg"]/ul[2]/li')

    imgs = []
    for li in liList:
        newData = {}
        newData['link'] = li.xpath('./a[1]/@href')[0]
        newData['img'] = li.xpath('./a[1]/img/@src')[0]
        newData['title'] = li.xpath('./a[2]/h3/text()')[0]
        imgs.append(newData)
    # print(imgs)
    res = {
        'imgs': imgs
    }
    return res


if __name__ == '__main__':
    crawl_scroll_img()