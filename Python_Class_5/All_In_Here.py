Students = ["Sadman", "Riadul Islam", "Jahangir", "Kasem", "Rifat", "Farekul Islam", "Samim"]
print(Students[2])
print(Students[-2])
print(Students[4:])
print(len(Students))
print(Students[1:5])
print("\n")

Students = ["Sadman", "Riadul Islam", "Jahangir", "Kasem", "Rifat", "Farekul Islam", "Samim"]
print(Students)
Students.append("Najim")
print(Students)
Students.insert(1, "Abdullah")
print(Students)
Students.pop()
Students.pop()
Students.pop()
print(Students)
Students.remove("Jahangir")
print(Students)

print("\n")
Students = ["Sadman", "Riadul Islam", "Jahangir", "Kasem", "Rifat", "Kasem", "Farekul Islam", "Kasem", "Samim"]
print(Students.index("Samim"))
print(Students.count("Kasem"))
Students.sort()
print(Students)

name = [12, 34, 56, 3, 45, 7, 45, 23, 67, 45, 23, 21, 4, 23]
name.sort()
print(name)

print("\n")
Family = ["Sadman", "Riadul Islam", ["Hamida", "Ayesha", "Arian"], "Kasem", "Samim"]
print(Family[2])
print(Family[2][2])
print(Family + ["Riduan", "Rakibul Islam"])
print("\n")
print("\n")


School = []
School = School + ["kasem", "Arian", "Ayesha"]
print(School)
School.insert(4, "Najim Uddin")
print(School)
School.insert(4, "Amdad Ullah")
print(School)
print(School[4])
print("\n")
print("\n")

School = list()
School = School + ["kasem", "Arian", "Ayesha"]
print(School)
School.insert(4, "Najim Uddin")
print(School)
School.insert(4, "Amdad Ullah")
print(School)
print(School[4])
print(type(School))
print("\n")

School[1] = ["amr", "tmr", "kntmi"]
print(School)

print("\n")
print("\n")
Family = ["Sadman", "Riadul Islam", "Kasem", "Samim"]
Sub_Mem = ["Hamida", "Ayesha", "Arian"]
All_Mem = Family + Sub_Mem
print(All_Mem)
Family.extend(Sub_Mem)
print(Family)