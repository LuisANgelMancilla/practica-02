#!/usr/bin/env python
# coding: utf-8

# ##Primer programa 
# 

# #Escribir un programa que me permita aplicar el 10% de descuento si la compra total es mayor a $100.

# In[8]:


compra=int(input("Introduce el costo de tu compra: "))

if compra <= 100: 
    print("Su compra fue menor o igual a 100, su costo fue de ")
    print (compra)
elif compra > 100: 
    print("Aplica descuento del 10 % por compras superiores a 100$")
    compra=compra*.9
    print ('Su compra con el descuento es de:')
    print(compra)


# #Ejercicio 2

# ##Sabiendo que la fórmula para obtener el área de un triángulo es a = (b x h) / 2, donde b es la longitud de la base del triángulo, y h es su altura. Escribir un programa que permita realizar el cálculo del área de un triángulo. Si el área contiene valores decimales, imprimir el resultado con dos dígitos.

# In[2]:


#dimenciones 
b=13.21
h=3
print ('Las dimenciones son \nBase=')
print (b)
print ('La altura es: ')
print (h)
print ('El area es la siguiente: ')
area=(b*h)/2
f"{area:.2f}"


# Ejecicio 3

# La fórmula para el Índice de Masa Corportal es IMC = kg/m2 donde kg es el peso de la persona en kilogramos y m2 es la altura en metros al cuadrado. Realizar un programa que calcula el IMC cuando se le provee el peso y la altura.

# In[3]:


altura=int(input("Introduce algo a través del teclado tu altura: "))
peso=int(input("Introduce algo a través del teclado tu peso: "))
imc=peso*altura^2
print ('Su IMC es el siguiente: ')
print (imc)


# In[ ]:




