import pandas as pd

input =[]

print("if u wanna stop write quit in place of name")
while True:
    name = input("enter event:")
    if name.lower() == 'quit':
        break
    date=input("enter date: ")
    note=input("enter a note :")
    data={"event":name,"date":date,"note":note}
    input.append(data)

df = pd.DataFrame(input)

calander = pd.read_csv('calander.csv')