from itertools import chain
from glob import glob

file = open('problem_blocks.pddl', 'r')

lines = [line.lower() for line in file]
with open('problem_blocks.pddl', 'w') as out:
     out.writelines(lines)