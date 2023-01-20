from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test content', publish_date='2022-01-01', author=self.user)
        self.post_data = {'title': 'Test Post Updated', 'content': 'Test content updated', 'publish_date': '2022-01-01'}

    def test_posts_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)
        self.assertEqual(response.context['posts'][0], self.post)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create-post'), data=self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('update-post', args=[self.post.id]), data=self.post_data)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Test Post Updated')
        self.assertEqual(self.post.content, 'Test content updated')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete-post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
