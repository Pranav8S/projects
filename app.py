#objects of student class

from student_template import student

student1 = student("pranav",34,"CS",7.8,True)
student2 = student("sumanyu",14,"AIDS",9.9,True)
student3 = student("Jim",40,"Business",5.7,False)




print(student2.gpa)

print(student3.isLocal)

print(student1.major)

print(student3.has_distinction())

print(student2.has_distinction())

