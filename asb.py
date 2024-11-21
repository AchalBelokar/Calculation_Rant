rent = int(input("enter your hostel/flat rent = "))
food = int(input("enter the amount of food ordered = "))
electricity_sped = int(input("enter the total of electricicty spend = "))
charge_per_unit = int(input("enter the charge per unit = "))
persons = int(input("enter the number of persons living in room/flat = "))
total_bill = electricity_sped * charge_per_unit
output = (food + rent + total_bill) // persons
print("each person will pay = ", output)



