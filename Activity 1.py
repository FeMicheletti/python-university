import math

t=0 #Valor para inicialização
h=0 #hipotenusa OK
b=0 #Base OK
p=0 #Lado Perpendicular OK
x=0 #angulo 1 OK
y=0 #angulo 2 OK
z=0 #angulo 3
pm=0 #Perimetro do Triangulo
ha=0 #Altura
A=0 #AREA
ci=0 #Raio do circulo inscrito
cci=0 #Raio do circulo cincunscrito

while True:
    
    if t==0:
            print('Trabalho feito por: 202010397011')
            print('')
            t = t+1

    
    try:
        if b==0: #IF INICIAL
            b=float(input('Digite o valor da Base do triangulo: '))

            if b<=0:
                print('o valor da base não pode ser negativa')
                continue
            else: #ELSE 1
                x=float(input('Digite o valor do angulo formado com a Base e a Hipotenusa: '))
                if x<=0:
                    print('O valor do angulo não pode ser negativo')
                    continue
                else: #ELSE 2
                    y = 90.0
                    cosX = math.cos(math.radians(x))
                    h = b/cosX
                    if h<=0:
                        print('Algo deu errado')
                        continue
                    else: #ELSE 3
                        p = math.sqrt(h*h-b*b)
                        if p<=0:
                            print('Algo deu errado')
                            continue
                        else: #ELSE 4
                            senZ = b/h
                            arcsen = math.asin(senZ)
                            z = math.degrees(arcsen)
                            pm = b+h+p
                            ha = p*b/h
                            A = (h*ha)/2
                            ci = (b+p-h)/2
                            cci = h/2
                            
                            A = round(A, 2)
                            cci = round(cci, 2)
                            ci = round(ci, 2)
                            ha = round(ha, 2)
                            pm = round(pm, 2)
                            z = round(z,2)
                            x=round(x,2)
                            b=round(b,2)
                            h = round(h, 2)
                            p = round(p, 2)
                            print('')
                            print('Resultado: ')
                            print('Hipotenusa: ' + str(h))
                            print('Base: ' + str(b))
                            print('Lado Perpendicular: ' + str(p))
                            print('Angulo da Base com a Hipotenusa: ' + str(x))
                            print('Angulo Reto: ' + str(y))
                            print('Angulo Do Lado Perpendicular com a Hipotenusa: ' + str(z))
                            print('    ')
                            print('EXTRA')
                            print('Perimetro: ' + str(pm))
                            print('Altura: ' + str(ha))
                            print('Area: ' + str(A))
                            print('Raio do Circulo Inscrito: ' + str(ci))
                            print('Raio do Circulo Circunscrito: ' + str(cci))
                            print(' ')                           
                            print('Deseja Fazer uma nova repetição? (Digite S para sim e N para não)')
                            quest=input('')
                            
                            if quest=='S' or quest=='s' or quest=='Sim' or quest=='SIM':
                                h=0
                                b=0
                                p=0
                                x=0
                                y=0
                                z=0
                                pm=0
                                ha=0
                                A2=0
                                ci=0
                                print('')
                                continue
                            else:
                                break
                            continue #ELSE 4
                        continue #ELSE 3
                    continue #ELSE 2
                continue #ELSE 1
            continue #IF INICIAL
        
        else: #ELSE 5
            x=float(input('Digite o valor do angulo formado com a Base e a Hipotenusa: '))
            if x<=0:
                print('O valor do angulo não pode ser negativo')
                continue
            else:#ELSE 6
                y = 90.0
                cosX = math.cos(math.radians(x))
                h = b/cosX
                if h<=0:
                    print('Algo deu errado')
                    continue
                else: #ELSE 7
                    p = math.sqrt(h*h-b*b)
                    if p<=0:
                        print('Algo deu errado')
                        continue
                    else: #ELSE 8
                        senZ = b/h
                        arcsen = math.asin(senZ)
                        z = math.degrees(arcsen)
                        pm = b+h+p
                        ha = p*b/h
                        A = (h*ha)/2
                        ci = (b+p-h)/2
                        cii = h/2
                        
                        cci = round(cci, 2)
                        A2 = round(A, 2)
                        ci = round(ci, 2)
                        ha = round(ha, 2)
                        pm = round(pm, 2)
                        z = round(z,2)
                        x=round(x,2)
                        b=round(b,2)
                        h = round(h, 2)
                        p = round(p, 2)
                        print('')
                        print('Resultado: ')
                        print('Hipotenusa: ' + str(h))
                        print('Base: ' + str(b))
                        print('Lado Perpendicular: ' + str(p))
                        print('Angulo da Base com a Hipotenusa: ' + str(x))
                        print('Angulo Reto: ' + str(y))
                        print('Angulo Do Lado Perpendicular com a Hipotenusa: ' + str(z))
                        print('    ')
                        print('EXTRA')
                        print('Perimetro: ' + str(pm))
                        print('Altura: ' + str(ha))
                        print('Area: ' + str(A))
                        print('Raio do Circulo Inscrito: ' + str(ci))
                        print('Raio do Circulo Circunscrito: ' + str(cci))
                        print(' ')
                        print('Deseja Fazer uma nova repetição? (Digite S para sim e N para não)')
                        quest=input('')
                        if quest=='S' or quest=='s' or quest=='Sim' or quest=='SIM':
                            h=0
                            b=0
                            p=0
                            x=0
                            y=0
                            z=0
                            pm=0
                            ha=0
                            A2=0
                            ci=0
                            print('')
                            continue
                        else:
                            break
                        continue #ELSE 8
                    continue #ELSE 7
                continue #ELSE 6
            continue #ELSE 5
            
    except:
        print('Digite um valor valido')
