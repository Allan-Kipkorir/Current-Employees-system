import csv
import os

class Employee:
    # empty dictionary(to store Employee data in memory before saving them in our csv file)
    db = {}
    def __init__(self,name,age,position,salary, department, location):
        #private instance attributes
        self.__name = str(name)
        self.__age = str(age)
        self.__position = str(position)
        self.__salary = str(salary)
        #public instance attributes
        self.department = str(department)
        self.location = str(location)

    # Loading data from csv file.
    @staticmethod
    def load_csv(filename = "Current_Employees.csv"):
        if not os.path.exists(filename):
            return # Current_Employees.csv file doesn't exist

        with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["Name"]
                    Employee.db[name] = Employee(
                        row["Name"],
                        row["Age"],
                        row["Position"],
                        row["Salary"],
                        row["Department"],
                        row["Location"]
                    )
    # Saving data to csv
    @staticmethod
    def save_to_csv(filename="Current_Employees.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Name", "Age", "Position", "Salary", "Department", "Location"])
            # Write each employee's data
            for emp in Employee.db.values():
                writer.writerow([
                    emp._Employee__name,
                    emp._Employee__age,
                    emp._Employee__position,
                    emp._Employee__salary,
                    emp.department,
                    emp.location
                ])
    #validate input
    @staticmethod
    def validate_input(prompt):
        while True:
            value = input(prompt).strip()
            if len(value) == 0:
                print("Invalid input. Try again")
            elif value.isdigit() == True:
                print("Invalid input. Try again")
            else:
                return value
    #validate name
    @staticmethod
    def validate_name(prompt):
        while True:
            value = input(prompt).strip()
            if len(value) == 0:
                print("Invalid input. Try again")
            elif value.isdigit() == True:
                print("Invalid input. Try again")
            elif value.lower() in Employee.db:
                print("User already exists. Try again")
            else:
                return value
    #Validate age as an integer
    @staticmethod
    def validate_int(prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit() == False:
                print("Invalid input. Try again")
            elif int(value) < 0:
                print("Invalid input. Try again")
            elif len(value) !=0:
                return value
    #Validate salary as float
    @staticmethod
    def validate_float(prompt):
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print("Invalid input. Try again")
    # Add employees
    @staticmethod
    def add_employee():
        # get info from user
        name = Employee.validate_name("Enter your name: ").lower()
        age = Employee.validate_int("Enter your age: ")
        position = Employee.validate_input("Enter your position: ").lower()
        salary = Employee.validate_float("Enter your salary: ")
        department = Employee.validate_input("Enter your department: ").lower()
        location = Employee.validate_input("Enter your location: ").lower()
        # create instance of Employee
        Employee.db[name]=Employee(name,age,position,salary,department,location,)


    #__str__ function to display employee details
    def __str__(self):
        return (f"Employee Name: {self.__name.capitalize()}, "
            f"Age: {self.__age}, "
            f"Position: {self.__position.capitalize()}, "
            f"Salary: {self.__salary}, "
            f"Department: {self.department.capitalize()}, "
            f"Location: {self.location.capitalize()}")

    #View all Employees
    @staticmethod
    def view_all_employees():
        if not Employee.db:
            print("No Employees Available")
        else:
            print("All Employees")
            for emp in Employee.db.values():
                print(emp)
                print("-"*50)
    #Update employee details
    @staticmethod
    def update_employee_details():
        name = input("Enter the name of the employee you want to update: ")
        if name in Employee.db:
            age = input("Enter the age of the employee you want to update: ")
            position = input("Enter the position of the employee you want to update: ").lower()
            salary = input("Enter the salary of the employee you want to update: ")
            department = input("Enter the department of the employee you want to update: ").lower()
            location = input("Enter the location of the employee you want to update: ").lower()

            Employee.db[name] = Employee(name,age,position,salary,department,location,)

            print("Employee Details Updated")
        else:
            print("Employee Not Found")
    #delete employees
    @staticmethod
    def delete_employee_details():
        name = input("Enter the name of the employee you want to delete: ")
        if name in Employee.db:
            del Employee.db[name]
        else:
            print("Employee Not Found")
    #search for employees
    @staticmethod
    def search_employee_details():
        name = input("Enter the name of the employee you want to search: ")
        if name in Employee.db:
            print(Employee.db[name])
        else:
            print("Employee Not Found")

    #sorting employee details
    @staticmethod
    def sort_employee_details():
        for key in sorted(Employee.db):
            print(key, Employee.db[key])



    @staticmethod
    def main():
        Employee.load_csv()
        print(Employee.db)
        main_menu = [
            "Main Menu Options",
            "1. Add New Employee",
            "2. View All Employees",
            "3. Update Employee",
            "4. Delete Employee",
            "5. Search Employees",
            "6. Sort Employees",
            "7. Exit"
        ]


        while True:
            for options in main_menu:
                print(options)
            #validating choice input
            choice = Employee.validate_int("Enter your choice: ")
            if int(choice) == 1:
                Employee.add_employee()
            elif int(choice) == 2:
                Employee.view_all_employees()
            elif int(choice) == 3:
                Employee.update_employee_details()
            elif int(choice) == 4:
                Employee.delete_employee_details()
            elif int(choice) == 5:
                Employee.search_employee_details()
            elif int(choice) == 6:
                Employee.sort_employee_details()
            elif int(choice) == 7:
                print("...Saving Files...")
                Employee.save_to_csv()
                break
            else:
                print("Invalid Choice. Try again")



Employee.main()



