positivo=0
negativos=0
mult15=0
sumaPar=0

for x in range(10):
   numero=int(input("Numero:"))
   if numero>0:
       positivos=positivo+1
    else:
        negativos=negativos+1
    if numero%15==0:
        mult15=mult15+1
    ifnumero%2==0:
        sumaPar=sumaPar+numero
print("Positivos:",positivos)
print("Negativos:",negativos)
print("Multiplos de 15:",mult15)
print("suma de los pares:",sumaPar)
  
