# Planning Visualisation - Visualsition File Generator

This python program takes the domain PDDL, problem PDDL and the animation profile to generate the Visualisation file for the Visualisor program.

## How to run the program
In the terminal, with python3 installed, run the following command and it will generate a file called visualisation.json in the root folder

```
python main.py [dommainfile] [problemfile] [animationprofile]

eg. python main.py domain_blocks.pddl test_problems/bw01.pdd animation_profile.json
```

## Versioning

1.0

## Limitation:

### Planning domain API
The planning domain API could only solve the block problems that the total number of block is below 25, otherwise the API has high chance return timeout error

### Parser:
Current parser we wrote is not general, it works well with the domain file and problem file we provided which use the following predicates:
* (on ?x ?y)
* (on-table ?x)
* (clear ?x)
* (arm-free)
* (holding ?x)

And also all the text must be lowercases. We have provided an converter for the block problem PDDL.
```
line=re.sub(r"\bontable\b","on-table",line)
```

The code above will replace the text "ontable" to "on-table" .
You can add more lines like this to convert your predicates to the predicates we accept.

We will update and make our parse more genearl in the future sprint


## Authors
* **Team Planning Visualisation** - *Initial work* -


## Acknowledgments

* Planning domain API (http://solver.planning.domains/)
