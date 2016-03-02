#Emily Ferretti
#homework 7 OOP SP'16

class Sales:
  def __init__(self,name='No company'): #receives a string containing a company name
    self._companyName=name
    self._quarters=[0.0,0.0,0.0,0.0] #quarterly sales

  def setName(self,name):
    self._companyName=name

  def getName(self):
    return self._companyName

  def getSales(self):
    i=0
    while i<4: #to receive the sales for each quarter
      try:
        salesAmount=float(raw_input('Enter sales amount:'))
        self._quarters.append(salesAmount)
        i+=1
      except ValueError:
        print 'Enter a valid value'
      except EOFError:
	print 'Enter a value'

#to show the company name and sum of their sales
  def display(self):
    display=self._companyName+'\n'+str(sum(self._quarters))
    print display
