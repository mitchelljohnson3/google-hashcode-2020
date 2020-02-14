#input file
#17 4
#2 5 6 8

#-input top line
# #slices, #typesOfPizza
#-input bottom line
# #num slices in each pizza

#output
#single int - num different types of pizzas to order - K
#K integers, the types of pizza to order

file = open('a_example.in', 'r')
slices = file.readline().split(' ')[0]
types = file.readline().split(' ')
print(slices, types)