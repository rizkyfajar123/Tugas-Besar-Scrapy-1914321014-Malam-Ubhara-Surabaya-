import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/eternal-sacred-king/',
	    'https://www.worldnovel.online/novel/the-rise-of-phoenixes/',
            'https://www.worldnovel.online/novel/vrmmo-the-unrivaled/',
            'https://www.worldnovel.online/novel/ed-id/',
            'https://www.worldnovel.online/novel/invincible-conqueror/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')