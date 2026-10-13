# Employee Management System

## Project Description

The Employee Management System is a simple Python project based on Object-Oriented Programming (OOP). It allows users to create and manage details of persons, employees, and managers using a menu-driven program.

## Features

- Create a Person with name and age.
- Create an Employee with name, age, employee ID, and salary.
- Create a Manager with name, age, employee ID, salary, and department.
- Display details of persons, employees, and managers.
- Use a menu-driven interface to perform different operations.
- Exit the program when finished.

## OOP Concepts Used

- **Class and Object:** Used to create Person, Employee, and Manager objects.
- **Inheritance:** Employee inherits from Person, and Manager inherits from Employee.
- **Encapsulation:** Employee ID and salary are stored as private attributes.
- **Getter and Setter:** Used to access and update employee ID and salary.
- **Method Overriding:** The `display()` method is defined in each class.
- **Constructor:** The `__init__()` method initializes object attributes.
- **Super Function:** Used to call the parent class constructor.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

## How to Run the Project

1. Install Python 3 on your computer.
2. Save the code in a file named `employee_management.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the following command:

```bash
python employee_management.py
```

## Menu Options

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

## Example Output

```text
--- Python OOP Project: Employee Management System ---
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2
Enter Name: Rahul
Enter Age: 25
Enter Employee ID: E101
Enter Salary: 30000

Employee created with name: Rahul, age: 25, ID: E101, and salary: $30000.0.
```

## Project Structure

```text
Employee-Management-System/
│
├── employee_management.py
└── README.md
```

## Future Improvements

- Add input validation for age and salary.
- Add options to update or delete employee records.
- Store employee details in a file or database.
- Add a search feature using employee ID.

## Conclusion

This project demonstrates basic Python OOP concepts through a simple employee management system. It is suitable for beginners who want to practice classes, inheritance, encapsulation, constructors, and method overriding.
