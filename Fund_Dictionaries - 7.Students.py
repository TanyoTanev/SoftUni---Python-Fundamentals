'''7.Student Academy
Write a program that keeps information about students and their grades.
You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade. Check if the student already
exists and if not, add him. Keep track of all grades for each student.
When you finish reading the data, keep the students with average grade higher than or equal to 4.50. Order the filtered students by average grade in
descending order.

Print the students and their average grade in the following format:
{name} –> {averageGrade}
Format the average grade to the 2nd decimal place.
Examples
Input
Output

Input
Output

5
John
5.5
John
4.5
Alice
6
Alice
3
George
5

John -> 5.00
George -> 5.00
Alice -> 4.50

5
Amanda
3.5
Amanda
4
Rob
5.5
Christian
5
Robert
6

Robert -> 6.00
Rob -> 5.50
Christian -> 5.00
'''

N = int(input())
students = dict()


for i in range(N):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)


for key in list(students):
    students[key]= sum (students[key])/len(students[key])
    if students[key] < 4.5:
        students.pop(key)

#for key in list(students):
  #if students[key] < 4.5:
   #     students.pop(key)

sorted_students = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))


for key in sorted_students:
    print(f"{key} -> {sorted_students[key]:.2f}")