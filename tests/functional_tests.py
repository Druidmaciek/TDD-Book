from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about new online to-do app and wants to check it out
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in to-do list

        # There is still a text box inviting h.r t, 'dd 'n,th.r yt.m3
        # She enters "Use peacock feathers to make a fly"

        # THe page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # That the site has generated a unique URL for her -- this is some
        # explanator text to that effec

        # She visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')