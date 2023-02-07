#No:1
name_code = ("Anis", 355, "Rashed", 356, "Kasem", 457, "Shihab", 5.00)
print(name_code[-1])


#No:2
Roll = (101, 102, 103, 104, 105)
print(Roll[2])

#No:3
distric = ("Dhaka", ("anis", "Titu", "malik"), "Chittagong", "Nuakhali", "Sylhet", "Rajshahi")
print(distric[1][1])
print(distric[::-1])

#No:4
country = ("Bangladesh", "Saudi Arabia", "Dubai", "Malaysia", "Afganistan", "Mishor", "Katar")
print("This is Third value from start: ",country[2])
print("This is Third value from last: ",country[-3])

#No:5
member = {12,13,14,15}
member.add(16)
member.add(20)
member.remove(12)
print(member)






print("\n")
print("\n")
#extra_work
name_code = ("Anis", 355, "Rashed", 356, "Kasem", 457, "Shihab", 5.00)
print(name_code[3:])
print(name_code[-1:-3])
print(name_code.index("Kasem"))