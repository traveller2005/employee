import sqlite3


"""
Initialize the database connection and create the table if it does not exist.
Args:
    db (str): The path to the database file.
Returns:
    None
"""
class Database :
    def __init__(self,db):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        sql= """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age TEXT NOT NULL,
                job TEXT NOT NULL,
                email Text NOT NULL, 
                gender TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
                )
        """
        self.cur.execute(sql)
        self.con.commit()
#===================add employee to database==============================
    """This function is used to insert a new record into the employees table.
    Args:
        name (str): The name of the employee.
        age (str): The age of the employee.
        job (str): The job of the employee.
        email (str): The email of the employee.
        gender (str): The gender of the employee.
        phone (str): The phone number of the employee.
        address (str): The address of the employee.
    Returns:
        None
    Raises:
        ValueError: If any of the arguments are missing or invalid.
    """
    def insert (self,name,age,job,email, gender,phone,address ):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                                (name,age,job,email, gender,phone,address))                              
                                                           
        self.con.commit()
    #===================fetch all the records from database==============================    
    """
    This function is used to fetch all the records from the employees table.
    Returns:
        list: A list of dictionaries containing all the records from the employees table.
    """
    def fetch(self):
        self.cur.execute("SELECT * FROM employees ")
        row = self.cur.fetchall()
        return row
    #===================Delete employee FROM database==============================
    """
    Delete an employee record from the database.
    Args:
        id (int): The id of the employee record to be deleted.
    Returns:
        None
    Raises:
        ValueError: If the id is not a valid integer.
    """
    def remove(self,id):
        self.cur.execute("DELETE from employees where id = ?",(id,))
        self.con.commit()
    #===================Update employee in the database==============================
    """
    Update an employee record in the database.
    Args:
        id (int): The id of the employee record to be updated.
        name (str): The name of the employee.
        age (str): The age of the employee.
        job (str): The job of the employee.
        email (str): The email of the employee.
        gender (str): The gender of the employee.
        phone (str): The phone number of the employee.
        address (str): The address of the employee.
    Returns:
        None
    Raises:
        ValueError: If the id is not a valid integer.
    """    
    
    def update(self,id,name,age,job,email, gender,phone,address ):
        self.cur.execute("update employees set name =? , age=?, job=?, email=?,gender=?, phone=?, address=? where id =?",
                         (name,age,job,email, gender,phone,address ,id))
        self.con.commit()



          
          

        
    
                