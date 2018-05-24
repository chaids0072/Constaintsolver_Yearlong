
import unittest
import json
import re
import sys
sys.path.append('../release1.0/')
import plan_generator as step1
import problem_parser as step2
import predicates_generator as step3
import visualisation_generator as step4
import main
import copy


class integration_testing_step1234(unittest.TestCase):
    # Test if the total amount of stages is a valid number
    def test_integration_number_of_stages_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]
        self.assertTrue(len(st) > 2)

    # Test if the each stage has prefab definition
    def test_integration_number_of_prefabs_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        for counter in range(0, len(st)):
            blockexist = st[counter]['visualSprites'][0]['prefab']
            register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has showName definition
    def test_integration_number_of_shownames_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        for counter in range(0, len(st)):
            showname = st[counter]['visualSprites'][0]['showName']
            if len(str(showname)) > 0:
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has x definition
    def test_integration_number_of_xs_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            xvalue = st[counter]['visualSprites'][0]['x']
            if isinstance(xvalue, int) :
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has y definition
    def test_integration_number_of_ys_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            yvalue = st[counter]['visualSprites'][0]['y']
            if isinstance(yvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has width definition
    def test_integration_number_of_widths_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            widthvalue = st[counter]['visualSprites'][0]['width']
            if isinstance(widthvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has height definition
    def test_integration_number_of_heights_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            heightvalue = st[counter]['visualSprites'][0]['height']
            if isinstance(heightvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has y definition
    def test_integration_bounday_limit_step1234(self):
        # amount of stages from step 4
        fileop = open("../release1.0/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            minX = st[counter]['visualSprites'][0]['minX']
            maxX = st[counter]['visualSprites'][0]['maxX']
            minY = st[counter]['visualSprites'][0]['minY']
            maxY = st[counter]['visualSprites'][0]['maxY']

            if isinstance(minX, float) and isinstance(maxX, float)and \
                    isinstance(minY, float) and isinstance(maxY, float):
                register += 1
        self.assertTrue(len(st) == register)


if __name__ == '__main__':
    unittest.main()
