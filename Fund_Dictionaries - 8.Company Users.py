'''8.Company Users

Write a program that keeps information about companies and their employees.
You will be receiving a company name and an employee's id, until you receive the command "End" command. Add each employee to the given company.
Keep in mind that a company cannot have two employees with the same id.
When you finish reading the data, order the companies by the name in ascending order.
Print the company name and each employee's id in the following format:

{companyName}
-- {id1}
-- {id2}
-- {idN}

Input / Constraints
Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
The input always will be valid.

Examples
Input
Output

SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

HP
-- BB12345
Microsoft
-- CC12345
SoftUni
-- AA12345
-- BB12345

SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End


Lenovo
-- XX23456
Movement
-- DD11111
SoftUni
-- AA12345
-- CC12344
'''

companies = dict()

while True:

    command = input().split(' -> ')

    if command[0] == 'End':
        break
    else:
        if command[0] not in companies:
            companies[command[0]]=[command[1]]
        elif command[0] in companies and command[1] not in companies[command[0]]:
            companies[command[0]].append(command[1])

sorted_companies = dict( sorted(companies.items(), key=lambda x:x[0], reverse=False) )
#print(sorted_companies)

for key in sorted_companies.keys():
    print(f" {key}"  )
    for i in range(len(sorted_companies[key])):
        print(f"-- {sorted_companies[key][i]}")