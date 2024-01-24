class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_employees(self, key):
        if key == 1:  # Sort by Age
            self.employees.sort(key=lambda emp: emp.age)
        elif key == 2:  # Sort by Name
            self.employees.sort(key=lambda emp: emp.name)
        elif key == 3:  # Sort by Salary
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")

    def display_employees(self):
        for emp in self.employees:
            print(emp)


if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    sorting_option = int(input("Choose the sorting parameter (1. Age, 2. Name, 3. Salary): "))
    employee_table.sort_employees(sorting_option)

    print("\nSorted Employee Data:")
    employee_table.display_employees()
