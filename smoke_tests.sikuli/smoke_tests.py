from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
        
    def test_001_OpenCalc(self):
        Calc.Start()
        
    def test_010_Test_ADD(self):
        click(CalcUI.button_4)
        click(CalcUI.button_plus)
        click(CalcUI.button_6)
        
        click(CalcUI.button_eq)
        assert(exists(CalcUI.result_img).highlight(2))
            

    def test_100_CloseCalc(self):
        Calc.Close()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
   
    outfile = open("Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()

