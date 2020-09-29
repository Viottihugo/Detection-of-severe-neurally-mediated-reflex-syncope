from numpy import array, sign, zeros
from scipy.interpolate import interp1d
from matplotlib.pyplot import plot,show,grid
import pandas as pd
"""
import csv
import numpy
"""
#hay que agregarla para hacerte la vida mas fácil si vas a trabajar con csv

clases = pd.read_csv("clases.csv", sep=";")




"""
s=[]
rownum = 0
columnnum = 0	
with open("originales.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # para convertir los a float
        
    for row in reader:
      row=numpy.array(row) 
      s.append(row)
      columnnum=len(row)
      rownum += 1
""" 
# No se si es lo q quieren, pero con esto cada fila de la lista es un array, s quedaría completo.

s = array([1,4,3,5,3,2,4,3,4,5,4,3,2,5,6,7,8,7,8]) #This is your noisy vector of values.

"""
q_u = numpy.zeros((columnnum, rownum))
q_l = numpy.zeros((columnnum, rownum))
"""
# esto lo tuve que hacer para crear los nuevos arrays vacíos. Igual, como no me di cuenta que todo lo de abajo solo toma un valor, es medio al Pedo

q_u = zeros(s.shape)
q_l = zeros(s.shape)

#Prepend the first value of (s) to the interpolating values. This forces the model to use the same starting point for both the upper and lower envelope models.

u_x = [0,]
u_y = [s[0],]

l_x = [0,]
l_y = [s[0],]

#Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.
asd=range(1,len(s)-1)

for k in asd:
    if (sign(s[k]-s[k-1])==1) and (sign(s[k]-s[k+1])==1):
        u_x.append(k)
        u_y.append(s[k])

    if (sign(s[k]-s[k-1])==-1) and ((sign(s[k]-s[k+1]))==-1):
        l_x.append(k)
        l_y.append(s[k])

#Append the last value of (s) to the interpolating values. This forces the model to use the same ending point for both the upper and lower envelope models.

u_x.append(len(s)-1)
u_y.append(s[-1])

l_x.append(len(s)-1)
l_y.append(s[-1])

#Fit suitable models to the data. Here I am using cubic splines, similarly to the MATLAB example given in the question.

u_p = interp1d(u_x,u_y, kind = 'cubic',bounds_error = False, fill_value=0.0)
l_p = interp1d(l_x,l_y,kind = 'cubic',bounds_error = False, fill_value=0.0)

#Evaluate each model over the domain of (s)
for k in asd:
    q_u[k] = u_p(k)
    q_l[k] = l_p(k)

#Plot everything
plot(s);plot(q_u,'r');plot(q_l,'g');grid(True);show()

