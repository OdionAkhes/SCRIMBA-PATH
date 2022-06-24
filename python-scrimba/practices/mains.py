# def greeting(name,age):
#     print("hello " + name + ", you are " + age + "!")
#     print(f"hello {name} , you are {age} !")
    
# greeting("Brian","age")

def greeting(name,age="28"):
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,"32")
greeting("Judith")