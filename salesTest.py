#homework 7 test file

from Sales import*

comp1=Sales()
print 'Enter an invalid input and then 4 for sales:'
comp1.getSales()

comp1.setName('bugs bunny') #sets company name to bugs bunny
print comp1.getName() #should print 'bugs bunny'

comp2=Sales('marilyn')


comp1.display() # should print bugs bunny \n 16
comp2.display() # should print marilyn \n 0
