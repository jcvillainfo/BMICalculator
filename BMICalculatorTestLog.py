##This script is an implementation of unit testing for a BMI calculator application.
##It includes a class TestBMI that contains various test cases to verify the functionality of the application.
##In the TestBMI class, the test_bmi_cal method tests the application's various functions,
##such as Reset() and BMI_Cal().
##It checks whether the application behaves as expected when given valid and invalid input.
##To conduct unit testing, the script imports the unittest module, which provides a framework for writing and running tests.
##It also imports the BMICalculator2 module, which contains the implementation of the BMI calculator application.
##In the test_bmi_cal method, the script creates an instance of the application and uses various test cases to verify the behavior of the application.
##The assertEqual() method is used to check whether the expected and actual results are the same, and the assertTrue() method is used to check whether a specific condition is true.
##
##
##The test log script is useful because it allows developers to verify that their code works correctly and to identify and fix any issues before releasing the application to users.
##By running tests automatically, it ensures that the application behaves as expected under various conditions, and it allows developers to catch bugs early in the development process,
##which can save a lot of time and effort in the long run.
##
##






import unittest
from tkinter import *
import tkinter.messagebox
#Import the code to be tested

from BMICalculator2 import BMI
#Define a class for testing

class TestBMI(unittest.TestCase):

#scss

    def test_bmi_cal(self):
    # Create an instance of the BMI class
        root = Tk()
        app = BMI_Cal(root)

        # Test the Reset function
        app.test_bmi_cal.Reset()
        self.assertEqual(app.var1.get(), "")
        self.assertEqual(app.var2.get(), "")
        self.assertEqual(app.var3.get(), 0)
        self.assertEqual(app.var4.get(), 0)
        self.assertEqual(app.txtBMIResult.get("1.0", END), "\n")

        # Test the BMI_Cal function with valid input
        app.var1.set("1.8")
        app.var2.set("70")
        app.test_bmi_cal()
        self.assertEqual(float(app.txtBMIResult.get("1.0", END)), 21.6)

        # Test the BMI_Cal function with invalid input
        app.var1.set("a")
        app.var2.set("b")
        app.test_bmi_cal()
        self.assertEqual(app.var1.get(), "")
        self.assertEqual(app.var2.get(), "")
        self.assertEqual(app.var3.get(), 0)
        self.assertEqual(app.var4.get(), 0)
        self.assertEqual(app.txtBMIResult.get("1.0", END), "\n")
        self.assertTrue(tkinter.messagebox.showwarning.called)

#Run the tests if the script is being run directly

if __name__ == 'main':
    unittest.main()
