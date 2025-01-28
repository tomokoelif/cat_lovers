from django.test import TestCase
from django.urls import reverse
from about.models import About  # 正しいモジュールからインポート
from about.forms import CollaborateForm
from django.contrib.auth.models import User
from blog.models import Post  # 正しいモジュールからインポート
from blog.forms import CommentForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)


class TestPostDetailView(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        print(response.content)  # デバッグ用にレスポンスの内容を出力
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)