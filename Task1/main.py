import sys
import os
from core.manager import FinanceManager

#因為pack左落不同file,所以需要定位番path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

#目錄和call function用
def main():
    app = FinanceManager()
    app.load_data()

    while True:
        print("\n" + "="*50)
        print("     Personal Finance Tracker System")
        print("="*50)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            amount = float(input("Amount: "))
            cat = input("Category (e.g. Salary, Investment): ")
            app.add_transaction("Cash Wallet", amount, cat, True)
            print("Income recorded!")
        elif choice == "2":
            amount = float(input("Amount: "))
            cat = input("Category (e.g. Food, Transport): ")
            app.add_transaction("Cash Wallet", amount, cat, False)
            print("Expense recorded!")
        elif choice == "3":
            app.show_summary()
        elif choice == "4":
            print("Thanks for using! Data saved.")
            break
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    main()
