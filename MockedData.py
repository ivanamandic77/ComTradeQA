import json

def getTestData(filename):
    TestData=[]

    with open(filename,'r') as f:
        TestData=json.load(f) 
    return TestData