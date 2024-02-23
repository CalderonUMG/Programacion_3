class Tarea2():
    def __init__(self):
        menu='''

            ***** Menú *****
            1.- Convertir a Binario
            2.- Contar Dígitos
            3.- Raíz Cuadrada Entera
            4.- Convertir a Decimal desde Romano
            5.- Suma de Números Enteros
            6.- Salir
        '''
        option=''
        while(option!= '6'):
            print(menu) 
            option= input('Ingrese el número de la opción a utilizar: ')
            
            if(option=='1'):
                decimal= input('Ingrese un numero decimal: ')
                try:
                    self.convertir_a_binario(decimal, "")
                except:
                    print("An exception occurred")
            elif(option=='2'):
                decimal= input('Ingrese un numero: ')
                self.contar_digitos(decimal,1)
            elif(option=='3'):
                decimal= input('Ingrese un numero: ')
                self.raiz_cuadrada_entera(decimal)
            elif (option == '4'):
                decimal= input('Ingrese un numero romano: ')
                #print(self.convertir_a_decimal(decimal, 0))
                self.numero_cadena(decimal)
            elif(option=='5'):
                decimal= input('Ingrese un numero: ')
                print("La espuesta es: "+str(self.suma_numeros_enteros(decimal)))
        
    def convertir_a_binario(self, dec, res):
        cociente = int(dec)//2
        residuo= str(int(dec)%2)+res
        if cociente == 0:
            print("El número binario es: "+str(residuo))
        else:
            return self.convertir_a_binario(cociente, residuo)
    
    def contar_digitos(self, num, i):
        control=num[0:i]
        if(control==num):
            print("El numero posee: "+str(i)+" Dígitos :)")
        else:
            i +=1
            self.contar_digitos(num, i)

    def raiz_cuadrada_entera(self, numero):
        print("La Raiz Cuadrada es: "+self.calcular_raiz_cuadrada(numero, 1))
    
    def calcular_raiz_cuadrada(self,num,i):
        raiz=int(i)*int(i)
        if(raiz<=int(num)):
            i+=1
            return(self.calcular_raiz_cuadrada(num,i))
        else:
            i-=1
            return "La raiz cuadrada de: "+ str(num)+ " es: "+ str(i)
        

    def numero_cadena(self, numero):
        cadena = list(numero)
        print("El Numero es: "+str(self.convertir_a_decimal(cadena,0)))

    def convertir_a_decimal(self, cadena, decimal):
        if((len(cadena)>1)):
            if(cadena[0]== 'I' and cadena[1]=='V'):
                decimal = decimal + 4
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            elif(cadena[0]== 'I' and cadena[1]=='X'):
                decimal = decimal + 9
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            elif(cadena[0]== 'X' and cadena[1]=='L'):
                decimal = decimal + 40
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            elif(cadena[0]== 'X' and cadena[1]=='C'):
                decimal = decimal + 90
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            elif(cadena[0]== 'C' and cadena[1]=='D'):
                decimal = decimal + 400
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            elif(cadena[0]== 'C' and cadena[1]=='M'):
                decimal = decimal + 900
                del cadena[0]
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
            else:
                decimal = decimal + int(self.valores_letra(cadena[0]))
                del cadena[0]
                return self.convertir_a_decimal(cadena, decimal)
        elif(len(cadena)==1):
            decimal = decimal + int(self.valores_letra(cadena[0]))
            del cadena[0]
            return decimal
        else:
            return decimal

    def valores_letra(self, letra):
        tabla_valores={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        return tabla_valores.get(letra, "NA")

    def suma_numeros_enteros(self, numero):
        if (numero == 0):
            return 0
        else:
            return int(numero) + self.suma_numeros_enteros(int(numero)-1)






        

        
mostrar=Tarea2()