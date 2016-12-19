#!/usr/bin/python

import dataFetch


#movieTitles2016 = [line.rstrip('\n') for line in open('2016')]
filmNames = [line.rstrip('\n') for line in open('filmNames')]
i = 0

for line in filmNames:
	review = dataFetch.Review(line)
	if review.movieTitle != '':
		with open('files/'+str(i), 'w+') as f:
			try:
				f.write(review.movieTitle.encode('utf-8'))
				f.write('\n')
				f.write(review.movieRating)
				f.write('\n')
				f.write(review.reviewContent.encode('utf-8'))
			except:
				continue
		i+=1
	

#for entry in reviewDatabase:
#	print entry.movieRating

#with open('JSONData.json', 'w') as f:
#     json.dump(reviewDatabase, f)
