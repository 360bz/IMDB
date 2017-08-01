import scraperwiki
import urlparse
import lxml.html

# create a new function, which gets passed a variable we're going to call 'url'
def scrape_imdb(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    #line below selects all <div class="reveal-modal medium"> - note that because there is a space in the value of the div class, we need to use a space to indicate that
    rows = root.cssselect("div.lister-item-content")
    for row in rows:
        print row
        # Set up our data record - we'll need it later
        record = {}
        a = row.cssselect("a") #grab all <a> tags within our <div>
        title = a[0].text
        #repeat process for <span class="lister-item-year text-muted unbold"> 
        item_year = row.cssselect("span.lister-item-year.text-muted.unbold")
        year = item_year[0].text
        #repeat process for <span class="value">
        value = row.cssselect("span.value")
        rating = value[0].text
        #repeat process for <p class="text-muted">
        txt = row.cssselect("span.text-muted")
        description = txt[0].txt_content()
        record['URL'] = url
        record['Title'] = title
        record['Year'] = year
        record['Rating'] = rating
        record['Description'] = memberbiog
        print record, '------------'
        # Finally, save the record to the datastore - 'Name' is our unique key
        scraperwiki.sqlite.save(["Title"], record)
        
imdblist = ['www.imdb.com/search/title?count=100&num_votes=2500,9000000&release_date=1960,2017&title_type=feature&user_rating=8.0,10&page=1&ref_=adv_nxt',  'www.imdb.com/search/title?count=100&num_votes=2500,9000000&release_date=1960,2017&title_type=feature&user_rating=8.0,10&page=2&ref_=adv_nxt', 'www.imdb.com/search/title?count=100&num_votes=2500,9000000&release_date=1960,2017&title_type=feature&user_rating=8.0,10&page=3&ref_=adv_nxt']
for url in imdblist:
    fullurl = 'http://'+url'
    print 'scraping ', fullurl
    scrape_imdb(fullurl)
