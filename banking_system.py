import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from decimal import Decimal
import mysql.connector
from mysql.connector import Error

def run():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'vishrutcoderpro',
        'database': 'banking_system'
    }


    def create_connection():
        connection = None
        try:
            connection = mysql.connector.connect(**db_config)
            return connection
        except Error as e:
            messagebox.showerror("Connection Error", f"The error '{e}' occurred")
            return None


    def generate_account_number():
        while True:
            acc_num = random.randint(1000000000, 9999999999)
            if not check_account_exists(acc_num):
                return acc_num


    def check_account_exists(account_number):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            exists = cursor.fetchone()[0] > 0
            cursor.close()
            connection.close()
            return exists
        return True


    def create_account(name, initial_balance):
        account_number = generate_account_number()

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO accounts (account_number, name, balance) VALUES (%s, %s, %s)"
            cursor.execute(query, (account_number, name, initial_balance))
            connection.commit()
            cursor.close()
            connection.close()
            return account_number
        return None


    def delete_account(account_number):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            connection.commit()
            deleted_count = cursor.rowcount
            cursor.close()
            connection.close()
            return deleted_count > 0
        return False

    def deposit(account_number, amount):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT balance FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result:
                new_balance = result[0] + Decimal(amount)
                update_query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
                cursor.execute(update_query, (new_balance, account_number))
                connection.commit()
                cursor.close()
                connection.close()
                return new_balance
        return None

    def withdraw(account_number, amount):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT balance FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result and amount <= result[0]:
                new_balance = result[0] - Decimal(amount)
                update_query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
                cursor.execute(update_query, (new_balance, account_number))
                connection.commit()
                cursor.close()
                connection.close()
                return new_balance
        return None

    def display_accounts():
        connection = create_connection()
        accounts_list = []
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT account_number, name, balance FROM accounts")
            accounts_list = cursor.fetchall()
            cursor.close()
            connection.close()
        return accounts_list


    def is_field_empty(*fields):
        for field in fields:
            if not field.strip():
                return True
        return False


    def create_account_window():

        def submit():
            name = name_entry.get()
            initial_balance = balance_entry.get()

            if is_field_empty(name, initial_balance):
                messagebox.showerror("Input Error", "All fields are compulsory. Please fill them out.")
                return

            try:
                initial_balance = float(initial_balance)
                if initial_balance < 0:
                    messagebox.showerror("Input Error", "Initial balance must be positive.")
                    return
                account_number = create_account(name, initial_balance)
                if account_number:
                    messagebox.showinfo("Success", f"Account created! Your account number is {account_number}")
                    create_window.destroy()
                else:
                    messagebox.showerror("Error", "Failed to create account.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid amount for initial balance.")

        create_window = tk.Toplevel()
        create_window.title("Create Account")
        create_window.config(bg="#add8e6")

        tk.Label(create_window, text="Create New Account", bg="#add8e6", font=('Arial', 16, 'bold')).grid(row=0, column=0,columnspan=2,padx=10, pady=10)
        tk.Label(create_window, text="Name:", bg="#add8e6", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(create_window, text="Initial Balance:", bg="#add8e6", font=('Arial', 12)).grid(row=2, column=0, padx=10,pady=10)

        name_entry = tk.Entry(create_window, font=('Arial', 12))
        balance_entry = tk.Entry(create_window, font=('Arial', 12))

        name_entry.grid(row=1, column=1, padx=10, pady=10)
        balance_entry.grid(row=2, column=1, padx=10, pady=10)

        submit_button = tk.Button(create_window, text="Create", command=submit, bg="#5cb85c", fg="white",font=('Arial', 12, 'bold'))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        create_window.bind('<Return>', lambda event: submit())


    def delete_account_window():

        def submit():
            account_number = account_entry.get()

            if is_field_empty(account_number):
                messagebox.showerror("Input Error", "All fields are compulsory. Please fill them out.")
                return

            try:
                account_number = int(account_number)
                if delete_account(account_number):
                    messagebox.showinfo("Success", f"Account {account_number} deleted successfully.")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Account not found!")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid account number.")

        delete_window = tk.Toplevel()
        delete_window.title("Delete Account")
        delete_window.config(bg="#add8e6")

        tk.Label(delete_window, text="Delete Account", bg="#add8e6", font=('Arial', 16, 'bold')).grid(row=0, column=0,columnspan=2, padx=10,pady=10)
        tk.Label(delete_window, text="Account Number:", bg="#add8e6", font=('Arial', 12)).grid(row=1, column=0, padx=10,pady=10)

        account_entry = tk.Entry(delete_window, font=('Arial', 12))
        account_entry.grid(row=1, column=1, padx=10, pady=10)

        submit_button = tk.Button(delete_window, text="Delete", command=submit, bg="#d9534f", fg="white",font=('Arial', 12, 'bold'))
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        delete_window.bind('<Return>', lambda event: submit())


    def deposit_window():

        def submit():
            account_number = account_entry.get()
            amount = amount_entry.get()

            if is_field_empty(account_number, amount):
                messagebox.showerror("Input Error", "All fields are compulsory. Please fill them out.")
                return

            try:
                account_number = int(account_number)
                amount = float(amount)
                new_balance = deposit(account_number, amount)
                if new_balance is not None:
                    messagebox.showinfo("Success", f"Deposited {amount:.2f}. New balance: {new_balance:.2f}")
                    deposit_win.destroy()
                else:
                    messagebox.showerror("Error", "Account not found or invalid amount.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid amounts.")

        deposit_win = tk.Toplevel()
        deposit_win.title("Deposit")
        deposit_win.config(bg="#add8e6")

        tk.Label(deposit_win, text="Deposit Money", bg="#add8e6", font=('Arial', 16, 'bold')).grid(row=0, column=0,columnspan=2, padx=10,pady=10)
        tk.Label(deposit_win, text="Account Number:", bg="#add8e6", font=('Arial', 12)).grid(row=1, column=0, padx=10,pady=10)
        tk.Label(deposit_win, text="Amount:", bg="#add8e6", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10)

        account_entry = tk.Entry(deposit_win, font=('Arial', 12))
        amount_entry = tk.Entry(deposit_win, font=('Arial', 12))

        account_entry.grid(row=1, column=1, padx=10, pady=10)
        amount_entry.grid(row=2, column=1, padx=10, pady=10)

        submit_button = tk.Button(deposit_win, text="Deposit", command=submit, bg="#5cb85c", fg="white",font=('Arial', 12, 'bold'))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        deposit_win.bind('<Return>', lambda event: submit())


    def withdraw_window():
        def submit():
            account_number = account_entry.get()
            amount = amount_entry.get()

            if is_field_empty(account_number, amount):
                messagebox.showerror("Input Error", "All fields are compulsory. Please fill them out.")
                return

            try:
                account_number = int(account_number)
                amount = float(amount)
                new_balance = withdraw(account_number, amount)
                if new_balance is not None:
                    messagebox.showinfo("Success", f"Withdrew {amount:.2f}. New balance: {new_balance:.2f}")
                    withdraw_win.destroy()
                else:
                    messagebox.showerror("Error", "Account not found or insufficient balance.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid amounts.")

        withdraw_win = tk.Toplevel()
        withdraw_win.title("Withdraw")
        withdraw_win.config(bg="#add8e6")  # Light Blue Background

        tk.Label(withdraw_win, text="Withdraw Money", bg="#add8e6", font=('Arial', 16, 'bold')).grid(row=0, column=0,columnspan=2, padx=10,pady=10)
        tk.Label(withdraw_win, text="Account Number:", bg="#add8e6", font=('Arial', 12)).grid(row=1, column=0, padx=10,pady=10)
        tk.Label(withdraw_win, text="Amount:", bg="#add8e6", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10)

        account_entry = tk.Entry(withdraw_win, font=('Arial', 12))
        amount_entry = tk.Entry(withdraw_win, font=('Arial', 12))

        account_entry.grid(row=1, column=1, padx=10, pady=10)
        amount_entry.grid(row=2, column=1, padx=10, pady=10)

        submit_button = tk.Button(withdraw_win, text="Withdraw", command=submit, bg="#d9534f", fg="white",font=('Arial', 12, 'bold'))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        withdraw_win.bind('<Return>', lambda event: submit())


    def display_accounts_window():
        accounts = display_accounts()
        display_win = tk.Toplevel()
        display_win.title("Display Accounts")
        display_win.config(bg="#add8e6")

        tk.Label(display_win, text="All Accounts", bg="#add8e6", font=('Arial', 16, 'bold')).pack(pady=10)

        tree = ttk.Treeview(display_win, columns=("Account Number", "Name", "Balance"), show="headings", height=10)
        tree.heading("Account Number", text="Account Number")
        tree.heading("Name", text="Name")
        tree.heading("Balance", text="Balance")
        tree.column("Account Number", width=150)
        tree.column("Name", width=200)
        tree.column("Balance", width=100)

        tree.pack(pady=20)

        for acc in accounts:
            tree.insert("", tk.END, values=acc)

        close_button = tk.Button(display_win, text="Close", command=display_win.destroy, bg="#5bc0de", fg="white",font=('Arial', 12, 'bold'))
        close_button.pack(pady=10)


    app = tk.Tk()
    app.title("Simple Banking System")
    app.geometry("400x400")
    app.config(bg="#add8e6")

    # Main menu
    tk.Label(app, text="Banking System", bg="#add8e6", font=('Arial', 24, 'bold')).pack(pady=20)
    tk.Button(app, text="Create Account", command=create_account_window, bg="#5cb85c", fg="white",font=('Arial', 12, 'bold')).pack(pady=10, fill='x', padx=20)
    tk.Button(app, text="Delete Account", command=delete_account_window, bg="#d9534f", fg="white",font=('Arial', 12, 'bold')).pack(pady=10, fill='x', padx=20)
    tk.Button(app, text="Deposit", command=deposit_window, bg="#5bc0de", fg="white", font=('Arial', 12, 'bold')).pack(pady=10, fill='x', padx=20)
    tk.Button(app, text="Withdraw", command=withdraw_window, bg="#5bc0de", fg="white", font=('Arial', 12, 'bold')).pack(pady=10, fill='x', padx=20)
    tk.Button(app, text="Display Accounts", command=display_accounts_window, bg="#5bc0de", fg="white",font=('Arial', 12, 'bold')).pack(pady=10, fill='x', padx=20)

    app.mainloop()


if __name__ == "__main__":
    run()