#This python file aims to finish step 3 in our solution
#######################################################
#Input File: api_output
#Input File: pddlproblem.json
#Output : predicates.json
#######################################################

import re
import json
from pprint import pprint

#######################################################
# Clean a string
def removeUnusedChar(actionList,actionLen):
    cleanActionList = []
    for x in range(0, actionLen):
        effectElement = actionList[x]['action']
        s = (effectElement[effectElement.index("effect") + len("effect"):])[:-1] #Remove the last line because it's useless
        cleanActionList.append(s)
    return cleanActionList

#######################################################
# Checks if action contains substring
def containsSub(actionString,actionSubString):
    if actionSubString in actionString:
        return True
    else:
        return False
def get_stages(solution_json,problem_json,problem_file):


    initStage = problem_json[0]['init']
    #Getting all the objects from problem.pddl
    with open(problem_file) as f:
        text = f.read()
        st = text[text.index("objects") + len("objects"):text.index("init")]
        objects = re.findall(r'\b\S+\b',st)

    #Getting the list of Actions
    actionList = solution_json['result']['plan']
    actionLen = len(actionList)
    cleanActionList = removeUnusedChar(actionList,actionLen)


    stages = []
    for var in initStage:
        stages.append(var)

    #Patterns that will be used for matching
    otPattern = re.compile(r'on-table\s\w')
    clPattern = re.compile(r'clear\s\w')
    onPattern = re.compile(r'on\s\w\s\w')
    afPattern = re.compile(r'arm-free')
    ahPattern = re.compile(r'holding\s\w')


    #######################################################
    #This for-loop will extract all the predicates and place them into a stage json
    content = {}
    content["stages"] = []
    content["objects"] = objects
    content['stages'].append({"items":initStage.copy()})
    for x in range(0, actionLen):
        checkList = []
        finalStage = []
        ot_name = otPattern.findall(cleanActionList[x])
        cl_name = clPattern.findall(cleanActionList[x])
        on_name = onPattern.findall(cleanActionList[x])
        af_name = afPattern.findall(cleanActionList[x])
        ah_name = ahPattern.findall(cleanActionList[x])

        #Search for all the predicates in the provided strings
        for ot in ot_name:
            data_object = {}
            data_object["name"] = ot.split()[0]
            data_object["objectNames"] = []
            data_object["objectNames"].append(ot.split()[1])
            checkList.append(data_object)
        for cl in cl_name:
            data_object = {}
            data_object["name"] = cl.split()[0]
            data_object["objectNames"] = []
            data_object["objectNames"].append(cl.split()[1])
            checkList.append(data_object)
        for on in on_name:
            data_object = {}
            data_object["name"] = on.split()[0]
            data_object["objectNames"] = []
            data_object["objectNames"].append(on.split()[1])
            data_object["objectNames"].append(on.split()[2])
            checkList.append(data_object)
        for af in af_name:
            data_object = {}
            data_object["name"] = af.split()[0]
            if len(af) > 8:
                if af.split()[1] is None:
                    data_object["objectNames"] = ["No objects"]
                else:
                    data_object["objectNames"] = []
                    data_object["objectNames"].append(af.split()[1])
            else:
                data_object["objectNames"] = ["No objects"]
            checkList.append(data_object)
        for ah in ah_name:
            data_object = {}
            data_object["name"] = ah.split()[0]
            data_object["objectNames"] = []
            data_object["objectNames"].append(ah.split()[1])
            checkList.append(data_object)

        addActionListArr = []
        removeActionListArr = []
        for var in checkList:
            if containsSub(stages,var) :
                removeActionListArr.append(var)
            else:
                addActionListArr.append(var)

        # Append the list to get the final result
        for addVar in addActionListArr:
            stages.append(addVar)
        for rmVar in removeActionListArr:
            stages.remove(rmVar)


        #Append everything to get the final output - content
        result = {}
        result["items"] = stages.copy()
        result["add"] = addActionListArr
        result["remove"] = removeActionListArr
        content['stages'].append(result)
    return content
