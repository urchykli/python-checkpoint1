# Create the following methods and make sure they return the correct data type
# and/or value

# #1: Create a method called num_list_with_arg that takes a positive integer and
# returns a list of integers between 1 and the number passed in.
#
# So if the number 5 is passed in, num_list_with_arg should return [1, 2, 3, 4]

result = []
n = 0

def num_list_with_arg(n):
	i = 1
	while i < n:
		result.append(i)
		i += 1
	print(result)

num_list_with_arg(n)

# #2: Modify the has_ruby_exp method below so that it returns a SORTED list of
# all instructors who have Ruby experience (i.e. where "ruby" == True)
# The list should contain only names of instructors.
# make sure you name the list ruby_experience before returning it.

# def has_ruby_exp():
#     ruby_experience = sorted(unsorted_ruby)
#     unsorted_ruby = []
#     experience = {
#         'jimmy': {
#             'bjj': False,
#             'soccer': False,
#             'ruby': True,
#             'baking': True,
#             'biking': True,
#             'pasta': False
#         },
#         'don': {
#             'bjj': False,
#             'soccer': False,
#             'ruby': True,
#             'baking': True,
#             'biking': False,
#             'pasta': False
#         },
#         'zakk': {
#             'bjj': False,
#             'soccer': False,
#             'ruby': True,
#             'baking': False,
#             'biking': False,
#             'pasta': True
#         },
#         'hector': {
#             'bjj': True,
#             'soccer': True,
#             'ruby': False,
#             'baking': False,
#             'biking': True,
#             'pasta': False
#         }
#     for i < len(expreience):
#     i = 0
#         if experience[i][2] == True:
#             unsorted_ruby.append(experience[0])
#             i +=
#         else:
#             i +=
#     print(ruby_experience())
#     }
    
# has_ruby_exp()


# #3: Create a method called toggle_str_num that takes an argument. If the
# argument is a string, convert it to an integer and return the integer; If the
# argument is an integer, convert it to a string and return the string; If the
# argument is neither a string nor an integer, return the string "this is not a
# str or a int":


# Commit when you finish working on these questions!