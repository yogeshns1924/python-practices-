score = int(input("enter the score:"))
if(score < 35):
    print("poor std")
elif(score > 35 and score < 70):
    print("average std")
elif(score>70 and score < 100):
    print("good std")
else:
    print("invalid input")
