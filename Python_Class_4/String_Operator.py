des = "the name of our country bangladesh. i love it very much."
print(len(des))
print(des.upper())
print(des.lower())
print(des.capitalize())
print(des.title())
print(des.count("e"))
print(des.count("e", 1, 12))
print(des.replace("e", "THE"))
print("\n")
print(des.split())

print(des.index("country"))

copy = ["mother", "father", "brother", "sister"]
copy.remove("mother")
print(copy)