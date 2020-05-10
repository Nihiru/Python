from selenium import webdriver
import unittest # provides lots of helper functions 
import warnings

#Tests are orgainzed in classes, which inherit from unittest.TestCase
class NewVistiorTest(unittest.TestCase):

    # runs before each test
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    ''' 
    :runs after each test
    :will run even if there's an error during the test itself.
    :destroys the opened firefox window
    '''
    def tearDown(self):
        self.browser.quit()

    # main method 
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finsih the test!!!') # to finish the test


if __name__ == '__main__':
    '''
    :unittest.main() launches the unittest test runner, which will automatically find test classes and methods in the file and run them
    :warnings='ignore' suppresses a superflous ResouceWarning
    '''
    warnings.simplefilter('ignore', category=ImportWarning)
    unittest.main()
