from math import inf as infinity
from random import choice
import time

H = -1
C = +1
b = [  [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]  ]

#-------------------------------------------------------------------------------
def Printar(msm):
    print(msm)

#-------------------------------------------------------------------------------
def Input(I):
    i = input(I)
    return i

#-------------------------------------------------------------------------------
def Int(i):
    i = int(i)
    return i

#-------------------------------------------------------------------------------
def Exit():
    exit()

#-------------------------------------------------------------------------------
def Len(l):
    l = len(l)
    return l   

#-------------------------------------------------------------------------------
def apresentacao():
    Printar('Participantes do Trabalho')
    Printar(' 202010358711 Sala22 IMECOMPUT Turma 1') #Bruna
    Printar(' 202010056811 Sala22 IMECOMPUT Turma 1') #Newton
    Printar(' 202010397811 Sala22 IMECOMPUT Turma 1') #Andrey
    Printar(' 202010397011 Sala22 IMECOMPUT Turma 1') #Felipe
    Printar(' 202010396711 Sala23 IMECOMPUT Turma 2') #Isabella
    Printar('')

#-------------------------------------------------------------------------------
def primeiro(f):
    try:
        f = Input('Você deseja ser o primeiro a jogar?[s/n]: ')
        if f=='S' or f=='s':
            return "S"
        elif f=='N' or f=='n':
            return "N"
        else:
            Printar("Tente denovo")
            primeiro(f)
    except:
        primeiro(f)

#-------------------------------------------------------------------------------
def avaliar(estado):
    if vitoria(estado, C):
        pontuação = +1
    elif vitoria(estado, H):
        pontuação = -1
    else:
        pontuação = 0
    return pontuação

#-------------------------------------------------------------------------------
def vitoria(estado, j):
    estado_vitoria = [  [estado[0][0], estado[0][1], estado[0][2]],
                        [estado[1][0], estado[1][1], estado[1][2]],
                        [estado[2][0], estado[2][1], estado[2][2]],
                        [estado[0][0], estado[1][0], estado[2][0]],
                        [estado[0][1], estado[1][1], estado[2][1]],
                        [estado[0][2], estado[1][2], estado[2][2]],
                        [estado[0][0], estado[1][1], estado[2][2]],
                        [estado[2][0], estado[1][1], estado[0][2]]  ]
    if [j, j, j] in estado_vitoria:
        return True
    else:
        return False

#-------------------------------------------------------------------------------
def game_over(estado):
    return vitoria(estado, H) or vitoria(estado, C)

#-------------------------------------------------------------------------------
def vazio(estado):
    cells = []
    def f(x, estado, n):
        if n < 1:
            return 0
        r = estado[x]
        g(x, 0, r, Len(r))
        return f(x+1, estado, n-1)
    def g(x, y, r, n):
        if n < 1:
            return 0
        cell = r[y]
        if cell == 0:
            cells.append([x, y])
        return g(x, y+1, r, n-1)
    f(0, estado, Len(estado))
    return cells

#-------------------------------------------------------------------------------
def validar(x, y):
    if [x, y] in vazio(b):
        return True
    else:
        return False

#-------------------------------------------------------------------------------
def setar(x, y, j):
    if validar(x, y):
        b[x][y] = j
        return True
    else:
        return False
    
#-------------------------------------------------------------------------------
def maxm(estado, d, j):
    def f(d, j, estado, best, cells, n, i):
        if n < 1:
            return best
        cell = cells[i]
        return f(d, j, estado, melhor(d, j, estado, best, cell), cells, n - 1, i + 1)
    if j == C:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    if d == 0 or game_over(estado):
        pontuação = avaliar(estado)
        return [-1, -1, pontuação]
    cells = vazio(estado)
    best = f(d, j, estado, best, cells, Len(cells), 0)
    return best

#-------------------------------------------------------------------------------
def melhor(d, j, estado, best, cell):
    x, y = cell[0], cell[1]
    estado[x][y] = j
    pontuação = maxm(estado, d - 1, -j)
    estado[x][y] = 0
    pontuação[0], pontuação[1] = x, y
    if j == C:
        if pontuação[2] > best[2]:
            best = pontuação 
    else:
        if pontuação[2] < best[2]:
            best = pontuação 
    return best

#-------------------------------------------------------------------------------
def g(r, n, i, chars):
        if n < 1:
            return 0
        cell = r[i]
        symbol = chars[cell]
        print(f'| {symbol} |', end='')
        return g(r, n-1, i+1, chars)

#-------------------------------------------------------------------------------
def f(estado, n, i, count, chars, line):
    if n < 1:
        return 0
    r = estado[i]
    g(r, Len(r), 0, chars)
    Printar('\n' + line)
    return f(estado, n-1, i+1, count+3, chars, line)

#-------------------------------------------------------------------------------
def renderizar(estado, c, h):
    chars = { -1: h, +1: c, 0: ' ' }
    str_line = '---------------'
    Printar('\n' + "Tabuleiro Atual\n" + str_line)
    f(estado, Len(estado), 0, 1, chars, str_line)
    Printar('\n')
    
#-------------------------------------------------------------------------------
def IA(c, h):
    d = Len(vazio(b))
    if d==0 or game_over(b):
        return
    Printar('Vez do Computador [O]')
    renderizar(b, c, h)
    if d == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = maxm(b, d, C)
        x, y = move[0], move[1]
    setar(x, y, C)
    time.sleep(1)

#-------------------------------------------------------------------------------
def usuario(c, h):
    d = Len(vazio(b))
    if d == 0 or game_over(b):
        return
    move = -1
    moves = {  7: [0, 0], 8: [0, 1], 9: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               1: [2, 0], 2: [2, 1], 3: [2, 2]  }
    Printar('Sua vez [X]')
    renderizar(b, c, h)
    Printar("Posições:")
    Printar("---------------")
    Printar("| 7 || 8 || 9 |")
    Printar("---------------")
    Printar("| 4 || 5 || 6 |")
    Printar("---------------")
    Printar("| 1 || 2 || 3 |")
    Printar("---------------")
    loop(move, moves)

#-------------------------------------------------------------------------------
def loop(move, moves):
    if move < 1 or move > 9:
        try:
            move = Int(Input('Escolha um numero entre o Tabuleiro das Posições: '))
            coord = moves[move]
            can_move = setar(coord[0], coord[1], H)

            if not can_move:
                Printar('Numero usado ou Fora do Tabuleiro')
                move = -1
        except:
            Printar("Algo deu errado")
        loop(move, moves)

#-------------------------------------------------------------------------------
def principal():
    global H, C, b
    h = 'X'
    c = 'O'
    f = 'S'
    game(c, f, h)
    if vitoria(b, H):
        Printar('É sua vez [X]')
        renderizar(b, c, h)
        Printar('VOCÊ GANHOU!')
    elif vitoria(b, C):
        Printar('Vez do Computador [O]')
        renderizar(b, c, h)
        Printar('VOCÊ PERDEU!')
    else:
        renderizar(b, c, h)
        Printar('DEU VELHA!')
    r = Input("\nDeseja jogar novamente? S ou s ")
    if r=='S' or r=='s':
        b = [  [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]  ]
        Printar("\n")
        principal()
    else:
        return
#-------------------------------------------------------------------------------
def game(c, f, h):
    if Len(vazio(b)) > 0 and not game_over(b):
        usuario(c, h)
        IA(c, h)
        game(c, f, h)
#-------------------------------------------------------------------------------
apresentacao()
principal()
