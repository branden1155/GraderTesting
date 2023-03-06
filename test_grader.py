import unittest

#Importing global Vars from grader.py and Grader Class.
from grader import name
from grader import assignment
from grader import grade
from grader import Grader

gr = Grader()

#Setting Global Vars values
name = name
assignment = assignment

class Test(unittest.TestCase):

    #EXAMPLE TEST ------------------------------------------------------------------------------

    def test_gradeInfo(self):
        self.assertEqual(gr.gradeInfo(),"You did not entered a grade number between 0 ant 100.")


    #FUNCTIONAL COVERAGE ------------------------------------------------------------------------------

    #Testing if the function is working correctly or not, we are checking for a correct grade,
    #and responsible name, and assignment name to qualify if the function is going to work correctly.

    def testfunction_gradeInfo(self):
        functionBool = False
        if grade > -1 and grade <= 100 and name.isalpha() and assignment.isalpha():
            functionBool = True
        self.assertTrue(functionBool, "Grader and GradeInfo Are not working correctly.")
            
    #STATEMENT COVERAGE ------------------------------------------------------------------------------

    #Testing each statement that is nested inside the Function. In this example, the if's and elif's were the statements that were tested.

    def testifA_gradeInfo(self):
        ifgradeA = False
        if(grade >=90 and grade <=100):
            ifgradeA = True
        self.assertTrue(ifgradeA, "Grade was not a A")
    
    def testifB_gradeInfo(self):
        ifgradeB = False
        if(grade >=80 and grade <90):
            ifgradeB = True
        self.assertTrue(ifgradeB, "Grade was not a B")

    def testifC_gradeInfo(self):
        ifgradeC = False
        if(grade >=70 and grade <80):
            ifgradeC = True
        self.assertTrue(ifgradeC, "Grade was not a C")
    
    def testifD_gradeInfo(self):
        ifgradeB = False
        if(grade >=61 and grade <70):
            ifgradeB = True
        self.assertTrue(ifgradeB, "Grade was not a D")
        
    def testiflast_gradeInfo(self):
        ifgradeNone = False
        if(grade <60 and grade >=0):
            ifgradeNone = True
        self.assertTrue(ifgradeNone, "Grade was not a Last position")

    #CONDITION COVERAGE ------------------------------------------------------------------------------

    #Testing each Condition that is needed inside the function if they are True or False, making sure and testing if we are
    #getting a responisble input needed to run the function.

    def testifName_gradeInfo(self):
        ifName = name.isalpha()
        self.assertTrue(ifName, "There was not a name Submitted.")

    def testifAssignment_gradeInfo(self):
        ifAssignment = assignment.isalpha()
        self.assertTrue(ifAssignment, "There was not an Assignment Submitted.")
        
    def testifNumber_gradeInfo(self):
        ifNumber = False
        if grade > -1:
            ifNumber = True
        self.assertTrue(ifNumber, "There was not a number submitted, the number submitted is "+str(grade)+".")

    #BRANCH COVERAGE ------------------------------------------------------------------------------

    #Testing Sub Conditions of the CONDITION COVERAGE, There are 9 Branch Coverages possible, done by cycling through each branch inside the function.

    def testbranch_gradeInfo(self):
        if grade >=90 and grade <=100:
            self.assertEqual(grade, "The grade was a A")
        elif grade >=80 and grade <90:
            self.assertEqual(grade, "The grade was  a B")
        elif grade >=70 and grade <80:
            self.assertEqual(grade, "The grade was a C")
        elif grade >=61 and grade <70:
            self.assertEqual(grade, "The grade was a D")
        elif grade <=60 and grade >=0:
            self.assertEqual(grade, "The grade was a Grade")