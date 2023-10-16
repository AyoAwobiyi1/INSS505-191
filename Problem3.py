#3) collecting five inputs from users to calculate their sum and average

information1= int(input("Enter the value for information1"))
information2= int(input("Enter the value for information2"))
information3= int(input("Enter the value for information3"))
information4= int(input("Enter the value for information4"))
information5= int(input("Enter the value for information5"))

addition= information1+information2+information3+information4+information5
average= (information1+information2+information3+information4+information5/5)
#note that the formula for average= Sum/total_no
print("addition:",addition)
print("addition:",average)