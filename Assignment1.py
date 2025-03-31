# Create a simplifued EMS 
employees = {
    101: {'name': "Satya", "age": 27, "Department": "HR", "Salary": 500000},
    102:   {'name': "Veeba", "age": 30, "Department": "IT", "Salary": 600000},
    103:  {'name': "Prerna", "age": 25, "Department": "Finance", "Salary": 300000},
    104:  {'name': "Rohan", "age": 31, "Department": "Marketting", "Salary": 550000},
    105:  {'name': "Esha", "age": 32, "Department": "Operations", "Salary": 650000}
}
#Adding employees
def add_employee():
    """Adding new employee"""
    emp_id = int(input("Enter the employee ID"))
    if emp_id in employees:
        print("Input already exists try again")
        return
    name = input("Enter your name")
    age = input("Enter your age")
    Department = input("Enter your department")
    Salary = float(input("Enter your salary"))
    employees[emp_id] = {'name': name, "age": age, "Department ": Department, "Salary": Salary}
    print("Details added successfully")
    print("***************************************************************************")

# Vewing Employees
def view_employee():
    """Function to display all employees."""
    if not employees:
        print("No employees found.\n")
        return
    print("\nEmployee List:")
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['Department']}, Salary: {details['Salary']}")
    print()

#Search a employeee
def search_employee():
    """Function to search for an employee by ID."""
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found:\nID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}\n")
    else:
        print("Employee not found!\n")

#Main function    
def main():
    """The Main menu"""
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View All Employee")
        print("3. Search an employee")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice== 1:
            add_employee()
        elif choice == 2:
            view_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Exiting the program. ThankYou")
            break
        else: 
            print("Invalid Input!")
        
main()