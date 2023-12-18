def hello(to="world"):
    print("hello,", to)

hello()
name = input("What is your name?")
print (f"hello, {name}")
if name!="james":
    print("wrong name")
elif name=="james":
    print("Correct")
else:
    print("bye")

match name:
    case "james" | "James" | "JAMES":
        print("Good morning")
    case "jim":
        print("good bye")
