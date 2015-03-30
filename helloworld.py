import webapp2
import httplib2
from google.appengine.ext.webapp import template
from oauth2client.appengine import AppAssertionCredentials
from apiclient.discovery import build
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

class about(webapp2.RequestHandler):
    def get(self):
	self.response.write(template.render('about.html',{}))

class source(webapp2.RequestHandler):
    def get(self):
        self.response.write(template.render('srccode.html',{}))

class secpage(webapp2.RequestHandler):
    def get(self):
        self.response.write(template.render('home.html',{}))

class chart(webapp2.RequestHandler):
    def get(self):
        self.response.write(template.render('chart.html',{}))

class trial(webapp2.RequestHandler):
    def post(self):
	name = self.request.get('param1')  #reading value from client side
	print "the output is-->"
	self.response.out.write(name)      #returning value to client side


class getdata(webapp2.RequestHandler):
    def post(self):
	api_url = 'https://www.googleapis.com/auth/bigquery'
	proj_id = 'able-stock-821'
	credentials = AppAssertionCredentials(scope=api_url)
	http = credentials.authorize(httplib2.Http())
	bigquery_service = build('bigquery', 'v2', http=http)


	api_job = bigquery_service.jobs()   #creates instance of job api(creating job from big query service)
	name = self.request.get("param1")
	
	#query executed against dataset
	queryData = {'query':'SELECT SUM(word_count) as word_count,corpus_date,group_concat(corpus) as Work FROM '
'[publicdata:samples.shakespeare] WHERE word="'+name+'" and corpus_date>0 GROUP BY corpus_date ORDER BY word_count'}
	#query from the created job 
       	response = api_job.query(projectId=proj_id,body=queryData).execute()
	#self.response.out.write(response)
	table = []
	if 'rows' in response:
	  for res in response['rows']:
	  #self.response.out.write(res)
	    for key,value in res.iteritems():
	      word_count = value[0]
	      corpus_date = value[1]
	      corpus = value[2]
	      table.append({'word_count':word_count['v'],'corpus_date':corpus_date['v'],'corpus':corpus['v']})
	else:
	  table.append({'word_count':'0','corpus_date':'0','corpus':'0'})
	    
	  
	    
        self.response.out.write(json.dumps(table))



	
appli = webapp2.WSGIApplication([
    ('/', secpage),
    ('/chart',chart),
    ('/getdata',getdata),
    ('/about',about),
    ('/srccode',source),
    ('/trial',trial),
], debug=True)
