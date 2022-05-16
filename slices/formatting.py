from unicodedata import name


person = {'name': 'Jenn', 'age': 26}

l = ['Jenn', 26]

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

# tag = 'h1'
# text = 'This is some text'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# p1 = Person("Alex", "27")

# sentence = 'My name is {0.name} and I am {0.age}'.format(p1)

sentence = 'My name is {name} and I am {age}'.format(**person)

print(sentence)

# for i in range(1,11):
#     sentence = 'The value is {}'.format(i)
#     print(sentence) 
    
# pi = 3.14159265

# sentence = 'Pi is equal to {:.3f}'.format(pi)

# sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)

# print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)