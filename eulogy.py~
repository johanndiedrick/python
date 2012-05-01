#Eulogy

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import random
import urllib2
import simplejson
import re
import requests
from bs4 import BeautifulSoup
from random import choice



from tornado.options import define, options

from context_free import ContextFree
from context_free_reader import add_rules_from_file


define("port", default=8888, help="run on the given port", type=int)
define("grammar", default="definitions.grammar", help="grammar file to load", type=str)
define("axiom", default="Def", help="axiom to expand from grammar", type=str)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
				(r"/", IndexHandler),
				(r"/eulogy", EulogyHandler)
		]

	
		settings = dict(
				template_path = os.path.join(os.path.dirname(__file__), "templates"),
				static_path = os.path.join(os.path.dirname(__file__), "static"), 
				debug=True
		)
		tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")


class EulogyHandler(tornado.web.RequestHandler):
	def post(self):
		searchTerm=self.get_argument('word')
		
		scraped_text = list()
		words = list()

		output_line = list()

		real_words_cleaned  = list()


		big_list_of_words = list()
		
		listOfUrls = []
		real_words_file = open("sowpods.txt")
		real_words = real_words_file.readlines()
		real_words_file.close()


		for line in real_words:
			line = line.strip()
			real_words_cleaned.append(line)
		

#function to use if we want to control size of string
# from bs4 import SoupStrainer
# 
# only_a_tags = SoupStrainer("a")
# 
# only_tags_with_id_link2 = SoupStrainer(id="link2")
# 
# def is_short_string(string):
#     return len(string) < 10
# 
# only_short_strings = SoupStrainer(text=is_short_string)


											# The request also includes the userip parameter which provides the end
											# user's IP address. Doing so will help distinguish this legitimate
											# server-side traffic from traffic which doesn't come from an end-user.



		id = searchTerm								# dynamic id from site in a post request
		url = ('https://ajax.googleapis.com/ajax/services/search/web'
       '?v=1.0&q='+ id + '&userip=USERS-IP-ADDRESS')

		request = urllib2.Request(url, None, {'Referer': "www.google.com" })
		response = urllib2.urlopen(request)  # opening url

    							# Process the JSON string.
		results = simplejson.load(response)
		results = results["responseData"]
		results = results['cursor']
		nofResults = (results["resultCount"])
										# set a variable for search result pagination
		nom = long(nofResults.replace(",", ""))/ 10000

		print "Results searched...." ,nom
		results = results["moreResultsUrl"]
#print results

								#results = results['resultCount']

								#regex to add number to results
		split = re.split("start=0", results)
		newurl= split[0] + "start=" + str(nom) +split[1]
		print "found!!!"+ newurl 

		r = requests.get(newurl)
								# print r.status_code
								# print r.headers['content-type']

		r= r.text
		soup = BeautifulSoup(r)
		all = []
		for link in soup.find_all("a"):
			all.append(link.get("href"))

		for s in all:					#iterate through the document and extract links
			if re.findall("/url?", s):
				split1 = re.split("&", s)
            		    	split2 =re.split("=", split1[0])
            		    	deathlinks=[]
            		    	sp =(split2[1]).split("//n")
                #print sp[0]
                
                				# list of lists
            		    	listOfUrls.append(sp[0])

								#random url selected




		def myloop(listOfUrls):
			deathUrl = choice(listOfUrls)
			listOfUrls.remove(deathUrl)
			if len(listOfUrls) > 0: 
				#printing the selected url
				print "Dying! " + deathUrl
				# for url in deathUrl:    #open urls and parse 
				death= urllib2.urlopen(deathUrl)
				try:
					death = death.read()
					deathSoup = BeautifulSoup(death)
			#		print (deathSoup.get_text())
					for string in deathSoup.stripped_strings:
						tocontextfree = (string)
						scraped_text.append(tocontextfree)
					for lines in scraped_text:
						lines = lines.strip()
						whatever = lines.split(" ")	
						for word in whatever:
							word = word.lower()
							word = word.encode('ascii', 'ignore')
							big_list_of_words.append(word)
		
					for word in big_list_of_words:
						if word in real_words_cleaned:
							 output_line.append(word)
				#		print output_line


				except (Exception,NameError,urllib2.HTTPError,urllib2.URLError):
					# deathUrl = choice(listOfUrls)
					print "I love errors"
					print deathUrl
					return myloop(listOfUrls)
		myloop(listOfUrls)
		print 'end'


#		for string in deathSoup.stripped_strings:
							 								#context free variable from site
#			tocontextfree = (string)
#			scraped_text.append(tocontextfree)



#		for lines in scraped_text:
#			lines = lines.strip()
#			whatever = lines.split(" ")	
#			for word in whatever:
#				word = word.lower()
#				word = word.encode('ascii', 'ignore')
#				big_list_of_words.append(word)
		
#		for word in big_list_of_words:
#			if word in real_words_cleaned:
#				output_line.append(word)
		sizeOfOutput = len(output_line)
		city = output_line[random.randrange(1,sizeOfOutput)]
		father = output_line[random.randrange(1,sizeOfOutput)]
		mother = output_line[random.randrange(1,sizeOfOutput)]
		date = output_line[random.randrange(1,sizeOfOutput)]
		year = output_line[random.randrange(1,sizeOfOutput)]
		school = output_line[random.randrange(1,sizeOfOutput)]
		degree = output_line[random.randrange(1,sizeOfOutput)]
		company = output_line[random.randrange(1,sizeOfOutput)]
		job = output_line[random.randrange(1,sizeOfOutput)]
		marrage_year = output_line[random.randrange(1,sizeOfOutput)]
		spouse = output_line[random.randrange(1,sizeOfOutput)]
		marrage_years = output_line[random.randrange(1,sizeOfOutput)]
		community = output_line[random.randrange(1,sizeOfOutput)]
		hobby = output_line[random.randrange(1,sizeOfOutput)]
		quality = output_line[random.randrange(1,sizeOfOutput)]
		character1 = output_line[random.randrange(1,sizeOfOutput)]
		character2 = output_line[random.randrange(1,sizeOfOutput)]
		character3 = output_line[random.randrange(1,sizeOfOutput)]
		value = output_line[random.randrange(1,sizeOfOutput)]

		words = city + " " + mother + " " + father

		self.render(
				'eulogy.html', 
				word=searchTerm, 
				output=' '.join(output_line), 
				randomWords = words,
				city = city,
				father = father,
				mother = mother,
				date = date,
				year = year,
				school = school,
				degree = degree,
				company = company,
				job = job,
				marrage_year = marrage_year,
				spouse = spouse,
				marrage_years = marrage_years,
				community = community,
				hobby = hobby,
				quality = quality,
				character1 = character1,
				character2 = character2,
				character3 = character3,
				value = value


				)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
