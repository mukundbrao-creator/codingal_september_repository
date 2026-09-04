print("=== ATM Cash Dispenser ===\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Please enter your name: ")
    amount = int(input(f"Hello {name}, please enter how much you would like to withdraw. \n"))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        continue
    print(f"Printing {amount} units for {name}: ")
    idx = 1
    remaining = amount
    if idx == 1:
        value = 100
    elif idx == 2:
        value = 50
    elif idx == 3:
        value = 20
    elif idx == 4:
        value = 10
    elif idx == 5:
        value = 5
    else:
        value = 1
    count = remaining // value
    print(f"{count} x {value} unit notes = {count * value}")
    remaining -= count * value
    if value == 100:
        total_100 += count
    elif value == 50:
        total_50 += count
    elif value == 20:
        total_20 += count
    elif value == 10:
        total_10 += count
    elif value == 5:
        total_5 += count
    else:
        total_1 += count
    idx += 1
    customers_served += 1
    total_dispensed += amount
    print(f"Transaction complete, {name}.")
    again = input("Is there another customer? (yes/no) ").strip().lower()
    if again != "yes":
        serving = False
print("===== Daily Denomination Report =====\n")
for slot in range (1, 7):
    if slot == 1:
        value, total = 100, total_100
    elif slot == 2:
        value, total = 50, total_50
    elif slot == 3:
        value, total = 20, total_20
    elif slot == 4:
        value, total = 10, total_10
    elif slot == 5:
        value, total = 5, total_5
    else:
        value, total = 1, total_1
    if value > 0:
        print(f"{value} unit notes dispensed: = {total}", end='')
        for note in range (total):
            print("=", end='')
        print("")
print("==== End of Day ATM Report =====")
print(f"Customers Served: {customers_served}")
print(f"Total Dispensed: {total_dispensed}")
print("Session closed. Have a great day!")