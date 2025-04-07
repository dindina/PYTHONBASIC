def openFile(filename):
    file = None

    with open(filename) as file:
        for line in file:
            print(line)



def openFile1(filename):
    file = None

    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            print(line)

#openFile("/Users/dinesh/Downloads/AWS SAA-03 Solution.txt")        
openFile1("/Users/dinesh/Downloads/AWS SAA-03 Solution.txt")        