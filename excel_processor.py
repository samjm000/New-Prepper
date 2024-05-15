# chi_finder
import os
import pandas as pd  # Excel file handler
from datetime import datetime
from collections import OrderedDict

# function to return a dicitonary of times and chi numbers from excel sheet
def get_chi_numbers(excelFile):
    print(f"Running Excel import from {excelFile}")
    clinic_file = pd.ExcelFile(excelFile)

       # Read in sheet 1 CHI numbers and time
    clinic_sheet = clinic_file.parse("Sheet1", converters={"Time": str, "CHI": str})

    # Normalize the column names to lowercase
    clinic_sheet.columns = [col.strip().lower() for col in clinic_sheet.columns]

    # Drop the rows where 'CHI' is NaN
    clinic_sheet = clinic_sheet.dropna(subset=["chi"])

    # save data from sheet as series
    appt_time = clinic_sheet["time"]
    chi_number = clinic_sheet["chi"]
    first_name = clinic_sheet["fname"]
    last_name = clinic_sheet["lname"]

    # remove '(b)' from time string
    appt_time = appt_time.str.replace("(b)", ":00", case=False)

    # Combine the data into a dictionary with CHI as the key
    combined_data = {
        chi: {"time": time, "fname": fname, "lname": lname}
        for chi, time, fname, lname in zip(chi_number, appt_time, first_name, last_name)
    }

    #Test print to ensure data is captured correctly
    print(combined_data)

    return combined_data

# test the program
if __name__ == "__main__":

    print("Testing Excel processing")
    get_chi_numbers(r"clinic lists\GN Clinic 200524.xls")
