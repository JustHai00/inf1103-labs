# ==========================================
# Persistent Inventory Auditor — Week 4
# ==========================================

MAX_CAPACITY = 500
DATA_FILE = "inventory.txt"


def load_inventory():
    """Read saved data from file. Return (total, history) or (0, []) if file missing."""
    try:
        with open(DATA_FILE, "r") as f:
            lines = f.read().strip().split("\n")
        
        if not lines or lines[0] == "":
            return 0, []
        
        total = int(lines[0])
        history = []
        for line in lines[1:]:
            if line.strip():
                history.append(int(line.strip()))
        
        return total, history
    
    except FileNotFoundError:
        # No saved file → start fresh
        return 0, []
    
    except Exception:
        # File broken → start fresh without crashing
        print(" Previous data file invalid — starting fresh.")
        return 0, []


def save_inventory(total_units, history_list):
    """Write final total + all transactions to file."""
    with open(DATA_FILE, "w") as f:
        f.write(f"{total_units}\n")
        for amount in history_list:
            f.write(f"{amount}\n")


def get_valid_input():
    """Prompt user, validate, return int, 'quit', or None for invalid."""
    while True:
        user_input = input("Enter stock quantity (or 'quit'): ")

        if user_input.lower() == "quit":
            return "quit"

        if user_input.isdigit():
            quantity = int(user_input)
            if quantity < 0:
                print(" Rejected: Negative quantities not allowed!")
                return None
            return quantity
        
        print(" Rejected: Please enter a valid whole number!")
        return None


def process_delivery(current_total, new_value):
    """Add new_value to total. Return new_total or -1 if over capacity."""
    new_total = current_total + new_value
    
    if new_total > MAX_CAPACITY:
        print(f" OVERSTOCK ALERT! Capacity ({MAX_CAPACITY}) exceeded!")
        return -1
    
    return new_total


def calculate_tax(amount):
    """Return 10% tax on given amount."""
    return amount * 0.10


def generate_report(total_units, failed_attempts, history_list):
    """Print final summary including transaction count."""
    print("\n" + "=" * 45)
    print(" PERSISTENT INVENTORY REPORT")
    print("=" * 45)
    print(f"Total Units Processed:   {total_units}")
    print(f"Total Transactions:      {len(history_list)}")
    print(f"Failed/Rejected Entries: {failed_attempts}")
    if history_list:
        print(f"Transaction History:     {history_list}")
    print("=" * 45)
    print(f" Data saved to {DATA_FILE}")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    #  1. Load previous work automatically
    total_inventory, transaction_history = load_inventory()
    failed_entries = 0

    print(" Persistent Inventory Auditor Started")
    if total_inventory > 0:
        print(f" Loaded saved inventory: {total_inventory} units")
    else:
        print(" Starting with empty inventory")
    print()

    #  2. Main loop
    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        
        # Tax calculation
        tax = calculate_tax(quantity)
        print(f" Tax for this delivery: ${tax:.2f}")

        # Check capacity
        new_total = process_delivery(total_inventory, quantity)
        
        if new_total == -1:
            # Overstock — save and exit
            transaction_history.append(quantity)
            total_inventory = MAX_CAPACITY + 1
            break

        #  Valid — update both total AND history list
        transaction_history.append(quantity)
        total_inventory = new_total
        print(f" Accepted. Current total: {total_inventory}")

    #  3. Save everything before exiting
    save_inventory(total_inventory, transaction_history)

    #  4. Show final summary
    generate_report(total_inventory, failed_entries, transaction_history)


if __name__ == "__main__":
    main()