import math

#----------------------------------------------------------------------------------------
def Participantes():
    Printar('Participantes do Trabalho')
    Printar(' 202010358711 Sala22 IMECOMPUT Turma 1') #Bruna
    Printar(' 202010056811 Sala22 IMECOMPUT Turma 1') #Newton
    Printar(' 202010397811 Sala22 IMECOMPUT Turma 1') #Andrey
    Printar(' 202010397011 Sala22 IMECOMPUT Turma 1') #Felipe
    Printar(' 202010396711 Sala23 IMECOMPUT Turma 2') #Isabella
    Printar('')
    
#----------------------------------------------------------------------------------------
def Printar(Mensagem):
    print(Mensagem)
    
#----------------------------------------------------------------------------------------
def Float(Fl):
    Fl = float(Fl)
    return Fl

#----------------------------------------------------------------------------------------
def Input(IP):
    Ip = input(IP)
    return Ip
#----------------------------------------------------------------------------------------
def Round(N, Q):
    r = round(N, Q)
    return r

#----------------------------------------------------------------------------------------
def Str(STR):
    P = str(STR)
    return P

#----------------------------------------------------------------------------------------
def Pede_Lado1():
    try:
        a = Float(Input('Qual o valor do lado A do triangulo? '))
        if  a<=0:
            Printar(' O valor deve ser positivo!')
            return Pede_Lado1()
        else:
            return a
    except:
        Printar('Deve ser um número!')
        return Pede_Lado1()
    
#----------------------------------------------------------------------------------------
def Pede_Lado2():
    try:
        b=Float(Input('Qual o valor do lado B do triangulo? '))
        if  b<=0:
            Printar(' O valor deve ser positivo!')
            return Pede_Lado2()
        else:
            return b
    except:
        Printar('Deve ser um número!')
        return Pede_Lado2()

#----------------------------------------------------------------------------------------
def Pede_Angulo1():
    try:
        x=Float(Input('Qual o valor do angulo formado entre os lados A e B do triangulo? '))
        if (x>=180) or (x<=0):
            Printar('O angulo deve ser maior que zero e menor que 180')
            return Pede_Angulo1()
        else:
            return x
    except:
        Printar('Deve ser um número!')
        return Pede_Angulo1()
    
#----------------------------------------------------------------------------------------
def CalcularLado3(a, b, x):
    cosx=math.cos(math.radians(x))
    c=((a**2)+(b**2)-2*a*b*cosx)**0.5
    return c

#----------------------------------------------------------------------------------------
def CalcularAngulo2(a, c, x):
    senx=math.sin(math.radians(x))
    arcsinx=math.asin(senx)
    seny=(a*senx)/c
    arcsiny=math.asin(seny)
    y=math.degrees(arcsiny)
    return y

#----------------------------------------------------------------------------------------
def CalcularAngulo3(x, y):
    z= 180 - (x + y)    
    return z

#----------------------------------------------------------------------------------------
def CalculaAlturaA(b, x):
    senx=math.sin(math.radians(x))
    ha=senx*b
    return ha

#----------------------------------------------------------------------------------------
def CalculaAlturaB(a, c, y, x):
    senx=math.sin(math.radians(x))
    seny=(senx*a)/c
    hb=c*seny
    return hb

#----------------------------------------------------------------------------------------
def CalculaAlturaC(a, b, c, x, y):
    senx=math.sin(math.radians(x))
    seny=(senx*a)/c
    hc=b*seny
    return hc

#----------------------------------------------------------------------------------------
def CalculaArea(a, b, x):
    senx=math.sin(math.radians(x))
    ar=(a*b*senx)/2
    return ar

#----------------------------------------------------------------------------------------
def CalculaPerimetro(a,b,c):
    p=a+b+c
    return p

#----------------------------------------------------------------------------------------
def CheckLados(a, b, c):
    a = Round(a, 2)
    b = Round(b, 2)
    c = Round(c, 2)
    if a==b==c:
        return 'definido como Equilatero'
    elif a!=b!=c:
        return 'definido como Escaleno'
    else:
        return 'definifo como Isoceles'

#----------------------------------------------------------------------------------------
def CheckAng(x, y, z):
    x = Round(x, 2)
    y = Round(y, 2)
    Z = Round(z, 2)
    if x==90 or y==90 or z==90:
        return 'definido como Retângulo'
    elif x>90 or y>90 or y>90:
        return 'definido como Obtusangulo'
    else:
        return 'definido como Acutangulo'

#----------------------------------------------------------------------------------------
def RaioInscrito(Cl, ar, p, ha):
    p = p/2
    r = ar/p
    return r

#----------------------------------------------------------------------------------------
def RaioCircunscrito(a, b, c, p):
    p = p/2
    rci = (a*b*c)/(4*math.sqrt(p*(p-a)*(p-b)*(p-c)))
    return rci

#----------------------------------------------------------------------------------------            
def Resposta(a, b, x, c, y, z, ha , hb, hc, ar, p, Cl, Ca, ri, rci):
    Printar('--------------------------------------------------')
    
    Printar('\nTriangulo ' + Cl + ' e ' +  Ca)

    Printar('\nO valor do lado A é ' + Str(Round(a, 2)))
    Printar('O valor do lado B é ' + Str(Round(b, 2)))
    Printar('O valor do lado C é ' + Str(Round(c, 2)))
    
    Printar('\nO valor do angulo a é ' + Str(Round(x, 2)))
    Printar('O valor do angulo b é ' + Str(Round(y, 2)))      
    Printar('O valor do angulo c é ' + Str(Round(z, 2)))

    Printar('\nO valor da altura A é ' + Str(Round(ha, 2)))
    Printar('O valor da altura B é ' + Str(Round(hb, 2)))
    Printar('O valor da altura C é ' + Str(Round(hc, 2)))

    Printar('\nO valor da area é ' + Str(Round(ar, 2)))
    Printar('O valor do perimetro é ' + Str(Round(p, 2)))
    Printar('O valor do Raio Inscrito é ' + Str(Round(ri, 2)))
    Printar('O valor do Raio Circunscrito é ' + Str(Round(rci, 2)) + '\n')

    
#----------------------------------------------------------------------------------------
def Nova_Execucao():
    n=Input('Nova execução??? Digite s ')
    if n=='S' or n=='s' or n=='Sim' or n=='SIM':
        Printar('Reiniciando\n')
        return Execução()
    else:
        Printar('Termino da execucao')
        return

#----------------------------------------------------------------------------------------
def Execução():
    a   = Float(Pede_Lado1())                        #Lado 1
    b   = Float(Pede_Lado2())                        #Lado 2
    x   = Float(Pede_Angulo1())                      #Angulo 1
    c   = Float(CalcularLado3(a,b,x))                #Lado 3
    y   = Float(CalcularAngulo2(a,c,x))              #Angulo 2
    z   = Float(CalcularAngulo3(x, y))               #Angulo 3
    ha  = Float(CalculaAlturaA(b,x))                 #Altura A
    hb  = Float(CalculaAlturaB(a,c,y,x))             #Altura B
    hc  = Float(CalculaAlturaC(a,b,c,x,y))           #Altura C
    ar  = Float(CalculaArea(a,b,x))                  #Area
    p   = Float(CalculaPerimetro(a,b,c))             #Perimetro
    Cl  = CheckLados(a,b,c)                          #Check dos Lados
    Ca  = CheckAng(x,y,z)                            #Check do Angulo
    ri  = Float(RaioInscrito(Cl, ar, p, ha))         #Raio Inscrito
    rci = Float(RaioCircunscrito(a,b,c,p))           #Raio Circunscrito
    Resposta(a,b,x,c,y,z,ha,hb,hc,ar,p,Cl,Ca,ri,rci) #Resposta
    Nova_Execucao()

#----------------------------------------------------------------------------------------
Participantes()
Execução()
