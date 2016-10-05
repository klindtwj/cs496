import webapp2

class HelloWorld(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-type'] = 'test/plain'
    self.response.write('Hello again world')
