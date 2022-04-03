from operator import truediv 
import os
import math

opcao = True

linha = '-' * 50
titulo = 'Calculadora de Cinematica simples'
print(linha)
print(titulo.center(50))
print(linha)

while opcao == True:

    seleção = int(input("\nPor favor escolha uma opção\n1-Posicao\n2-Velocidade\n3-Aceleracao Media\n4-Torricelli\n\n")) #opcao
    os.system("cls")

    if seleção == 1:
        s0 = int(input("Digite a posicao inicial: "))
        v0 = int(input("Digite a velocidade inicial: "))
        t = int(input("Digite o tempo gasto: "))
        a = int(input("Digite a aceleracao continua: "))   

        s = s0 + v0 * t + (a * pow(t, 2))/2
        print (f"A distancia percorrida foi de {s} metro(s)\n")
       

    elif seleção == 2:
        v0 = int(input("Digite a velocidade inicial: "))
        a = int(input("Digite a aceleracao continua: "))  
        t = int(input("Digite o tempo gasto: "))

        v = v0 + a * t
        print (f"A velocidade nesse intervalo de tempo e de {v} m/s\n")
        
    elif seleção == 3:
        v0 = int(input("Digite a velocidade inicial: "))
        v = int(input("Digite a velocidade final: "))
        t0 = int(input("Digite o tempo inicial: "))
        t = int(input("Digite o tempo final: "))

        a = (v-v0)/(t-t0)
        print (f"A aceleração media nesse intervalo de tempo é de {a} m/s²\n")
        
    elif seleção == 4:
        v0 = int(input("Digite a velocidade inicial: "))
        a = int(input("Digite a aceleracao continua: "))
        s0 = int(input("Digite a posicao inicial: "))
        s =  int(input("Digite a posicao final: "))

        v = pow(v0, 2) + 2 * a * (s-s0)
        Vreal = math.sqrt(v)
        print (f"A velocidade final foi de {Vreal} m/s\n")
        

    else:
        print("Por favor digite um valor valido\n")
        continue

    final = int(input("Se deseja continuar pressione 1, se deseja sair digite qualquer valor: "))
    if final == 1:
        opcao == True
        continue
    else:
        opcao == False
        print ("Obrigado pelo teste :D")
        break