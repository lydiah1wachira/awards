from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User(id=1, username='morces', password='hdbhdvdyd')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

        
class Project(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='wakadinali')
        self.newPost = Project(title = 'Pizza', image='pizza.jpg', description = 'im hungry ', link ='http://pizzapp.com', user= 'wakadinali')
        
    def test_search_post(self):
        self.project.save()
        project = Project.search_project('test')
        self.assertTrue(len(project)>0)


class CommentsTestCase(TestCase):
    def setUp(self):
        self.comment=Comments(text="Good", pro_id=self.www.id, user = self.wakadinali)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment.Comments))

    def test_save_comments(self):
        self.comment.save_comment()
        coments = Comments.objects.all()
        self.assertEqual(len(coments),1)

    def test_delete_comment(self):
        self.comment.save_comments()
        self.comment.delete_comments()
        comment_list = Comments.objects.all()
        self.assertTrue(len(comment_list)==0)  
        
class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='morces')
        self.post = Project.objects.create(id=1, title='test post', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='describe', user=self.user, link='https://www.instagram.com/')
        self.rating = Rating.objects.create(id=1, design=6, usability=9, content=7, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))
