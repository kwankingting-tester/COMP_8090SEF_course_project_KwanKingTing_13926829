import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
#Task 2 目錄和call function用
if project_root not in sys.path:
    sys.path.insert(0, project_root)

task1_path = os.path.join(project_root, "Task1")
if task1_path not in sys.path:
    sys.path.insert(0, task1_path)

try:
    from core.manager import FinanceManager
except ImportError:
    try:
        # 拿Task1的data黎用
        from Task1.core.manager import FinanceManager
    except ImportError:
        print("Error: Cannot find 'core.manager'.")
        print(f"Current sys.path: {sys.path}")
        sys.exit(1)

def main():
    app = FinanceManager()
    
    app.load_data()

    while True:
        print("\n" + "="*55)
        print("     Personal Finance Tracker System (Task 2 Edition)")
        print("     [Integrated with Binary Heap & Heap Sort]")
        print("="*55)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. [Task 2] Top 5 Highest Expenses (Real-time Heap)")
        print("5. [Task 2] Sorted Expense Report (Heap Sort)")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                cat = input("Category (e.g. Salary, Investment): ")
                app.add_transaction("Cash Wallet", amount, cat, True)
                print("Income recorded!")
            except ValueError:
                print("Invalid input. Please enter a number for amount.")
                
        elif choice == "2":
            try:
                amount = float(input("Amount: "))
                cat = input("Category (e.g. Food, Transport): ")
                app.add_transaction("Cash Wallet", amount, cat, False)
                print("Expense recorded!")
            except ValueError:
                print("Invalid input. Please enter a number for amount.")
                
        elif choice == "3":
            app.show_summary()
            
        elif choice == "4":
            if hasattr(app, 'show_top_5_expenses'):
                app.show_top_5_expenses()
            else:
                print("Method 'show_top_5_expenses' not found in manager.py")
            
        elif choice == "5":
            if hasattr(app, 'show_sorted_expenses'):
                app.show_sorted_expenses()
            else:
                print("Method 'show_sorted_expenses' not found in manager.py")
            
        elif choice == "6":
            print("Saving data and exiting. See you next time!")
            break
        else:
            print("Invalid selection, please enter 1-6.")

if __name__ == "__main__":
    main()