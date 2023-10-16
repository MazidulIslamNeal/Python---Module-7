names_set = set()

while True:
    name = input("Enter a name( or press enter to finish): ")
    if name == "":
        break
    if name in names_set:
        print(f"Existing name {name}")
    else:
        print(f"New name : {name}")
        names_set.add(name)
print("\nInputNames:")
for name in names_set:
    print(name)
