from django.test import SimpleTestCase #when you use database, you should use TestCase
from django.urls import reverse

# Create your tests here.
class SnickerTests(SimpleTestCase):
  def test_home_page_status(self):
    url = reverse('home')
    response = self.client.get(url)
    actual = response.status_code
    expected = 200
    self.assertEqual(actual, expected)

  def test_home_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')
