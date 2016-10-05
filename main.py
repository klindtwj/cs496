import webapp2

application = webapp2.WSGIApplicatoin([
  ('/', 'base_page.HelloWorld'),
], debug=True)
