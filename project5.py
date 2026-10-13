class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person created with name: {self.name} and age: {self.age}.")


class Employee(Person):
    def __init__(self, name="", age=0, employee_id="", salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = float(salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    def display(self):
        print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.__employee_id}, and salary: ${self.__salary}.")

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name="", age=0, employee_id="", salary=0.0, department=""):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print(f"Manager created with name: {self.name}, age: {self.age}, ID: {self.get_employee_id()}, salary: ${self.get_salary()}, and department: {self.department}.")


def main():
    persons = []
    employees = []
    managers = []

    while True:
        print("--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            p = Person(name, age)
            persons.append(p)
            p.display()

        elif choice == '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(name, age, emp_id, salary)
            employees.append(emp)
            emp.display()

        elif choice == '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            mgr = Manager(name, age, emp_id, salary, dept)
            managers.append(mgr)
            mgr.display()

        elif choice == '4':
            print("Choose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                for p in persons:
                    p.display()
            elif sub_choice == '2':
                for emp in employees:
                    print("Employee Details:")
                    print(f"Name: {emp.name}")
                    print(f"Age: {emp.age}")
                    print(f"Employee ID: {emp.get_employee_id()}")
                    print(f"Salary: ${emp.get_salary()}")
            elif sub_choice == '3':
                for mgr in managers:
                    mgr.display()

        elif choice == '5':
            print("Exiting the system. All resources have been freed.")
            break

        print("--- Choose another operation ---")


if __name__ == "__main__":
    main()