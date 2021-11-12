from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        """Create a new test database with one entry """

        Post.objects.create(text="Sample random text")

    def test_text_content(self):
        """Check that the db field contains the entry"""

        # variable for the 1st id in the Post model
        post = Post.objects.get(id=1)

        # string of the value in post.text 
        expected_object_name = f"{post.text}"

        #check the newly created entry matches the input
        self.assertEqual(expected_object_name, "Sample random text")

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Yet another random text")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, 'home.html')

