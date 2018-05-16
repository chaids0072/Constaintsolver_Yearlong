import urllib2, json

data = {'domain': open('domain_blocks.pddl', 'r').read(),
        'problem': open('problem_blocks.pddl', 'r').read()}

req = urllib2.Request('http://solver.planning.domains/solve')
req.add_header('Content-Type', 'application/json')
response=urllib2.urlopen(req, json.dumps(data)).read()
resp = json.loads(response)
print(resp)
with open('result.json', 'w') as f:
    f.write(response)
