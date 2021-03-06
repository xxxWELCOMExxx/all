import csv

def read_employees(csv_file_location):

    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = "empDialect")

    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees("C:\\Users\\A645674\\PycharmProjects\\untitled01\\venv\\test_data\\employees.csv")
#print(employee_list) #will print list of dictionaries

#########ANOTHER_OPTION_OF_THE_FUNCTION_ABOVE####################
#def read_employees(csv_file_location):
#    employee_list = []
#    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
#    with open(csv_file_location) as employee:
#        employee_file = csv.DictReader(employee, dialect="empDialect")
#        for data in employee_file:
#            employee_list.append(data)
#        return employee_list
############################END###################################
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department "])#will append only tab Department


    department_data = {}
    for department_name in set(department_list): #will set duplicates into numbers
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+ ':'+str(dictionary[k])+"\n")
        f.close()

write_report(dictionary, "C:\\Users\\A645674\\PycharmProjects\\untitled01\\venv\\test_data\\test_report.txt" )