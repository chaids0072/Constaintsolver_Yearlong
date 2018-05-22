import sys
import step1
import step2
import step3
import step4
domain_file=sys.argv[1]
problem_file=sys.argv[2]
plan=step1.get_plan(domain_file,problem_file)
problem_json=step2.get_problem_json(problem_file)
stages=step3.get_stages(plan,problem_json,problem_file)
step4.get_visualisation_json(stages)