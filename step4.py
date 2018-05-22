import json
import random_color
import copy
import custom_functions


def initialObjects(objectList, animation_profile):
    unsolvedObjects = {}
    for objectname in objectList:
        unsolvedObjects[objectname] = {}
        objType = animation_profile["objects"]["default"]
        # update the value for each
        for objproperty in animation_profile["shape"][objType]:
            value = animation_profile["shape"][objType][objproperty]
            if value is not False:
                if value == "randomcolor":
                    unsolvedObjects[objectname][
                        objproperty] = random_color.get_random_color()
                    continue
                unsolvedObjects[objectname][objproperty] = value
            else:
                unsolvedObjects[objectname][objproperty] = False
        unsolvedObjects[objectname]["name"] = objectname
    return unsolvedObjects


def check_rule_complete(predicate, objectsDic, predicates_rules):
    predicatename = predicate["name"]
    objectnamelist = predicate["objectNames"]
    predicate_rule = predicates_rules[predicatename]
    for rulename in predicate_rule["rules"]:
        rule = predicate_rule[rulename]
        for key in rule:
            # 0 is on the left side of equation
            if key != "value" and key != "0":
                property_check = rule[key]
                objectname = objectnamelist[int(key)]
                if objectsDic[objectname][property_check] is False:
                    return False
    return True


def applypredicates(predicate, objectsDic, predicates_rules, space):
    pname = predicate["name"]
    objects = predicate["objectNames"]
    left = objects[0]
    for rulename in predicates_rules[pname]["rules"]:
        propertyname = predicates_rules[pname][rulename]["0"]
        value = predicates_rules[pname][rulename]["value"]
        rule = predicates_rules[pname][rulename]
        if "function" in value:
            if value["function"] == "distributex":
                objectsDic[left][propertyname] = custom_functions.distributex(
                    left, space, 20, 80, False)
        elif "equal" in value:
            right_value = value["equal"]
            if right_value in rule:
                right_proterpy = rule[right_value]
                right_object = objects[int(right_value)]
                objectsDic[left][propertyname] = objectsDic[
                    right_object][right_proterpy]
            else:
                objectsDic[left][propertyname] = right_value

        elif "add" in value:
            rightvalue = 0
            for additem in value["add"]:
                if additem in rule:
                    right_property = rule[additem]
                    right_object = objects[int(additem)]
                    addvalue = objectsDic[right_object][right_property]
                    rightvalue += addvalue
                else:
                    rightvalue += additem
            objectsDic[left][propertyname] = rightvalue


def solvepredicates(predicates, objectsDic, predicates_rules, space):
    while (len(predicates) > 0):
        predicate = predicates.pop(0)
        if predicate["name"] not in predicates_rules:
            continue
        if check_rule_complete(predicate, objectsDic, predicates_rules):
            applypredicates(predicate, objectsDic, predicates_rules, space)
        else:
            if len(predicates) == 0:
                return False
            predicates.append(predicate)
    return True


def solveAllStages(stages, objectsDic, predicates_rules, space):
    result = {}
    result["visualStages"] = []
    for stage in stages:
        stageDic = {}
        objectDicCopy = copy.deepcopy(objectsDic)
        predicates = stage["items"]
        solvepredicates(predicates, objectDicCopy, predicates_rules, space)
        stageDic["visualSprites"] = objectDicCopy
        result["visualStages"].append(stageDic)
    return result


def transfer(oneStep, initialobjects, panelWidth, panelHeight):
    # list that stores object name
    finalFile = {}
    temp = []
    # dict that stores new position info
    dictX = {"minX": "",
             "maxX": "",
             "minY": "",
             "maxY": ""}
    # new position info
    minX = 0.0
    maxX = 0.0
    minY = 0.0
    maxY = 0.0
    # generate new json file
    for i, object in enumerate(initialobjects):
        temp.append(oneStep[object])
        # get all information about position
        xNum = oneStep[object]["x"]
        yNum = oneStep[object]["y"]
        width = oneStep[object]["width"]
        height = oneStep[object]["height"]
        # transfer the position info into position needed in Unity
        minX = xNum / panelWidth
        maxX = (xNum + width) / panelWidth
        minY = yNum / panelHeight
        maxY = (yNum + height) / panelHeight
        dictX["minX"] = round(minX, 3)
        dictX["maxX"] = round(maxX, 3)
        dictX["minY"] = round(minY, 3)
        dictX["maxY"] = round(maxY, 3)
        # update the old dict
        temp[i].update(dictX)
        finalFile["visualSprites"] = temp
    return finalFile


def get_panel_size(result, padding=20):
    lists = result["visualStages"]
    maxX = 0
    maxY = 0
    for stage in lists:
        stageitems = stage["visualSprites"]
        for item in stageitems:
            x = stageitems[item]["x"] + stageitems[item]["width"] + padding
            y = stageitems[item]["y"] + stageitems[item]["height"] + padding
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
    return maxX, maxY


def generate_visualisation_file(result, objectList):
    final = {"visualStages": []}
    oneStep = {}
    spriteList = []
    lists = result["visualStages"]
    panelWidth, panelHeight = get_panel_size(result)
    print(panelHeight)
    for i, step in enumerate(lists):
        oneStep = lists[i]["visualSprites"]
        spriteList.append(
            transfer(oneStep, objectList, panelWidth, panelHeight))
        final["visualStages"] = spriteList

    with open('visualisation.json', 'w') as outfile:
        json.dump(final, outfile)


def get_visualisation_json(predicates):
    apfile = "animation_profile.json"
    f1 = open(apfile)
    content1 = f1.read()
    animation_profile = json.loads(content1)

    objectList = copy.deepcopy(predicates["objects"])
    stages = copy.deepcopy(predicates["stages"])
    predicates_rules = animation_profile["predicates_rules"]

    objectsDic = initialObjects(objectList, animation_profile)
    objectsDic["Claw"] = {"name": "Claw", "prefab": "Claw", "color": {
        "r": 0.0, "g": 0.0, "b": 0.0, "a": 1.0}, "showName": False, "x": 230, "y": 500, "width": 80, "height": 40}
    space = custom_functions.init_space(len(objectList))
    result = solveAllStages(stages, objectsDic, predicates_rules, space)
    generate_visualisation_file(result, list(objectsDic.keys()))
