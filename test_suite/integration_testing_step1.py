import sys
import unittest
sys.path.append('../release1.0/')
import plan_generator as step1

class integration_testing_step1(unittest.TestCase):
    # Test if the domain file is not empty
    def test_integration__input_domain_step_1(self):
        with open("../release1.0/domain_blocks.pddl", "r") as f1:
            domaintext = f1.read()
        self.assertTrue(domaintext)
        f1.close()

    # Test if the domain file is not empty
    def test_integration__input_problem_step_1(self):
        with open("../release1.0/problems/bw01.pddl", "r") as f2:
            problemtext = f2.read()
        self.assertTrue(problemtext)
        f2.close()

    # Test if the returning value from the API is not empy
    def test_integration_api_result(self):
        self.assertTrue(step1.get_plan("../release1.0/domain_blocks.pddl", "../release1.0/problems/bw01.pddl"))

if __name__ == "__main__":
    unittest.main()
