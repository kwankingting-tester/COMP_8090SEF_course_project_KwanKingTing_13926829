import customtkinter as ctk
from core.manager import AccountManager

class FinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__() 
        
        self.manager = AccountManager()
        self.title("HKMU Personal Finance Tracker")
        self.geometry("800x500")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="Finance Tracker", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)

        self.balance_label = ctk.CTkLabel(self.sidebar, text=f"Balance: ${self.manager.get_total_balance()}")
        self.balance_label.pack(pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.add_btn = ctk.CTkButton(self.main_frame, text="Add Transaction", command=self.add_entry)
        self.add_btn.pack(pady=10)

    def add_entry(self):
        print("Adding new transaction...")

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()