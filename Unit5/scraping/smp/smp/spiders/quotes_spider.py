import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
'''
'''
As you can see, our Spider subclasses :class:`scrapy.Spider <scrapy.spiders.Spider>`
and defines some attributes and methods:

* :attr:`~scrapy.spiders.Spider.name`: identifies the Spider. It must be
  unique within a project, that is, you can't set the same name for different
  Spiders.

* :meth:`~scrapy.spiders.Spider.start_requests`: must return an iterable of
  Requests (you can return a list of requests or write a generator function)
  which the Spider will begin to crawl from. Subsequent requests will be
  generated successively from these initial requests.

* :meth:`~scrapy.spiders.Spider.parse`: a method that will be called to handle
  the response downloaded for each of the requests made. The response parameter
  is an instance of :class:`~scrapy.http.TextResponse` that holds
  the page content and has further helpful methods to handle it.

  The :meth:`~scrapy.spiders.Spider.parse` method usually parses the response, extracting
  the scraped data as dicts and also finding new URLs to
  follow and creating new requests (:class:`~scrapy.http.Request`) from them.
'''
