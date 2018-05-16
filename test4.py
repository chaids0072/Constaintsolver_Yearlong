import re
otPattern = re.compile(ur'on-table\s\w')
clPattern = re.compile(ur'clear\s\w')
onPattern = re.compile(ur'on\s\w\s\w')
afPattern = re.compile(ur'arm-free')
ahPattern = re.compile(ur'holding')

f = open ('problem_blocks.pddl')
st = f.read()

ot_name = otPattern.findall(st)
cl_name = clPattern.findall(st)
on_name = onPattern.findall(st)
af_name = afPattern.findall(st)
ah_name = ahPattern.findall(st)



for ot in ot_name:
    print 'nameOfPredicate : ' + ot.split()[0] + ',' + '\n' +  'ObjectNames :' + ot.split()[1]
for cl in cl_name:
    print 'nameOfPredicate : ' + cl.split()[0] + ',' + '\n' + 'ObjectNames :' + cl.split()[1]
for on in on_name:
    print 'nameOfPredicate : ' + on.split()[0] + ',' + '\n' + 'ObjectNames :' + on.split()[1]+ ',' + '\n' + on.split()[2]
for af in af_name:
    print 'nameOfPredicate : ' + af.split()[0]
for ah in ah_name:
    print 'nameOfPredicate : ' + ah.split()[0]


f.close()
