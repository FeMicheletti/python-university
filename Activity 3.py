#------------------------------------------------------------------------
def apresentacao():
    Printar('Participantes do Trabalho')
    Printar(' 202010358711 Sala22 IMECOMPUT Turma 1') #Bruna
    Printar(' 202010056811 Sala22 IMECOMPUT Turma 1') #Newton
    Printar(' 202010397811 Sala22 IMECOMPUT Turma 1') #Andrey
    Printar(' 202010397011 Sala22 IMECOMPUT Turma 1') #Felipe
    Printar(' 202010396711 Sala23 IMECOMPUT Turma 2') #Isabella
    Printar('')
    
#------------------------------------------------------------------------
def Printar(msm):
    print(msm)

#------------------------------------------------------------------------
def Int(i):
    i = int(i)
    return i

#------------------------------------------------------------------------
def Str(s):
    s = str(s)
    return s

#------------------------------------------------------------------------
def Input(i):
    i = input(i)
    return i

#------------------------------------------------------------------------
def pergunta_numero():
    try:
        x = Int(Input("Informe um número: "))
        if -10<=x<=10:
            return x
        else:
            Printar("entre 10 e -10")
            return pergunta_numero()
    except:
        Printar("Precisa ser um numero \n")
        return pergunta_numero()

#------------------------------------------------------------------------
C=564
def recursiva(r):
    global C
    if C!= r:
        Printar(r)
        C = r
        return r
        

#------------------------------------------------------------------------
def resto(x, y):
    if x >= 0:
        if y > 0:
            if x < y:
                recursiva(x)
                return x
            p = x - y
            if p < 0:
                return x
            recursiva(p)
            return resto(p, y)
        else:
            p = x + y
            if p > 0:
                recursiva(-p)
                return resto(p, y)
            else:
                recursiva(p)
                return p
    else:
        if y > 0:
            p = x + y
            if p >= 0:
                recursiva(p)
                return p
            recursiva(-p)
            return resto(p, y)
        else:
            if y<x:
                recursiva(x)
                return x
            p = x - y
            if p < 0:
                recursiva(p)
                return resto(p, y)
            else:
                recursiva(p)
                return p
            
#------------------------------------------------------------------------
def maior(x, y):
    if modulo(x) > modulo(y):
        return 1
    
#------------------------------------------------------------------------
def produto(x, y):
    if x == 0 or y == 0:
        return recursiva(0)
    if maior(x, y):
        if y > 0:
            return recursiva(x + produto(x, y - 1))
        else:
            return recursiva(-x + produto(x, y + 1))
    else:
        if x > 0:
            return recursiva(y + produto(y, x - 1))
        else:
            return recursiva(-y + produto(y, x + 1))

#------------------------------------------------------------------------
def quociente(x,y):
    if y < 0:
        y = -y
        x = -x
    if x < 0 or y < 0:
        return recursiva(quociente(x + y, y) - 1)
    if x >= y:
        return recursiva(quociente(x - y, y) + 1)
    return 0

#------------------------------------------------------------------------
def modulo(m):
    if m < 0:
        return -m
    return m
            
#------------------------------------------------------------------------
def pergunta():
    o = Str(Input("Digite 'p' para Produto, 'Q' para Quociente, 'R' para resto ou clique qualquer letra para tudo: "))
    return o

#------------------------------------------------------------------------
def main():
    x = pergunta_numero()
    y = pergunta_numero()
    global C
    C=564
    
    if y==0:
        Printar("\nNão pode ser 0\n")
        return main()
    
    o = pergunta()
    
    if o=="p" or o=="P":
        Printar("\nProduto:")
        p = produto(x, y)
        
    elif o=="q" or o=="Q":
        Printar("\nQuociente:")
        q = quociente(x, y)
        if Int(q)==0:
            Printar(Int(q))
            
    elif o=="r" or o=="R":
        Printar("\nResto:")
        r = resto(x, y)
        if Int(x)==0:
            Printar(Int(x))
            
    else:
        Printar("\nProduto:")
        p = produto(x, y)
        
        Printar("\nQuociente:")
        q = quociente(x, y)
        if Int(q)==0:
            Printar(Int(q))
        Printar("\nResto:")
        r = resto(x, y)
        if Int(x)==0:
            Printar(Int(x))
    res = Input("\nDeseja executar denovo? S ou s: ")
    if res=='S' or res=='s':
        return main()
    else:
        return
    
#------------------------------------------------------------------------    
apresentacao()
main()
