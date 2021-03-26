pin_number = int(input("Please enter your pin number: "))
i = 0
while i < pin_number:
#.zfill(4) - fills code to 4 digit places
    print(str(i).zfill(4))
    i += 1
pin = str(i).zfill(4)
print(f"Your pin is: {pin}")
