import BeautifulSoup
import random
import re
import json
import urllib2


def get_items(site):
    if site:
        agents = [
            'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',  # noqa
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',  # noqa
            'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A510F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',  # noqa
            'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',  # noqa
        ]
        r = random.sample(agents, 1)
        hdr = {'User-Agent': r[0],
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        req = urllib2.Request(site, headers=hdr)

        try:

            proxy = urllib2.ProxyHandler({'http': '185.229.65.9:41258'})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

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

        price = re.findall("\d+\,\d+", price)
        data_dict = {
            'title': title,
            'price': price[0].replace(',', '.'),
            'img': img,
            'link': site
        }
        print data_dict
        j_dict = json.dumps(data_dict)

        return j_dict
    return json.dumps({'error': 'no link provided'})
