courses = ['Math', 'History', 'Sciences', "Art"]
nums = [6, 5, 2, 9]
#popped = courses.pop()


#courses.reverse() or courses.sort(reverse=True)
#courses.append("Techno")

# nums.sort(reverse=True)
# courses.sort(reverse=True)
# sorted_courses = sorted(courses)

# print(sorted_courses)
# print(min(nums)) / print(max(nums)) / print(sum(nums))

#print(popped)

# print(courses.index('Math')) / print('Art' in courses) return True / print('Gym' in courses) return false

#Loop 

# for index, course in enumerate(courses, start=1):
#     print(index, course)

# join
# course_str = ' - '.join(courses)

# new_list = course_str.split(' - ');

# print(course_str)
# print(new_list)

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()