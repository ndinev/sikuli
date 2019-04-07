import iHTMLTestRunner
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print "this is log from test_upper"
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print "this is log from test_isupper"
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        assert(False)

    def test_split(self):
        print "this is log from test_split"
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
      
    outfile = open("Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='TestStringMethods Report')
    runner.run(suite)
    outfile.close()