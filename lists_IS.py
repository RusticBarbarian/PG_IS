name = "Isaac"

subjects = {"English","Latin","History","Math","Science"}

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)



bands = {"Avenged Sevenfold","Rage Against the Machine","Kamelot","Sabaton","Powerwolf","Thy Art is Murder"}

for i in bands:
    if i == "Rage Against the Machine":
        print(i + " is the best rap/funk metal band")
    elif i == "Thy Art is Murder":
        print(i + " is a great death metal band")
    elif i == "Kamelot":
        print(i + " is the best symphonic metal band")
    else:
        print("One of the best metal bands is " + i)


bands = []

while True:
    print("What is a band you like? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        bands.append(answer)

for i in bands:
    if i == "Avenged Sevenfold":
        print(i + " is one of my favorites too!")
    else:
        print("One of your favorites is " + i)

    
