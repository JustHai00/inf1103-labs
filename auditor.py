#Initialize inventory and counters
total_inventory = 0 # start from 0
failed_inventory = 0 # have not started yet
Max_Item= 500 # maximum number of items allowed in inventory

print("Smart Inventory Auditor")
print( "Enter stock quantities one at a time, or 'quit' to exit.\n")

# 2. continuous loop
while True:
    user_input = input("Enter stock quantity: ")

    #exit condition
    if user_input.lower() == 'quit':
        break

    # 3. Validate input is a number
    if user_input.isdigit():
        quantity = int(user_input)

        