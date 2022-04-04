# How to update a dictionary

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}
door = 100
marks.update(internal_marks)
# marks{'Physics'=89}
marks.update({'Physics': door})

print(marks)

# Output: {'Physics': 67, 'Maths': 87, 'Practical': 48}