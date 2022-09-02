
class Decimal:
    def convertIterative(num, outputType):
        if(outputType == "binario"):
            modulos = ""

            while num != 0:
                modulo = int(num) % 2
                cociente = int(num) / 2
                modulos = modulos + str(modulo)
                num = cociente
                
                resp = modulos[::-1] 
            resp = resp[1:]
            return resp    
        
        elif(outputType == "octal"):
            octal = ""
            while int (num) > 0:
                residuo = int(num) % 8
                octal = str(residuo) + octal
                num = int (num) / 8
            return octal
        
        elif(outputType == "hexadecimal"):
            suma = num
            hexa = ""
            hexa_dic = {10:'A', 11:'B', 12:'C', 13:'D',14:'E',15:'F'}
            while suma > 0:
                residuo = suma % 16
                if(residuo > 9):
                    residuo = hexa_dic[residuo]
                hexa = str(residuo) + hexa
                suma = int (suma / 16)
            return hexa
    
    def convertRecursive(num, outputType):
        if(outputType == "binario"):
            num = int(num)
            residuo = num % 2
            num = int (num / 2)     
            if(num == 0):
                return str(residuo)
            else:
                return Decimal.convertRecursive(num,"binario") + str(residuo)
            
        elif(outputType == "octal"):
            num = int(num)
            residuo = num % 8
            num = int (num / 8)     
            if(num == 0):
                return str(residuo)
            else:
                return Decimal.convertRecursive(num,"octal") + str(residuo)
            
        elif (outputType=="hexadecimal"):
            hexa_dic = {10:'A', 11:'B', 12:'C', 13:'D',14:'E',15:'F'}
            num = int(num)
            residuo = num % 16
            if(residuo > 9):    
                residuo = hexa_dic[residuo]
            num = int (num / 16)     
            if(num == 0):
                return str(residuo)
            else:
                return Decimal.convertRecursive(num,"hexadecimal") + str(residuo)

class Binary:
    def convertIterative(num, outputType):
        if(outputType=="decimal"):
            suma = 0
            total =len(num)
            for digit in num:
                digit = int(digit)
                suma = suma + digit * 2**(total-1)
                total = total-1
            return suma
        
        
        elif(outputType=="octal"):
            suma = Binary.convertIterative(num, "decimal") 
            return Decimal.convertIterative(suma, "octal")
        
        
        elif(outputType == "hexadecimal"):
            suma = Binary.convertIterative(num, "decimal")
            return Decimal.convertIterative(suma,"hexadecimal")
        

        
    
    def convertRecursive(num, outputType):
        if(outputType =="decimal"):
    
            total =len(num)
            if(total == 1):
                resp = int(num)
                return resp
        
            digit = int(num[0])
            rest = num[1:]
            
            return digit * 2**(total-1) + Binary.convertRecursive(rest,outputType)
        
        elif(outputType== "octal"):
            numero_nuevo = Binary.convertRecursive(num, "decimal")
            return Decimal.convertRecursive(numero_nuevo,"octal")
            
        elif(outputType=="hexadecimal"):
            numero_nuevo = Binary.convertRecursive(num, "decimal")
            return Decimal.convertRecursive(numero_nuevo,"hexadecimal")


is_active = True
menu = 0
while is_active :

    menu = int(input(" 1. Convertir de decimal a binario \n 2. Convertir de decimal a octal \n 3. Convertir de decimal a hexadecimal \n" 
            " 4. Convertir de binario a decimal \n 5. Convertir de binario a octal \n 6. Convertir de binario a hexadecimal \n "
            "7. Convertir de octal a decimal \n 8. Convertir de octal a binario \n 9. Convertir de octal a hexadecimal \n"
            " 10. Convertir de hexadecimal a binario \n 11. Convertir de hexadecimal a octal \n 12. Convertir de hexadecimal a decimal \n"
            " Escribe tu respuesta: "))

    if menu == 1:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertIterative(num,"binario")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertRecursive(num,"binario")
            print('El número es: ', dec)
        menu = 0


    elif menu == 2:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertIterative(num,"octal")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertRecursive(num,"octal")
            print('El número es: ', dec)
        menu = 0


    elif menu == 3:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertIterative(num,"hexadecimal")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = int(input('Ingresa el número que quieres convertir: '))
            dec = Decimal.convertRecursive(num,"hexadecimal")
            print('El número es: ', dec)
        menu = 0


    elif menu == 4: 
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertIterative(num,"decimal")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertRecursive(num,"decimal")
            print('El número es: ', dec)
        menu = 0


    elif menu == 5: 
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertIterative(num,"octal")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertRecursive(num,"octal")
            print('El número es: ', dec)
        menu = 0


    elif menu == 6:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertIterative(num,"hexadecimal")
            print('El número es: ', dec)
        elif num_elej == 2:
            print('Recursiva')
            num = input('Ingresa el número que quieres convertir: ')
            dec = Binary.convertRecursive(num,"hexadecimal")
            print('El número es: ', dec)
        menu = 0

    elif menu == 7:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            # Octal a Decimal
            def oct_dec(numero):
                suma = 0
                i = 0
                while numero!= 0:
                    resultado = numero%10
                    suma = suma + resultado*pow(8,i)
                    i = i + 1
                    numero = int(numero/10)
                return suma
            scan_num = int(input("Escriba el número en el que quiere hacer la conversión: \n"))
            solucion = oct_dec(scan_num)
            print("El número en base octal " ,scan_num, " en base decimal sería " ,solucion )
            num_elej = 0
        elif num_elej == 2:
            print('Recursiva')
            def oct_dec_recursive(num):
                total =len(num)
                if(total == 1):
                    resp = int(num)
                    return resp
            
                digit = int(num[0])
                rest = num[1:]
                
                return digit * 8**(total-1) + oct_dec_recursive(rest)
            scan_num = input("Escriba el número en el que quiere hacer la conversión: \n")
            solucion = oct_dec_recursive(scan_num)
            print("El número en base octal " ,scan_num, " en base decimal sería " ,solucion )
        menu = 0


    elif menu == 8:
        def oct_bin(numero):
            print('El número octal', numero, end='' )
            # Octal a Binario
            suma = 0
            i = 0
            while numero!= 0:
                resultado = numero%10
                suma = suma + resultado*pow(8,i)
                i = i + 1
                numero = int(numero/10)
            d = []
            while(suma >= 1):
                d.append(suma%2);
                suma = int(suma/2);
            temporal = d[:: -1]
            print(' Corresponde al binario ', end= '')
            for k in temporal:
                print(k, end='' )
            print()
            
        scan_num = int(input("Escriba el número en el que quiere hacer la conversión: \n"))
        solucion = oct_bin(scan_num)
        menu = 0
    

    elif menu == 9:
        def oct_hex(n):
            suma=0
            i=0
            while n!=0:
                r=n%10
                suma+=r*pow(8,i)
                i=i+1
                n=int(n/10)
                hexadecimal = format(suma, '0x')
                solucion = hexadecimal
            print('el número ',scan_num,' corresponde al número hexadecimal ', solucion)
        scan_num = int(input('Dijite el numero octal que quiere convertir \n'))
        solucion = oct_hex(scan_num)
        menu = 0

    
    elif menu == 10:
        hexa = input('Escriba el numero hexadecimal que quiere convertir \n')
        dec = int(hexa, 16)
        def hexa_bin(numero): 
            d=[]
            print('El hexadecimal',hexa,end=' ')
            while(numero>=1):
                d.append(numero%2);
                numero =int(numero/2);
            suma = d[::-1]
            print('correponde al número binario', end=' ')
            for k in suma:
                print(k,end='')
            return ''
        solucion = hexa_bin(dec)
        print(solucion)
        menu = 0
    
    elif menu == 11:
        hexa = input('Escriba el numero hexadecimal que quiere convertir \n')
        dec = int(hexa, 16)
        def hexa_oct(numero): 
            d=[]
            print('El hexadecimal',hexa,end=' ')
            while(numero>=1):
                d.append(numero%8);
                numero =int(numero/8);
            suma = d[::-1]
            print('correponde al octal', end=' ')
            for k in suma:
                print(k,end='')
            return ''
        solucion = hexa_oct(dec)
        print(solucion)
        menu = 0
    

    elif menu == 12:
        num_elej = int(input('Quiere que sea de forma... \n 1. Iterativa \n 2. Recursiva \n Escribe tu respuesta: '))
        if num_elej == 1: 
            print('Iterativa')
            hexa = input('Escriba el numero hexadecimal que quiere convertir \n')
            dec = int(hexa, 16)
            def hexa_dec(numero): 
                d=[]
                print('El hexadecimal',hexa,end=' ')
                while(numero>=1):
                    d.append(numero%10);
                    numero =int(numero/10);
                suma = d[::-1]
                print('correponde al número decimal', end=' ')
                for k in suma:
                    print(k,end='')
                return ''
            solucion = hexa_dec(dec)
            print(solucion)
        elif num_elej == 2:
            print('Recursiva')
            def hex_dec_recursive(num):
                hexa_dic = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13,'E':14,'F':15}
                total =len(num)
                if(total == 1):
                    resp = hexa_dic[num]
                    return resp
            
                digit = hexa_dic[num[0]]
                rest = num[1:]
                
                return digit * 16**(total-1) + hex_dec_recursive(rest)
            scan_num = input("Escriba el número en el que quiere hacer la conversión: \n")
            solucion = hex_dec_recursive(scan_num)
            print("El número en base hexadecimal " ,scan_num, " en base decimal sería " ,solucion )
        menu = 0
        
        
    elif menu == 0:
        is_active = False   
