# ==========================================
# Modular Smart Inventory Auditor — Week 3
# ==========================================

MAX_CAPACITY = 500  # Business rule: maximum stock


def get_valid_input():
    """Prompt user, validate input, return integer or 'quit' signal"""
    while True:
        user_input = input("Enter stock quantity (or 'quit'): ")

        if user_input.lower() == "quit":
            return "quit"  # Signal to stop

        if user_input.isdigit():
            quantity = int(user_input)
            if quantity < 0:
                print(" Rejected: Negative quantities not allowed!")
                return None  # Failed input
            return quantity  # Valid number
        
        else:
            print(" Rejected: Please enter a valid whole number!")
            return None  # Failed input


def process_delivery(current_total, new_value):
    """Add new_value to current_total, check capacity, return new total"""
    new_total = current_total + new_value
    
    if new_total > MAX_CAPACITY:
        print(f" OVERSTOCK ALERT! Exceeded {MAX_CAPACITY}!")
        return -1  # Special signal = stop immediately
    
    return new_total


def calculate_tax(amount):
    """Return 10% tax of the given amount"""
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """Print final summary report"""
    print("\n" + "=" * 40)
    print(" INVENTORY AUDIT REPORT")
    print("=" * 40)
    print(f"Total Units Processed:   {total_units}")
    print(f"Failed/Rejected Entries: {failed_attempts}")
    print("=" * 40)


# ==========================================
# MAIN PROGRAM — Glues everything together
# ==========================================

def main():
    total_inventory = 0
    failed_entries = 0

    print(" Modular Inventory Auditor Started\n")

    while True:
        result = get_valid_input()

        # Case 1: User wants to quit
        if result == "quit":
            break

        # Case 2: Input failed
        if result is None:
            failed_entries += 1
            continue

        # Case 3: Valid input — process it
        quantity = result
        tax = calculate_tax(quantity)
        print(f" Tax for this delivery: ${tax:.2f}")

        new_total = process_delivery(total_inventory, quantity)

        # Check for overstock stop signal
        if new_total == -1:
            failed_entries += 0  # Alert triggered — not counted as failed input
            total_inventory = MAX_CAPACITY + 1  # Mark as exceeded
            break

        # Update running total
        total_inventory = new_total
        print(f" Accepted. Current total: {total_inventory}")

    # Final report
    generate_report(total_inventory, failed_entries)


# Start the program!
if __name__ == "__main__":
    main()