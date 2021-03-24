code = int("0456")
start_number = int("0000")
while start_number <= 9999:
    if start_number == code:
        print(f"{start_number:04d}")
        break
    else:
        start_number += 1
