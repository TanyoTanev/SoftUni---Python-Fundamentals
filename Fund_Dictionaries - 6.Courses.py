'''6.Courses
Write a program that keeps information about courses. Each course has a name and registered students.
You ewill be receiving a course name and a student name, until you receive the command "end". Check if such course already exists, and if not,
add the course. Register the user into th course. When you receive the command "end", print the courses with their names and total registered users,
ordered by the count of registered users in descending order. For each contest print the registered users ordered by name in ascending order.

Input
Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
The product data is always delimited by " : ".

Output
Print the information about each course in the following the format:
"{courseName}: {registeredStudents}"
Print the information about each student, in the following the format:
"-- {studentName}"

Examples
Input
Output

Programming Fundamentals : John Smith
Programming Fundamentals : Linda Johnson
JS Core : Will Wilson
Java Advanced : Harrison White
end

Programming Fundamentals: 2
-- John Smith
-- Linda Johnson

JS Core: 1
-- Will Wilson
Java Advanced: 1
-- Harrison White

Algorithms : Jay Moore
Programming Basics : Martin Taylor
Python Fundamentals : John Anderson
Python Fundamentals : Andrew Robinson
Algorithms : Bob Jackson
Python Fundamentals : Clark Lewis
end

Python Fundamentals: 3
-- Andrew Robinson
-- Clark Lewis
-- John Anderson
Algorithms: 2

-- Bob Jackson
-- Jay Moore
Programming Basics: 1
-- Martin Taylor
'''

courses = dict()



while True:

     command = input().split(' : ')

     if command[0] == 'end':
        break

     elif command[0] not in courses:
         courses[command[0]] = [command[1]]
     else:
         courses[command[0]].append(command[1])


#print(courses)
#sorted_courses = dict( sorted(sorted_courses, key=lambda k: len(sorted_courses[k]), reverse=True))

sorted_courses = dict(sorted(courses.items(), key=lambda x:len(x[1]), reverse=True))
#print(sorted_courses)

for key in sorted_courses:
    sorted_courses[key] = (sorted(sorted_courses[key], key= lambda x: x[0], reverse=False ))


for course in sorted_courses:
    print(f"{course}: {len(sorted_courses[course])}")
    for i in range(len(sorted_courses[course])):
        print(f"-- {sorted_courses[course][i]}")
