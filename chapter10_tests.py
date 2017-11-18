# ***
# Auto-tests for Chapter 10 tasks
# ***


import unittest
from chapter10_task1 import Employee


# class TestAnonymousSurvey(unittest.TestCase):
#     """ Tests for the class AnonymousSurvey. """
#     def setUp(self):
#         """ Create tests objects once and use for whatever method tests """
#         self.question = "What language did you first learn to sepak?"
#         self.my_survey = AnonymousSurvey(self.question)
#         self.responses = ['English', 'Spanish', 'Russian']

#     def test_store_single_response(self):
#         """ Test that single response is stored properly. """
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)

#     def test_store_three_responses(self):
#         """ Test that three or more responses are stored properly. """
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for responses in self.responses:
#             self.assertIn(response, self.my_survey.responses)


class TestEmployee(unittest.TestCase):
    """ Tests for class Employee """
    def setUp(self):
        """ Create tests objects once and use for whatever method tests """
        self.employee_good = Employee("Johnson", "Brown", 1000)

    def test_give_default_raise(self):
        self.employee_good.give_raise()

    def test_give_custom_raise(self):
        self.employee_good.give_raise(999)


unittest.main()