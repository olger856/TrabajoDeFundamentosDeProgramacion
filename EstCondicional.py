def ejercicio01():
  #Definir Variables y otros
  print("Pago por horas")
  totalY=0
  #Datos de entrada
  cantidadX=int(input("Ingrese cantidad de horas que trabajo:"))
  montoP=int(input("Ingrese el pago por hora:"))
  #Proceso
  if cantidadX>=40:
    totalY=2*(cantidadX*montoP)
  else:
    totalY=cantidadX*montoP
  #Datos de Salida
  print("El Monto a pagar es:", totalY)

def elecciones():
  #Definir Variables y otros
  print("Verifique si puede votar o no")
  #Datos de entrada
  edadX=int(input("Ingrese su edad:"))
  #Proceso
  if edadX>=18:
    print("USTED SI PUEDE VOTAR")
  else:
    print("USTED NO PUEDE VOTAR POR SER MENOR DE EDAD")

def AutobusTortuga():
  #Definir Variables
  montoFinal=0.0
  #Datos de Entrada
  PaisNcomp=input("Ingrese al pais que desea ir\nA=Mexico\nB=P.V\nC=Acapulco\nD=Cancun:")
  costoXhora=float(input("Ingrese cuanto se cobra por hora:"))
  #Proceso
  if PaisNcomp=="A":
    montoFinal=750*costoXhora;
    PaisNcomp="Mexico"
  elif PaisNcomp=="B":
    montoFinal=800*costoXhora;
    PaisNcomp="P.V"  
  elif PaisNcomp=="C":
    montoFinal=1200*costoXhora;
    PaisNcomp="Acapulco"
  elif PaisNcomp=="D":
    montoFinal=1800*costoXhora;
    PaisNcomp="Cancun";
  else:
    print("La opcion que ingreso no existe! intente nuevamente....")
  #Datos de Salida
  print("El total del monto es: ", montoFinal," su destino es a : ",PaisNcomp)

def sueldoXhora():
  #Definir Variables
  pagoT=0
  #Datos de entrada
  pagoH=float(input("Ingrese cuanto le pagan por hora:"))
  trabajosH=float(input("Ingrese cuantas horas trabajo durante toda esta semana:"))
  #Proceso
  if trabajosH<=40: 
    pagoT=(pagoH*trabajosH)
  elif trabajosH>40 and trabajosH<=45:
    pagoT=(pagoH*trabajosH)*2
  elif trabajosH>45 and trabajosH<=50:
    pagoT=(pagoH*trabajosH)*3
  else:
    print("No se permite trabajar mas de 50 horas")
  #Datos de Salida
  print("Su sueldo de la semana es: ", pagoT,"el total de horas trabajadas es: ",trabajosH,"horas: ")

def Viaje():
  #Definir Variables
  montoT=0
  #Datos de entrada
  CantidadA=float(input("Ingrese cuantos alumnos viajaran:"))
  #Proceso
  if CantidadA>=101:
    montoT=CantidadA*20
  elif CantidadA>50 and CantidadA<=100:
    montoT=CantidadA*35
  elif CantidadA>20 and CantidadA<=49:
    montoT=CantidadA*40
  elif CantidadA<20:
    montoT=CantidadA*70
  #Datos de Salida
  print("La cantidad de alumnos que van a ir es: ", CantidadA,"y el monto a pagar es: ", montoT)

  
def Educacion():
    #Definir Variables
    Premio=0.0
    #Datos de entrada
    Puntos=float(input("Ingrese los puntos acumulados:"))
    Salario=float(input("Cuanto es su salario minimo:"))
    #Proceso
    if Puntos<=100:
      Premio=Salario
    elif Puntos>=101 and Puntos<=150:
      Premio=Salario*2
    elif Puntos>=151:
      Premio=Salario*3
    #Datos de Salida
    print("Su bono es de un total de: ", Premio,"y sus puntos en total es: ", Puntos)

def compra():
  #Datos de entrada
  dinero=float(input("Cuanto dinero tiene:"))
  #Proceso
  if dinero>=50000:
    print("Usted se puede comprar el paquete A y viene una televicion, un modular, 3 pares zapatos, 5 camisas y 5 pantalones")
  elif dinero>=20000 and dinero<50000:
    print("Usted se puede comprar el paquete B y viene una grabadora, 3 pares de zapato, 5 camisas, 5 pantalones")
  elif dinero>=10000 and dinero<20000:
    print("Usted se puede comprar el paquete C y viene 2 pares de zapatos 3 camisas y 3 pantalones")
  elif dinero<10000:
    print("Usted se puede comprar el paquete D y viene un par de zapatos, 2 camisas y 2 pantalones")

def salud():
  #Datos de entrada
  edad=float(input("Que edad tiene:"))
  #Proceso
  if edad>70:
    print("La vacuna que deve ser colocada es la C sin importar el sexo")
  elif edad>=16 and edad<=69:
    print("Se pone la vacuna A si es varon y la vacuna B si es mujer")
  elif edad<16:
    print("Se pone la vacuna A sin importar el sexo")

def descuentoX():
  #Definir Variables
  Pago=0.0
  Descuento=0.0
  #Datos de entrada
  costoT=float(input("Cuanto es el costo que gasto en las compras: "))
  #Proceso
  if costoT>=200:
    Descuento=(costoT*15)/100
    pago=(costoT-Descuento)
  elif costoT>=100 and costo<200:
    Descuento=(costoT*12)/100
    pago=costo-Descuento
  elif costo<100:
    Descuento=(costoT*10)/100
    pago=costo-Descuento
  #Datos Salida
  print("El monto a pagar es", pago,"y el descuento es de un total de:", Descuento)

def estacionamiento():
  #Definir Variables
  PrecioT=0.0
  #Datos de Entrada
  tarifaNcomp=input("Ingrese cuantas horas va a estar en el estacionamiento\nA=2Horas\nB=3Horas\nC=5Horas\nD=10Horas:")
  Cpersonas=float(input("Ingrese cuantos autos se van a estacionar:"))
  #Proceso
  if tarifaNcomp=="A":
    PrecioT=5.00*Cpersonas;
    tarifaNcomp="2Horas"
  elif tarifaNcomp=="B":
    PrecioT=4.00*Cpersonas;
    tarifaNcomp="3Horas"  
  elif tarifaNcomp=="C":
    PrecioT=3.00*Cpersonas;
    tarifaNcomp="5Horas";
  elif tarifaNcomp=="D":
    PrecioT=2.00*Cpersonas;
    tarifaNcomp="10Horas";
  else:
    print("La opcion que ingreso no existe! intente nuevamente....")
  #Datos de Salida
  print("El precio total es: ", PrecioT," y las horas escojidas son : ",tarifaNcomp)

#ejercicio01()
#elecciones()
#AutobusTortuga()
#sueldoXhora()
#Viaje()
#Educacion()
#compra()
#salud()
#descuentoX()
estacionamiento()