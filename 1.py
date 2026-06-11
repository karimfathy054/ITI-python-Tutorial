import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)

cursor = connection.cursor()

class Employee:
    all_employees = []
    def __init__(self,first_name,last_name,age,department,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.all_employees.append(self)
        cursor.execute("insert into employee (first_name,last_name,age,department,salary) values (%s,%s,%s,%s,%s)",(self.first_name,self.last_name,self.age,self.department,self.salary))
        connection.commit()
        self.id = cursor.lastrowid
        print("Employee added successfully")
        
        
    def transfer(self,new_department):
        self.department = new_department
        cursor.execute("update employee set department = %s where id = %s",(new_department,self.id))
        connection.commit()
        
    def fire(self):
        Employee.all_employees.remove(self)
        cursor.execute("delete from employee where id = %s",(self.id,))
        connection.commit()

    def show(self):
        print(f"ID: {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        
    @classmethod
    def List_employees(cls):
        for emp in cls.all_employees:
            emp.show()
            
    @staticmethod
    def addEmployee():
        fname = input("First Name:>> ")
        lname = input("Last Name:>> ")
        age = input("Age:>> ")
        department = input("Department:>> ")
        salary = input("Salary:>> ")
        Employee(fname,lname,age,department,salary)
    
    @classmethod
    def getEmployeeByID(cls,id):
        emp = list(filter(lambda emp: emp.id == id,cls.all_employees))
        if len(emp) == 0:
            return None
        return emp[0]
        

            

class Manager(Employee):
    def __init__(self,first_name,last_name,age,department,salary,managed_department):
        super().__init__(first_name,last_name,age,department,salary)
        self.managed_department = managed_department
        cursor.execute("update employee set managed_department = %s where id = %s",(self.managed_department,self.id))
        connection.commit()
        
    def show(self):
        print(f"ID: {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Managed Department: {self.managed_department}")
        print(f"salary: confidential")
        
    @staticmethod
    def addManager():
        fname = input("First Name:>> ")
        lname = input("Last Name:>> ")
        age = input("Age:>> ")
        department = input("Department:>> ")
        salary = input("Salary:>> ")
        managed_department = input("Managed Department:>> ")
        Manager(fname,lname,age,department,salary,managed_department)



while(True):
    print("""
available opeartions and (keywords)
-> Add employee (add)
-> fire employee (fire)
-> transfer employee (transfer)
-> get employee by ID (get)
-> list all employees (list)
-> exit (q)
""")
    choice = input().lower()
    if choice == "add":
        choice = input("""
(e) to add employee
(m) to add manager""").lower()
        if choice == "e":
            Employee.addEmployee()
        elif choice == "m":
            Manager.addManager()
        else:
            print("invalid choice")
    elif choice == "fire":
        id = int(input("Enter employee ID to fire: "))
        emp = Employee.getEmployeeByID(id)
        if emp:
            emp.fire()
            print("Employee fired successfully")
        else:
            print("Employee not found")
    elif choice == "transfer":
        id = int(input("Enter employee ID to transfer: "))
        emp = Employee.getEmployeeByID(id)
        if emp:
            new_department = input("Enter new department: ")
            emp.transfer(new_department)
            print("Employee transferred successfully")
        else:
            print("Employee not found")
    elif choice == "get":
        id = int(input("Enter employee ID: "))
        emp = Employee.getEmployeeByID(id)
        if emp:
            emp.show()
        else:
            print("Employee not found")
    elif choice == "list":
        Employee.List_employees()
    elif choice == "q":
        break
    else:
        print("invalid choice")

cursor.close()
connection.close()

