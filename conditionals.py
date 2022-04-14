# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# language = "Python"

# if language == "Python":
#   print('Language is Python')
# elif language == "Java":
#   print("Language is Java")
# else:
#   print('No Match')

user = "Admin"
is_logged_in = True

if user == "Admin" and is_logged_in:
  print("Admin Page")
else:
  print("Bad Creds")

# False Values:
  # False
  # None
  # Zero of any numeric type
  # Any empty sequence. For example, '', (), [].
  # Any empty mapping. For example, {}.

condition = False

if condition:
  print("Evaluated to True")
else:
  print("Evaluated to False")