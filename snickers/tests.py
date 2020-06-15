from django.test import SimpleTestCase #when you use database, you should use TestCase
from django.urls import reverse

# Create your tests here.
class SnickerTests(SimpleTestCase):

  def test_all_page_status(self):
    pages = ['home','about','doggy_home','cat_home']

    for page in pages:
      self.url_testing_200_status(page)
  
  def test_templates_for_each_url(self):
    pages = [['home','home.html'],['about','about.html'],['doggy_home','dog_adoption.html'],['cat_home','cat_adoption.html']]
    for url_list in pages:
      self.template_testing_generic(url_list[0],url_list[1])

  def url_testing_200_status(self, url_name):
    url = reverse(url_name)
    response = self.client.get(url)
    actual = response.status_code
    expected = 200
    self.assertEqual(actual, expected)
  
  def template_testing_generic(self, url_name, html_page):
    url = reverse(url_name)
    response = self.client.get(url)
    self.assertTemplateUsed(response, html_page)
    self.assertTemplateUsed(response, 'base.html')

