import unittest
import sys
import unittest
sys.path.append('../release1.0/')
import plan_generator as step1
import problem_parser as step2
import re


class test_integration_step12(unittest.TestCase):
    # Test if the problem file is not empty, when step1 has been executed
    def test_integration_input_domain_step_12(self):
        step1.get_plan("../release1.0/domain_blocks.pddl", "../release1.0/problems/bw01.pddl")
        with open("../release1.0/problems/bw01.pddl", "r") as f1:
            problemTest = f1.read()
            self.assertTrue(problemTest)

    # Test if the result contains init state, when step1 has been executed
    def test_integration_init_stage_step_12(self):
        step1.get_plan("../release1.0/domain_blocks.pddl", "../release1.0/problems/bw01.pddl")
        problem_json = step2.get_problem_json("../release1.0/problems/bw01.pddl")
        text = ''.join(str(e) for e in problem_json)
        st = text[text.index("init") + len("init"):]
        self.assertTrue(st)

    # Test if the result contains goal state, when step1 has been executed
    def test_integration_goal_stage_step_12(self):
        step1.get_plan("../release1.0/domain_blocks.pddl", "../release1.0/problems/bw01.pddl")
        problem_json = step2.get_problem_json("../release1.0/problems/bw01.pddl")
        text = ''.join(str(e) for e in problem_json)
        st = text[text.index("goal") + len("goal"):]
        self.assertTrue(st)

    # Test if the result contains predicate - clear , when step1 has been executed
    def test_integration_init_stage_content_step_12_t1(self):
        step1.get_plan("../release1.0/domain_blocks.pddl", "../release1.0/problems/bw01.pddl")
        problem_json = step2.get_problem_json("../release1.0/problems/bw01.pddl")
        pattern = re.compile(r'\w\s\w')
        result = pattern.findall(str(problem_json))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
