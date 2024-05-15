from typing import List
from datetime import time


class ClinicPatient:
    def __init__(self, CHI: str, appt_time: time, first_name, last_name):
        self._CHI = CHI
        self.appt_time = appt_time
        self._summary = "None Found"
        self._last_seen = None
        self._first_name = first_name
        self._last_name = last_name
        #print(f"Created patient record with {self.CHI}, {self.appt_time}, {self.first_name}, {self.last_name}")

    # Getter and setter for _CHI
    @property
    def CHI(self):
        return self._CHI

    @CHI.setter
    def CHI(self, CHI):
        if len(CHI) < 10:
            CHI = "0" + CHI
        self._CHI = CHI

    # Getter and setter for _appt_time
    @property
    def appt_time(self):
        return self._appt_time

    @appt_time.setter
    def appt_time(self, appt_time):
      if isinstance(appt_time, str) and len(appt_time) > 5:
        appt_time = appt_time[:5]
      self._appt_time = appt_time

    # Getter and setter for _summary
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, summary):
        # Remove included previous clinic time
        while ":" in summary:
            colon_index = summary.index(":")
            removal_start = max(0, colon_index - 2)
            removal_end = min(len(summary), colon_index + 3)
            # check characters are numbers
            if summary[removal_start:removal_end].replace(":", "").isdigit():
                summary = summary[:removal_start] + summary[removal_end:]
        # Remove patient's first name, last name, and CHI if they are present
        summary = summary.replace(self.first_name, '')
        summary = summary.replace(self.last_name, '')
        summary = summary.replace(self.CHI, '')
        
        self._summary = summary

    # Getter and setter for _last_seen
    @property
    def last_seen(self):
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        self._last_seen = f"Last seen : {last_seen}"
        
    def title_output(self):
        #to_document = f"{self.appt_time} {self.CHI} {self._first_name} {self._last_name}\n{self.summary} \n{self.last_seen}"
        to_document = f"{self.appt_time} {self.CHI} {self.first_name} {self.last_name}"
        return to_document
    
    # Getter and setter for _first_name
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    # Getter and setter for _last_name
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

if __name__ == "__main__":
    print("Testing Class :")

    clinic = ClinicPatient("123456789", "15:30:00", "sam", "mcinerney")
    clinic.summary = (
        "This is a summary. With a Time in 12:30 that I'm hoping gets removed."
    )
    clinic.last_seen = "2024-04-12"

    print(clinic.title_output())
    print(clinic.summary)
