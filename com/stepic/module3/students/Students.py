lines = [line.rstrip('\n') for line in open('dataset.txt')]

students = []
ranks = []

for line in lines:
    temp_array = line.split(";")
    students.append(temp_array)

first_avg = 0
second_avg = 0
third_avg = 0

number_of_students = len(students)

for student in students:
    avg = (float(student[1]) + float(student[2]) + float(student[3])) / 3
    ranks.append(str(avg))
    first_avg += float(student[1])
    second_avg += float(student[2])
    third_avg += float(student[3])

last_string = [str(first_avg / number_of_students), str(second_avg / number_of_students), str(third_avg / number_of_students)]

ouf = open('result.txt', 'w')

for rank in ranks:
    ouf.write(rank + "\n")

for rank in last_string:
    ouf.write(rank + " ")

ouf.close()