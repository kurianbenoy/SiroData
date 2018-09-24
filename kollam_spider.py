import scrapy

class ChurchSpider(scrapy.Spider):
    name = "kollam"
    start_urls = ['https://directory.mosc.in/parishes/?diocese=990',
                  'https://directory.mosc.in/parishes/page/2/?diocese=990',
                  'https://directory.mosc.in/parishes/page/3/?diocese=990',
                  'https://directory.mosc.in/parishes/page/4/?diocese=990',
                  'https://directory.mosc.in/parishes/page/5/?diocese=990',
                  'https://directory.mosc.in/parishes/page/6/?diocese=990',
                  'https://directory.mosc.in/parishes/page/7/?diocese=990',
                  'https://directory.mosc.in/parishes/page/8/?diocese=990',
                  'https://directory.mosc.in/parishes/page/9/?diocese=990',
                  'https://directory.mosc.in/parishes/page/10/?diocese=990',
                  # '',

                  ]

    def parse(self,response):
        SET_SELECTOR = '.dioceses-name'
        for i in response.css(SET_SELECTOR):
            yield {
                    'church':i.css('h3::text').extract_first(),
                    'address':i.css('p::text').extract(),

                    }

        next_page = '.pager a ::attr(href)'
        nextpage = response.css(next_page).extract_first()
        if nextpage:
            yield scrapy.Request(
                    response.urljoin(nextpage),
                    callback=self.parse
                    )
