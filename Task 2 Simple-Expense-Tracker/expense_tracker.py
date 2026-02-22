"""
Simple Expense Tracker
----------------------
A beginner-friendly Python program to track multiple expenses.

Features:
- Add multiple expense amounts
- Uses accumulator logic
- Displays total spent
- Displays number of expenses
- Input validation
- Error handling
"""

def expense_tracker():
    print("=" * 40)
    print("        SIMPLE EXPENSE TRACKER")
    print("=" * 40)

    total = 0.0          # Accumulator variable
    count = 0            # Number of expenses

    while True:
        user_input = input("\nEnter expense amount (or type 'q' to quit): ").strip()

        # Exit condition
        if user_input.lower() == 'q':
            break

        try:
            amount = float(user_input)

            # Validate negative values
            if amount < 0:
                print("⚠️  Expense cannot be negative. Please enter a valid amount.")
                continue

            # Accumulator logic
            total = total + amount
            count += 1

            print(f"✅ Expense added successfully!")

        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

    # Final Summary
    print("\n" + "=" * 40)
    print("              SUMMARY")
    print("=" * 40)
    print(f"Total Expenses Entered : {count}")
    print(f"Total Amount Spent     : ₹ {total:.2f}")
    print("=" * 40)
    print("Thank you for using Simple Expense Tracker!")


# Run the program
if __name__ == "__main__":
    expense_tracker()