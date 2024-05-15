import tkinter as tk
from tkinter import ttk
import program_logic
import datetime
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os

def next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    next_monday_date = today + datetime.timedelta(days=days_until_monday)
    return next_monday_date.strftime("%d%m%y")


class CPApp:
    def __init__(self, root):
        self.root = root
        self.next_monday_var = tk.StringVar(value="Clinic " + next_monday())
        self.inputExcelFile = ""
        
        # GUI SETTINGS
        root.geometry("300x200")
        root.title("Clinic Prepper")

        # Style
        style = ttk.Style()
        style.theme_use("clam")

        # Create the "Browse" button
        browse_button = ttk.Button(
            root,
            text="Select Excel file containing Time and CHI List",
            command=self.get_excel_file,
        )
        browse_button.pack(padx=10, pady=10)

        # Input filename
        label = ttk.Label(root, text="Enter file name for output:")
        label.pack()

        self.entry = ttk.Entry(root)  # Use the StringVar
        clinic_name = f"GN Clinic {next_monday()}" 
        self.entry.insert(0, clinic_name)
        self.entry.pack()
        # textvariable=self.next_monday_var

        # Run Program
        run_button = ttk.Button(root, text="Run", command=self.run_prepper)
        run_button.pack(padx=10, pady=10)

        # Exit Program
        exit_button = ttk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(padx=10, pady=10)

    def get_excel_file(self):
        filetypes = [("Excel files", "*.xls")]
        filepathforinfo = filedialog.askopenfilename(
            title="Open an Excel file", initialdir=os.getcwd(), filetypes=filetypes
        )
        print("Selected file path:", filepathforinfo)
        #self.entry.delete(0, "end")
   
        # Import clinic list from Excel sheet
        self.inputExcelFile = filepathforinfo
        print(filepathforinfo)
        return self.inputExcelFile

    def run_prepper(self):
        output_filename= self.entry.get()

        #check for excel file
        if not self.inputExcelFile:
            messagebox.showerror("Error", "No input Excel file selected")
            return
        
        #check filename
        if not output_filename.endswith('.docx'):
          output_filename += '.docx'
        print(f"Running program with {self.inputExcelFile, output_filename}")
        result = program_logic.clinic_prepper(self.inputExcelFile,output_filename )
        messagebox.showinfo("Complete",f" Created file : {output_filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CPApp(root)
    root.mainloop()
