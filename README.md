**Employee Management System**

A **Python-based** Employee Management System using Object-Oriented Programming (OOP) and CSV file storage. This system allows you to **add, view, update, delete, search, sort, and save employee records** via a **simple menu interface.**

**Features**

Add new employees with validated inputs

View all employees in a formatted display

Update employee details

Delete employee records

Search employees by name

Sort employees alphabetically

Save and load employee data using CSV

**Prerequisites**


Python 3.x installed on your system

Basic understanding of running Python scripts

Installation

Clone or download this repository or save the Employee class code to a .py file, e.g., employee_system.py.

Ensure the same directory has a CSV file named Current_Employees.csv for persistent storage. If it doesn’t exist, the system will create one automatically.

**Usage**


Open a terminal or command prompt.

Navigate to the directory containing employee_system.py.

**Run the program:**


python employee_system.py


**Follow the on-screen menu options:**


1. Add New Employee
2. View All Employees
3. Update Employee
4. Delete Employee
5. Search Employees
6. Sort Employees
7. Exit


**Enter the number corresponding to the action you want to perform.**


**Upon exiting, the system will automatically save all employee data to Current_Employees.csv.**


**Notes**


Employee **names** must be unique; the system will prompt if a duplicate is entered.

Input validation ensures that **names, positions, and departments are text**, while age and salary are numeric.

The system uses private attributes for sensitive data (name, age, position, salary) and public attributes for department and location.
