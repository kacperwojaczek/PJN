from sys import stdin
import requests
import re
import html

#print('Podaj strone.')

#start = stdin.readline().rstrip('\n')

#print('Podaj strone.')

#end = stdin.readline().rstrip('\n')


start = 1
end = 500
startCount = '1000'
endCount = ''
sort = 'COUNT'

search_uri = 'http://www.filmweb.pl/search/film?startCount=' + startCount + '&endCount=' + endCount + \
    '&sort=' + sort + '&page='
review_uri = 'http://www.filmweb.pl/reviews/'

film_links_processed = 0
accepted_reviews = 0

for i in range(int(start), int(end)+1):
   # print('------ PAGE: ' + str(i) + ' ------')
    search_page = requests.get(search_uri + str(i)).text
    film_links = re.findall('(?<=id="filmRecommendPageFB" class="hide">)(http://www\.filmweb\.pl/.+)'
                            '(?=/userRecommends#recomm-list)', search_page)
    for link in film_links:
        film_links_processed += 1
        #print('\n')
        reviews_uri = link + '/reviews'
        reviews_page = requests.get(reviews_uri).text

        unique_name = str.replace(link, 'http://www.filmweb.pl/', '')

    #    print('--- Film: ' + str(film_links_processed) + ' ---')
        #print(unique_name)

        film_name = re.search('cap s-16 top-5">(.+?)</h2>', reviews_page)
        if film_name is None:
            film_name = re.search('v:itemreviewed">(.+?)</a></h1><span class="halfSize">', reviews_page)
        if film_name is not None:
            film_name = film_name.group(1)
            film_name = html.unescape(film_name)
            print(film_name)

