from mongoengine import *
connect('twitter_db', host='mongo', port=27017)

class TwitterProvider(EmbeddedDocument):
  tokenSecret = StringField(default='', max_length=200)
  token = StringField(default='', max_length=200)
  twitterId = StringField(db_field='id', default='', max_length=200)

class User(Document):
  # userId = ObjectIdField(db_field='_id')
  email = StringField(required=True, max_length=200)
  twitterProvider = EmbeddedDocumentField(TwitterProvider)


# class Comment(EmbeddedDocument):
#     content = StringField()

# class Page(Document):
#     comments = ListField(EmbeddedDocumentField(Comment))

# comment1 = Comment(content='Good work!')
# comment2 = Comment(content='Nice article!')
# page = Page(comments=[comment1, comment2])


# {
# "_id":"5aaeb3249c2e8dd05f939ba2",
# "email":"wardnath.alt@gmail.com",
# "twitterProvider":
# {
# "tokenSecret":"y0FP0Ob01AqnXOgy2QRRUxrviEhJWDF7Zn3wH4bWtUA3c",
# "token":"2993000517-gFpmP2Y4NcZb4qgtBrgzDu43r2egl5QiAgwCo7t",
# "id":"2993000517"
# },
# "__v":0}