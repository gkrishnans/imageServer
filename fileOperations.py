
from config import DATA_FILE

def getDataFromFile(key):
    dataItems = open(DATA_FILE,'r').read().split()
    for item in dataItems:
        if(key in item):
            return item.split(":")[-1]

def writeDataToFile(key,data):
    dataItems = open(DATA_FILE,'r').read().split()
    counter = 0
    for item in dataItems:
        if(key in item):
            index_of_the_record_to_be_modified = counter
            break
        counter+=1
    dataItems[index_of_the_record_to_be_modified] = dataItems[index_of_the_record_to_be_modified].split(":")[0] + ":" + str(data)
    writable_file = open(DATA_FILE,'w')
    for item in dataItems:
        writable_file.write(item + "\n")
