age=float(input("enter your age"))
member=str(input("enter if vip if not leave it blank"))
if member=="vip":
    print(" Welcome vip! Enjoy exclusive access and a free drink")
elif age >=25:
     print("Entry granted and a they get a free drink")
elif age >=18 :
    print("Entry granted but no free drink")
elif age <=17:
    print("No entry")

else:
    print("Invalid entry")


age=float(input("enter your age"))
member=str(input("enter if vip if not leave it blank"))
if age>=18:
    print("Entry granted but no free drink")
    if member=="vip":
        print("Entry granted and a they get a free drink")
    else:
        print("Entry granted but no free drink")
else:
    print("No entry")









day=str(input("enter day"))
match day:
    case "Monday":
        print("Start of workweek")
    case "Friday":
        print("End of workweek")
    case "Saturday":
        print("Time to relax")
    case _:
        print("Just another day")















