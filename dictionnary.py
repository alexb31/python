from unicodedata import name


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# student['phone'] = '555-555'

# del student['age']
# age = student.pop('age')

for key, value in student.items():
  print(key, value)

student.update({'name': 'Jack', 'phone': '555-555'})

print(student)
# print(student.get('phone', 'Not found'))