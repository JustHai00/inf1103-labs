# ==========================================
# INF1103 Week 3 — Modular Inventory Auditor
# Fully Complete: includes negative value check
# ==========================================

# --------------------------
# Function 1: Get & Validate Input
# --------------------------
def get_valid_input():
    """Prompt user, validate input. Returns integer, 'quit', or None for invalid."""
    user_input = input("Enter stock quantity (or type 'quit' to finish): ")
    
    # Check for quit command
    if user_input.strip().lower() == "quit":
        return "quit"
    
    # Try convert to integer
    try:
        quantity = int(user_input.strip())
        
        #  YOUR "LIMIT" CHECK — reject negative numbers
        if quantity < 0:
            print(" Invalid! Quantity cannot be negative.")
            return None
            
        return quantity
        
    except ValueError:
        print(" Invalid! Please enter a whole number only.")
        return None


# --------------------------
# Function 2: Update Running Total
# --------------------------
def process_delivery(current_total, new_value):
    """Add new_value to current_total and return the updated total."""
    new_total = current_total + new_value
    return new_total


# --------------------------
# Function 3: Calculate Tax (10%)
# --------------------------
def calculate_tax(amount):
    """Take delivery amount, return 10% tax value."""
    tax = amount * 0.10
    return tax


# --------------------------
# Function 4: Print Final Report
# --------------------------
def generate_report(total_deliveries, failed_attempts):
    """Display final summary when user quits."""
    print("\n" + "=" * 40)
    print("INVENTORY AUDIT REPORT")
    print("=" * 40)
    print(f" Total Deliveries Processed: {total_deliveries}")
    print(f" Failed/Rejected Entries:   {failed_attempts}")
    print("=" * 40)
    print("Done! Thank you.\n")


# --------------------------
# Main Program — Ties Everything Together
# --------------------------
def main():
    # Initialize counters — ALL start at 0
    inventory_total = 0
    delivery_count = 0
    failed_count = 0

    # Welcome message
    print("=" * 40)
    print(" MODULAR INVENTORY AUDITOR")
    print("Enter stock numbers one at a time (0 or higher).")
    print("Type 'quit' at any time to stop and see report.")
    print("=" * 40 + "\n")

    # Main loop — keeps running until "quit"
    while True:
        result = get_valid_input()

        # Case A: User wants to exit
        if result == "quit":
            print("\nGenerating report...")
            break

        # Case B: Input was bad (non-number OR negative)
        if result is None:
            failed_count = failed_count + 1
            continue

        # Case C: Good input — process it
        delivery_count = delivery_count + 1
        inventory_total = process_delivery(inventory_total, result)
        tax_amount = calculate_tax(result)
        
        print(f" Accepted | Units: {result} | Tax: ${tax_amount:.2f} | Running Total: {inventory_total}")

    # Show final report
    generate_report(delivery_count, failed_count)


# Run the program
if __name__ == "__main__":
    main()


