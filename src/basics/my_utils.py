# my_utils.py
def greet(person):
    return f"Hello, {person}!"

def main():
    print(__name__)
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()