#Dictionary Comprehension
#new_dict = {new_key : new_value for (key,value) in dict.items() if test}
names = ["Alex","Florida","Aaarti","Nimisha","Javed","Abhijeet"]
#new_dict = {new_key : new_value for student in names if test}
import random
student_scores = {student : random.randint(0,101) for student in names}
print(f"All Students with their scores are : {student_scores}")
passed_students = {student : score for (student,score) in student_scores.items() if score >= 60}
print(f"Passed Students with their scores are : {passed_students}")
failed_students = {student : score for (student,score) in student_scores.items() if score < 60}
print(f"Failed Students with their scores are : {failed_students}")