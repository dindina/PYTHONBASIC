def filegen(filename):
    file = None
    try:
        with open(filename) as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print("file not found")
    except StopIteration:
        print("No more content")        
    finally:
        print("file is end")


fileyielder = filegen("/Users/dinesh/Downloads/Sample-text.txt")
print(next(fileyielder))
print(next(fileyielder))
print(next(fileyielder))
print(next(fileyielder))


