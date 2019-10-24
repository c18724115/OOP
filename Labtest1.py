#This program will generate a program that will ask the user to input
#the height (number of rows) as user would like and then and then generate a
#pascal triangle with that many rows


#Author:james Delahunty C18724115
#Date: 24/10/2019
#object orientated programming CMPU2016
def make_new_row(old_row):
    old_row +=1
    new_row = [old_row]
    if old_row is[]:
        for i in range(n):
            new_row[i].append(i+1)
    elif old_row is[1]:
        return(1,1)
    print(new_row)

num_of_rows=int(input("Enter the desired height of pascal's triangle: "))
list=[]
#'[]' signify a list and the list is known as 'list'
if num_of_rows >= 1:
    for ind in range(num_of_rows):
        list.append([])
        #the append() adds the argument as a single element to the end of a list
        list[ind].append(1)
        #The for loop is used to append sub-lists into an empty list defined earlier.
        for j in range(1,ind):
            list[ind].append(list[ind-1][j-1]+list[ind-1][j])
        if(num_of_rows!=0):
            list[ind].append(1)

    print("Printing whole list of lists")
    #Part 3
    print(list)
    print("Printing list of lists, one list at a time:")
    #for loop with ind and j as indexes
    for ind in range(num_of_rows):
        #indentation for triange
        print("   "*(num_of_rows-ind),end=" ",sep=" ")
        #the separator(sep) between the arguments or items in an iterator to print.
        for j in range(0,ind+1):
            #format the string
            print('{0:6}'.format(list[ind][j]),end=" ",sep=" ")
        print()
#error checking for user input
elif num_of_rows == 0:
    print("0")

#Part 4
abc = ''.join([str(ind)for ind in list])
print(abc.center(100))
#formatting the string is an other way of centring the triangles
