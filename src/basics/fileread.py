
def open_file(filename):
    file = None
    try:
        with open(filename,'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError as e:
        print(f" Error File {e}")
    else:
        print("file read successfully")    
    finally:
        if file:
            file.close()
            print("File closed")
        else:
            print("No File to close")    
    

open_file("/Users/dinesh/Downloads/AWS SAA-03 Solution.txt")
#open_file("filread.py1")