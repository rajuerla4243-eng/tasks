import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

class ReportGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Automated Report Generator")
        self.root.geometry("400x300")

        # Title
        self.title_label = tk.Label(root, text="Test Report Generator", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Input Fields
        self.test_case_label = tk.Label(root, text="Test Case")
        self.test_case_label.pack()

        self.test_case_entry = tk.Entry(root, width=30)
        self.test_case_entry.pack(pady=5)

        self.status_label = tk.Label(root, text="Status (Pass/Fail)")
        self.status_label.pack()

        self.status_entry = tk.Entry(root, width=30)
        self.status_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Test Case", command=self.add_data)
        self.add_button.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Report", command=self.generate_report)
        self.generate_button.pack(pady=10)

        # Data storage
        self.data = [["Test Case", "Status"]]

    def add_data(self):
        test_case = self.test_case_entry.get()
        status = self.status_entry.get()

        if test_case and status:
            self.data.append([test_case, status])
            messagebox.showinfo("Success", "Test case added!")

            # Clear fields
            self.test_case_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter all fields")

    def generate_report(self):
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Test Report"

            for row in self.data:
                ws.append(row)

            wb.save("Test_Report.xlsx")
            messagebox.showinfo("Success", "Report Generated Successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ReportGeneratorApp(root)
    root.mainloop()