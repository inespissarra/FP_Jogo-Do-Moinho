#99236 Ines Pissarra

# TAD posicao:

# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

# Representacao Interna: tuplo, cujo o primeiro elemento corresponde
# a letra da coluna, e o segundo elemento corresponde ao numero da linha
# (coluna, linha)

#-------------------------------------
def valida_posicao(c, l):
    # valida_posicao: str x str -> booleano
    '''A funcao recebe duas cadeias de caracteres, c (coluna) e l (linha). 
    Devolve True caso os argumentos sejam validos e False caso contrario.'''    
    return type(c)==str and type(l)==str and c in 'abc' and l in '123' \
       and len(c)==1 and len(l)==1
#-------------------------------------

# Construtores:
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    '''A funcao recebe duas cadeias de caracteres, c (coluna) e l (linha). 
    Devolve a posicao correspondente.'''
    if valida_posicao(c, l):
        return (c, l)
    else:
        raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(p):
    # cria_copia_posicao: posicao -> posicao
    '''A funcao recebe uma posicao, p, e devolve uma copia nova da posicao.'''
    if eh_posicao(p):
        return (p[0], p[1])
    else:
        raise ValueError('cria_copia_posicao: argumento invalido')


# Seletores:
def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    '''A funcao recebe uma posicao, p, e devolve a componente coluna, c.'''    
    return p[0]

def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    '''A funcao recebe uma posicao, p, e devolve a componente linha, l.''' 
    return p[1]


# Reconhecedor:
def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    '''A funcao devolve True se o seu argumento for TAD posicao \
e False caso contrario.'''
    return type(arg)==tuple and len(arg)==2 and valida_posicao(arg[0], arg[1])


# Teste
def posicoes_iguais(p1, p2):
    # posicoes_iguais: posicao x posicao -> booleano
    '''A funcao devolve True se p1 e p2 sao posicoes e sao iguais.'''
    # se p1 for posicao e for igual a p2, entao p2 e posicao
    return eh_posicao(p1) and p1 == p2


# Transformador
def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    '''A funcao recebe uma posicao, p, e devolve a cadeia de caracteres 'cl' \
que representa o seu argumento.
Os valores c e l sao as componentes coluna e linha de p.'''
    return obter_pos_c(p) + obter_pos_l(p)

#-------------------------------------
# Funcao de alto nivel:

def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    '''A funcao recebe uma posicao, p, e devolve um tuplo com as posicoes \
adjacentes a p.'''
    adj = ()
    c, l = obter_pos_c(p), obter_pos_l(p)
    c_adj, l_adj = [chr(ord(c)-1), chr(ord(c)+1)], \
        [chr(ord(l)-1), chr(ord(l)+1)]
    # lateral = True se a posicao p for uma lateral
    lateral = posicoes_iguais(p, cria_posicao('a','2')) \
        or posicoes_iguais(p, cria_posicao('b', '1')) \
        or posicoes_iguais(p, cria_posicao('b', '3')) \
        or posicoes_iguais(p, cria_posicao('c', '2')) 
    # se p for uma lateral entao nao devolve as diagonais
    if valida_posicao(c_adj[0], l_adj[0]) and not lateral:  # diagonal esq. sup.
        adj = adj + (cria_posicao(c_adj[0], l_adj[0]),)
    if valida_posicao(c, l_adj[0]):                         # cima
        adj = adj + (cria_posicao(c, l_adj[0]),)    
    if valida_posicao(c_adj[1], l_adj[0]) and not lateral:  # diagonal dir. sup.
        adj = adj + (cria_posicao(c_adj[1], l_adj[0]),)
    if valida_posicao(c_adj[0], l):                         # esquerda
        adj = adj + (cria_posicao(c_adj[0], l),)
    if valida_posicao(c_adj[1], l):                         # direita
        adj = adj + (cria_posicao(c_adj[1], l),)
    if valida_posicao(c_adj[0], l_adj[1]) and not lateral:  # diagonal esq. inf.
        adj = adj + (cria_posicao(c_adj[0], l_adj[1]),)
    if valida_posicao(c, l_adj[1]):                         # baixo
        adj = adj + (cria_posicao(c, l_adj[1]),)
    if valida_posicao(c_adj[1], l_adj[1]) and not lateral:  # diagonal dir. inf.
        adj = adj + (cria_posicao(c_adj[1], l_adj[1]),)      
    return adj


#-------------------------------------------------------------------------------

# TAD peca:

# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str

# Representacao Interna: lista, com um elemento str que representa um jogador
# [jogador]

#-------------------------------------
def valida_peca(s):
    # valida_peca: str -> booleano
    '''A funcao recebe uma cadeia de caracteres, s, e devolve True caso o \
argumento sejam valido, False caso contrario.'''
    return type(s)==str and s in 'X O' and len(s)==1    
#-------------------------------------

# Construtores:
def cria_peca(s):
    # cria_peca: str -> peca
    '''A funcao recebe uma cadeia de caracteres, s ('X', 'O' ou ' '), \
e devolve a peca correspondente.'''
    if valida_peca(s):
        return [s]
    else:
        raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
    # cria_copia_peca: peca -> peca
    '''A funcao recebe uma peca, j, e devolve uma copia nova da peca.'''  
    if eh_peca(j):
        return [j[0]]
    else:
        raise ValueError('cria_copia_peca: argumento invalido')


# Reconhecedor:
def eh_peca(arg):
    # eh_peca: universal -> booleano
    '''A funcao devolve True se o seu argumento for TAD peca \
e False caso contrario.'''
    return type(arg)==list and len(arg)==1 and valida_peca(arg[0])


# Teste:
def pecas_iguais(j1, j2):
    # pecas_iguais: peca x peca -> booleano
    '''A funcao recebe duas pecas, j1 e j2, e devolve True se as pecas forem \
iguais, False caso contrario.'''
    # se j1 for peca e for igual a j2, entao j2 e peca
    return eh_peca(j1) and j1 == j2


# Transformador:
def peca_para_str(j):
    # peca_para_str: peca -> str
    '''A funcao recebe uma peca, j, e devolve a cadeia de caracteres que \
representa o jogador dono da peca.'''
    return '[' + j[0] + ']'

#-------------------------------------
# Funcao de alto nivel:

def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> N
    ''' A funcao recebe uma peca, j, e devolve um inteiro 1, -1 ou 0 \
dependendo se a peca e do jogador 'X', 'O' ou livre.'''
    pecas, valor = 'O X', -1
    for i in pecas:
        if pecas_iguais(cria_peca(i), j):
            return valor
        valor = valor + 1
        
        
#-------------------------------------------------------------------------------

# TAD tabuleiro:

# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro

# Representacao Interna: lista de tres listas (cada uma com tres pecas)
# [[peca, peca, peca], [peca, peca, peca], [peca, peca, peca]]

# Construtores:
def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    '''A funcao devolve um tabuleiro de jogo do moinho 3x3 \
sem posicoes ocupadas por pecas de jogador.'''
    x = cria_peca(' ')
    return [[x,x,x],[x,x,x],[x,x,x]]

def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    '''A funcao recebe um tabuleiro, t, e devolve uma copia nova de t.'''
    if eh_tabuleiro(t):
        return [[t[0][0], t[0][1], t[0][2]], [t[1][0], t[1][1], t[1][2]],\
            [t[2][0], t[2][1], t[2][2]]]
    else:
        raise ValueError('cria_copia_tabuleiro: argumento invalido')
    

# Seletores
def obter_peca(t, p):
    # obter_peca: tabuleiro x posicao -> peca
    '''A funcao recebe um tabuleiro, t, e uma posicao, p, e devolve a peca \
que se encontra nessa posicao do tabuleiro.'''
    # int(1) = 1, ord('a') = 97
    # para obter os indices do tabuleiro, tem que se subtrair esses valores.
    return t[int(obter_pos_l(p))-1][ord(obter_pos_c(p))-97]

def obter_vetor(t, s):
    # obter_vetor: tabuleiro x str -> tuplo de pecas
    '''A funcao recebe um tabuleiro, t, uma linha ou coluna, s, e devolve \
um tuplo com as pecas de s.'''
    vetor = ()
    if s in '123':
        for c in 'abc':
            vetor = vetor + (obter_peca(t, cria_posicao(c, s)),)
    else:
        for l in '123':
            vetor = vetor + (obter_peca(t, cria_posicao(s, l)),)
    return vetor


# Modificadores:
def coloca_peca(t, j, p):
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    '''A funcao recebe um tabuleiro, t, uma peca, j, e uma posicao, p, \
e devolve o tabuleiro com a peca na posicao pedida.'''
    t[int(obter_pos_l(p))-1][ord(obter_pos_c(p))-97] = j
    return t

def remove_peca(t, p):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    '''A funcao recebe um tabuleiro, t, e uma posicao, p, e devolve o tabuleiro\
 resultante da remocao da peca existente na posicao pedida.'''
    return coloca_peca(t, cria_peca(' '), p)

def move_peca(t, p1, p2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    '''A funcao modifica o tabuleiro, t, movendo a peca da primeira \
posicao, p1, para a segunda posicao, p2.'''
    if not posicoes_iguais(p1, p2):
        coloca_peca(t, obter_peca(t, p1), p2)
        remove_peca(t, p1)
    return t


# Reconhecedores:
def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    '''A funcao devolve True se o seu argumento for TAD tabuleiro \
e False caso contrario.'''
    if type(arg)==list and len(arg)== 3 and \
       (type(arg[l])==list and len(arg[l]) == 3 for l in range(3)) \
       and (eh_peca(arg[l][c]) for c in range(3)):
        X, O, winner = 0, 0, 0
        for l in range(3):
            if pecas_iguais(arg[l][0], arg[l][1]) and \
               pecas_iguais(arg[l][1],arg[l][2]) and not \
               pecas_iguais(arg[l][2], cria_peca(' ')):
                winner = winner + 1
            for c in range(3):
                if pecas_iguais(arg[l][c], cria_peca('X')):
                    X = X + 1 
                if pecas_iguais(arg[l][c], cria_peca('O')):
                    O = O + 1
        for c in range(3):
            if pecas_iguais(arg[0][c], arg[1][c]) and \
               pecas_iguais(arg[1][c], arg[2][c]) and not \
               pecas_iguais(arg[2][c], cria_peca(' ')):
                winner = winner + 1
        return abs(X-O) <= 1 and X<=3 and O<=3 and winner <= 1
    else:
        return False

def eh_posicao_livre(t, p):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    '''A funcao recebe um tabuleiro, t, e uma posicao, p, e devolve True \
apenas se essa posicao nesse tabuleiro estiver livre.'''
    return pecas_iguais(cria_peca(' '), obter_peca(t, p))


# Teste
def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    '''A funcao recebe dois tabuleiros, t1 e t2, e devolve True se os \
tabuleiros forem iguais, False caso contrario.'''
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        # para manter a abstracao e necessario verificar a igualdade 
        # entre as pecas com a funcao pecas_iguais()
        for l in '123':
            for c in 'abc':
                p = cria_posicao(c, l)
                if not pecas_iguais(obter_peca(t1, p), obter_peca(t2, p)):
                    return False
        return True
    return False


# Transformadores
def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    '''A funcao recebe um tabuleiro, t, e devolve-o no formato tradicional'''
    tab_str = '   a   b   c\n1 '
    for l in '123':
        if l == '2':
            tab_str = tab_str + '\n   | \\ | / |\n' + l + ' '
        if l == '3':
            tab_str = tab_str + '\n   | / | \\ |\n' + l + ' '
        for c in 'abc':
            if c != 'a':
                tab_str = tab_str + '-'            
            tab_str = tab_str + peca_para_str(obter_peca(t, cria_posicao(c, l)))
    return tab_str

def tuplo_para_tabuleiro(t):
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    '''A funcao recebe um tuplo, t, e devolve o tabuleiro representado \
por esse tuplo.'''
    tab = cria_tabuleiro()
    for l in range(3):
        for c in range(3):
            if t[l][c] == 0:
                x = ' '
            elif t[l][c] == -1:
                x = 'O'
            elif t[l][c] == 1:
                x = 'X' 
            tab[l][c] = cria_peca(x)
    return tab

#-------------------------------------
# Funcoes de alto nivel:

def obter_ganhador(t):
    # obter_ganhador: tabuleiro -> peca
    '''A funcao recebe um tabuleiro, t, e devolve a peca do jogador que tiver \
3 pecas em linha horizontal ou vertical.
(no caso de ainda nenhum jogador ter ganho, a funcao devolve uma peca livre)'''
    for c in 'abc':
        coluna = obter_vetor(t, c)
        if pecas_iguais(coluna[0], coluna[1]) and \
           pecas_iguais(coluna[1], coluna[2]) and not \
           pecas_iguais(coluna[2], cria_peca(' ')):
            return coluna[0]
    for l in '123':
        linha = obter_vetor(t, l) 
        if pecas_iguais(linha[0], linha[1]) and \
           pecas_iguais(linha[1], linha[2]) and not \
           pecas_iguais(linha[2], cria_peca(' ')):
            return linha[0]
    return cria_peca(' ')

def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    '''A funcao recebe um tabuleiro, t, e devolve um tuplo com todas as \
posicoes livres nesse tabuleiro'''
    livres = ()
    for l in '123':
        for c in 'abc':
            if eh_posicao_livre(t, cria_posicao(c, l)):
                livres = livres + (cria_posicao(c, l),)
    return livres

def obter_posicoes_jogador(t, j):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    '''A funcao recebe um tabuleiro, t, e uma peca, j, e devolve um tuplo de \
todas as posicoes com essa peca nesse tabuleiro'''
    pos_jogador = ()
    for l in '123':
        for c in 'abc':
            if pecas_iguais(obter_peca(t, cria_posicao(c, l)), j):
                pos_jogador = pos_jogador + (cria_posicao(c, l),)
    return pos_jogador


#-------------------------------------------------------------------------------
# Funcoes Adicionais:

def obter_movimento_manual(t, j):
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    '''A funcao recebe um tabuleiro, t, e uma peca, j, e realiza a leitura da \
posicao introduzida manualmente pelo jogador.
Retorna um tuplo com uma posicao caso o jogo se encontre na fase de colocacao,
ou um tuplo com a posicao de origem e a posicao de destino, \
caso o jogo se encontre na fase de movimento.'''
    pos_jogador = obter_posicoes_jogador(t, j)
    if len(pos_jogador) < 3:                                # fase de colocacao
        p = input('Turno do jogador. Escolha uma posicao: ')
        if len(p)==2 and valida_posicao(p[0], p[1]) and \
           eh_posicao_livre(t, cria_posicao(p[0], p[1])):
            return (cria_posicao(p[0], p[1]),)
    else:                                                   # fase de movimento
        p = input('Turno do jogador. Escolha um movimento: ')
        if len(p)==4 and \
           valida_posicao(p[0], p[1]) and valida_posicao(p[2], p[3]):
            
            posicoes_adj_livres = False
            for p1 in pos_jogador:
                for p2 in obter_posicoes_adjacentes(p1):
                    if eh_posicao_livre(t, p2):
                        posicoes_adj_livres = True
            # posicoes_adj_livres = True se existirem posicoes adjacentes livres
                    
            p1, p2 = cria_posicao(p[0], p[1]), cria_posicao(p[2], p[3])
            
            eh_adjacente = False
            for adj in obter_posicoes_adjacentes(p1):
                if posicoes_iguais(adj, p2):
                    eh_adjacente = True
            # eh_adjacente = True se p2 for uma posicao adjacente a p1
            
            if pecas_iguais(obter_peca(t, p1), j) and \
               ((eh_posicao_livre(t, p2) and eh_adjacente) \
                or (not posicoes_adj_livres and posicoes_iguais(p1, p2))):
                return (p1, p2)
    raise ValueError('obter_movimento_manual: escolha invalida')


def obter_movimento_auto(t, j, nivel):
    # obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    '''A funcao recebe um tabuleiro, t, uma peca, j, e uma cadeia de caracteres\
, nivel (de dificuldade do jogo). \nRetorna um tuplo com uma posicao \
caso o jogo se encontre na fase de colocacao,\nou um tuplo com a posicao de \
origem e a posicao de destino, caso o jogo se encontre na fase de movimento.'''
    pos_jogador, livres = obter_posicoes_jogador(t, j), obter_posicoes_livres(t)
    if len(pos_jogador) < 3:                                # fase de colocacao
        # vitoria - testar se uma das posicoes livres faz do jogador ganhador
        for p in livres:
            if pecas_iguais(obter_ganhador(coloca_peca(\
                cria_copia_tabuleiro(t), j, p)), j):
                return (p,)
        if pecas_iguais(j, cria_peca('X')):
            adv = cria_peca('O')
        else:
            adv = cria_peca('X')
        #bloqueio - testar se uma das posicoes livres faz do adversario ganhador
        for p in livres:
            if pecas_iguais(obter_ganhador(coloca_peca(\
                cria_copia_tabuleiro(t),adv, p)), adv):
                return (p,)
        centro = cria_posicao('b','2')
        if eh_posicao_livre(t, centro):               # centro vazio
            return (centro,)     
        for p in (cria_posicao('a','1'), cria_posicao('c', '1'), \
                  cria_posicao('a', '3'), cria_posicao('c', '3')):
            if eh_posicao_livre(t, p):                # canto vazio
                return (p,)  
        for p in (cria_posicao('a','2'), cria_posicao('b', '1'), \
                  cria_posicao('b', '3'), cria_posicao('c', '2')):
            if eh_posicao_livre(t, p):                # lateral vazio
                return (p,)
    else:                                                   # fase de movimento
        if nivel == 'facil':
            for p1 in pos_jogador:
                for p2 in obter_posicoes_adjacentes(p1):
                    if eh_posicao_livre(t, p2):
                        return (p1, p2)
            # todas as jogadas bloqueadas -> posicao da primeira peca duas vezes
            return (pos_jogador[0], pos_jogador[0])
        elif nivel == 'normal':
            vencedor, movimento = minimax(t, j, 1, ())
        else: # nivel == 'dificil'
            vencedor, movimento = minimax(t, j, 5, ())
        return (movimento[0], movimento[1]) # retorno do nivel normal ou dificil

         
def minimax(t, j, profundidade, seq_movimentos):
    # minimax:tabuleiro x peca x int x tuplo de posicoes->int, tuplo de posicoes
    '''A funcao recebe um tabuleiro, uma peca, um inteiro \
(que corresponde a profundidade maxima de recursao), 
e um tuplo de posicoes/vazio (que corresponde a sequencia de movimentos).
Devolve um inteiro e um tuplo de posicoes, que correspondem, respetivamente,
ao melhor resultado e melhor movimento para o jogador do turno atual.'''
    # acaba a recursao se houver um vencedor ou a prfundidade chegar a zero
    if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(t)), seq_movimentos
    else:
        if pecas_iguais(j, cria_peca('X')):
            adv = cria_peca('O')
        else:
            adv = cria_peca('X')  
            
        melhor_resultado = peca_para_inteiro(adv) # pior dos casos
        melhor_seq_movimentos = ()
        
        for p1 in obter_posicoes_jogador(t, j):
            for p2 in obter_posicoes_adjacentes(p1):
                if eh_posicao_livre(t, p2):
                    # tabuleiro com esse movimento
                    novo_tabuleiro = \
                        move_peca(cria_copia_tabuleiro(t), p1, p2)
                    novo_movimento = (p1, p2)
                    # obter o novo resultado e nova sequencia de movimentos
                    # usando a recursividade
                    novo_resultado, nova_seq_movimentos = \
                        minimax(novo_tabuleiro, adv, profundidade-1, \
                                seq_movimentos + novo_movimento)
                    # se o novo resultado for mais favoravel que o anterior,
                    # ou ainda nao houver melhor sequencia de movimentos,
                    # entao, substituir o melhor resultado pelo novo
                    # e a melhor sequencia de movimentos pela nova
                    if (melhor_seq_movimentos == ()) \
                       or (pecas_iguais(j, cria_peca('X')) \
                           and novo_resultado > melhor_resultado) \
                       or (pecas_iguais(j, cria_peca('O')) \
                           and novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos
        # retornar o resultado e sequencia de movimentos mais favoravel 
        return melhor_resultado, melhor_seq_movimentos
    
    
def moinho(jogador, nivel):
    # str x str -> str
    '''Esta e a funcao principal que permite o utilizador jogar com o computador
    Recebe um jogador '[X]' ou '[O]' (a escolha do utilizador) \
e o nivel de dificuldade ('facil', 'normal' ou 'dificil')'''
    if jogador not in ('[O]','[X]') or \
       nivel not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')  
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + nivel + '.')
    t, j = cria_tabuleiro(), cria_peca(jogador[1])
    print(tabuleiro_para_str(t)) 
    if pecas_iguais(j, cria_peca('X')):
        p = obter_movimento_manual(t, j)                 # TURNO DO JOGADOR
        # Como este e o primeiro turno nao e necessario verificar a fase do jogo
        coloca_peca(t, j, p[0])
        print(tabuleiro_para_str(t))
        adv = cria_peca('O')
    else:
        adv = cria_peca('X')
    while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
        # repetir o ciclo enquanto ainda nao ha ganhador
        print ('Turno do computador (' + nivel +'):')    # TURNO DO COMPUTADOR
        p = obter_movimento_auto(t, adv, nivel)
        if len(p)==1:
            coloca_peca(t, adv, p[0])  
        else:
            move_peca(t, p[0], p[1])
        print(tabuleiro_para_str(t))
        # e necessario verificar se ainda nao existe vencedor
        if pecas_iguais(obter_ganhador(t), cria_peca(' ')):
            p = obter_movimento_manual(t, j)             # TURNO DO JOGADOR
            if len(p)==1:
                coloca_peca(t, j, p[0])
            else:
                move_peca(t, p[0], p[1])
            print(tabuleiro_para_str(t))
    return peca_para_str(obter_ganhador(t))