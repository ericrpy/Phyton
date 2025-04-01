import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            print(f"Texto: {text}")  
            print(f"Autor: {author}")  
            print(f"Tags: {tags}")  
            print("-" * 50)  # Separador para facilitar leitura no terminal

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }
