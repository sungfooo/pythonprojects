print "hello"

variable = "value of the variable"

data types 
#integers
123421
#float (with decimal)
123.23
#boolean
True
False

#array (group of data types)
[1,True,"string"]

#dictionary or object
#{""}

#for loop - can be used to loop through arrays or objects one element at a time

#for x_element in x_array_or_object:

#example v

roommates = ["callie", "gary", "ari", "katie", "tim", "peter"]

for x in roommates:
    print x[::-1]


def dogger(arg):
    arg = arg+"dog"
    print arg

for x in roommates:
    dogger(x)
