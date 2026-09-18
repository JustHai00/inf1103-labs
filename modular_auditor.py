# ==========================================
# Smart Inventory Auditor — INDENTED CORRECTLY
# ==========================================

total_inventory = 0
failed_inventory = 0
MAX_CAPACITY = 500

print(" Smart Inventory Auditor Started")

while True:
    # ↓ 4 spaces → belongs to while loop
    user_input = input("Enter stock quantity (or 'quit'): ")

    # Exit check
    if user_input.lower() == "quit":
        break

    # Validate: is it a number?
    if user_input.isdigit():
        # ↓ 8 spaces → belongs to "if isdigit()" block
        quantity = int(user_input)

        # Check negative — SAME indent as quantity = int(...)
        if quantity < 0:
            # ↓ 12 spaces → belongs to "if quantity < 0"
            print(" Rejected: Negative quantities are not allowed.")
            failed_inventory += 1
        else:
            # ↓ 12 spaces → belongs to "else" (not negative)
            total_inventory += quantity
            print(f" Accepted. Current total: {total_inventory}")

            # Check overstock
            if total_inventory > MAX_CAPACITY:
                print(f" OVERSTOCK ALERT! Exceeded {MAX_CAPACITY}!")
                break

    else:
        # ↓ 8 spaces → belongs to "else" (NOT a number)
        print(" Rejected: Please enter a valid whole number.")
        failed_inventory += 1


# Final report — NO indent (back to level 0)
print("\n===== INVENTORY SUMMARY =====")
print(f"Total Units Processed: {total_inventory}")
print(f"Failed/Rejected Entries: {failed_inventory}")

