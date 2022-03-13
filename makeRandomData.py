import random

state = ["Home State", "Other State"]
category = ["SC", "ST", "GEN", "GEN-EWS", "OBC", "PWD", "EX-SER", "KM", "PH", "SBC", "MIN"]
branch = ["AI", "DS", "CS",  "IT", "ECE", "CE", "ME", "EE"]
Inter = range(80, 101)
JEEScore = range(80, 98)
# Inter = range(70, 90)
# JEEScore = range(60, 80)
with open("Data1.csv", "w") as f:
    f.write("Branch,Category,State,12th Score,JEE Score\n")
    for i in range(200):
        string = ""
        string += random.choice(branch) + ","
        string += random.choice(category) + ","
        string += random.choice(state) + ","
        string += str(random.choice(Inter)) + ","
        string += str(random.choice(JEEScore)) + "\n"
        f.write(string)