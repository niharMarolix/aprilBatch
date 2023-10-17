import pandas as nihar

employeeData = {
    "employees":[
        {"id":1, "name":"sia", "des":"CEO", "Salary":"8LPA", "dept":"management", "roles":["Managing company", "looking for talent"]},
        {"id":2, "name":"ram", "des":"CTO", "Salary":"9LPA", "dept":"Tech","roles":["R&D", "Leading the Tech"]},
        {"id":3, "name":"lakshya", "des":"Assocaite", "Salary":"6LPA", "dept":"Tech","roles":["R&D", "Developing the tech"]}
    ]
}

table = nihar.DataFrame(employeeData['employees'])
print(table)