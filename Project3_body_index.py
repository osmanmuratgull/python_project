size=int(input("Enter your height (in cm): "))
kg =float(input("enter your weight: "))
vki=kg 16/((size/100)**2)
print("Your body mass index {}".format(round(vki,2)))
print("Your status: ")
if vki <=18.5:
    print("Weak")
    print("{} you need to gain kilograms".format(round(18.5*((size/100)**2)-kg ,2)))
elif vki <=24.9:
    print("Normal")
elif vki<=29.9:
    print("Overweight")
    print("{} you need to lose kilograms".format(round(kg -24.9*((size / 100) ** 2)),2))
elif vki<=39.9:
    print("Obese")
    print("{} you need to lose kilograms".format(round(kg  - 24.9 * ((size / 100) ** 2)), 2))
else:
    print("extremely obese")
    print("{} you need to lose kilograms".format(round(kg  - 24.9 * ((size / 100) ** 2)), 2))
