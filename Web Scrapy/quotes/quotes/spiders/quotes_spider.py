import scrapy

def clean_text(text):
    text = text.strip(u'\u201c')
    text = text.strip(u'\u201d')
    return text

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]

# criando uma classe no padrão
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
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None: # se a página é válida
            yield response.follow(next_page, callback=self.parse) # self por estar em um método dentro da classe, padrão, callback é o método