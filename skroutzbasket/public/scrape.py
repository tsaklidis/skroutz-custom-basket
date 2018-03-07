import BeautifulSoup
import urllib2
import json


def get_items(site):
    if site:
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        req = urllib2.Request(site, headers=hdr)

        try:
            page = urllib2.urlopen(req).read()
            soup = BeautifulSoup.BeautifulSoup(page)

            item = soup.find(
                'a', attrs={'class': 'product-link js-product-link content-placeholder'})
            title = soup.find('h1', attrs={'class': 'page-title'})
            img = soup.find('a', attrs={'class': 'sku-image'})

            price = item.getText()
            title = title.getText()
            img = 'https:{0}'.format(img.get('href'))

        except urllib2.HTTPError, e:
            print e.fp.read()

        pythonDictionary = {'title': title,
                            'price': price, 'img': img, 'link': site}
        dictionaryToJson = json.dumps(pythonDictionary)

        return dictionaryToJson
    return {'error': 'no link provided'}
