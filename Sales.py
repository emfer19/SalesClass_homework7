class Sales:
  def __init__(self,name='No company',quarters=[0.0,0.0,0.0,0.0]):
    self._companyName=name
    self._quarters=quarters

  def setName(self,name):
    self._companyName=name

  def getName(self):
    return self._companyName

  def getSales(self):
    i=0
    while i<4:
      try:
        salesAmount=float(raw_input('Enter sales amount:'))
        self._quarters.append(salesAmount)
        i+=1
      except ValueError:
        print 'Enter a valid value'

  def display(self):
    display=self._companyName+'\n'+str(sum(self._quarters))
    print display
