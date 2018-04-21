from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template

class Comments(db.Model):
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        comments_query = Comments.all()
        comments = comments_query.fetch(10)
        self.response.out.write(template.render('index.html', {"Comments" : comments}))
        
class AddComment(webapp.RequestHandler):
    def post(self):
        comment = Comments()
        comment.content = self.request.get("content")
        comment.put()
        self.redirect('/')

app = webapp.WSGIApplication([('/', MainPage), ('/add', AddComment)], debug=True)

if __name__ == "__main__":
    app.run()
