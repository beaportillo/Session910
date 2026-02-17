def greeting():
    print("Hello")
greeting()


def greeting2(name):
    print("Hello ", name)

for i in range (10):
    greeting()
print("I can take a break")
for i in range(5):
    greeting2("John")


def greeting3(name):
    message = ""
    message += f"Hello {name}"
    message 
    return message
print(greeting3("John"))