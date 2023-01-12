import random

#def = define uma funcao
def find_pacman(map):
    pacman_x = -1  #eixo x com uma posição q n existe
    pacman_y = -1  #eixo y

    # len(map) = retorna o numero de linhas do map
    # len(map[x]) = retorna o numero de colunas de cada linha (x)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "@":
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y

def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)
    # "....@...." separar a string .... + @ + .... Trocar o @ por um . pq o pacman andou
    #o caminho onde o pacman estava é vazio agora
    
    everything_to_the_left = map[pacman_x][0:pacman_y]
    everything_to_the_right = map[pacman_x][pacman_y+1:]
    
    map[pacman_x] = everything_to_the_left+ "." + everything_to_the_right

    #a nova posição do pacman
    everything_to_the_left = map[next_pacman_x][0:next_pacman_y] 
    everything_to_the_right = map[next_pacman_x][next_pacman_y+1:]
    map[next_pacman_x] = everything_to_the_left + "@" + everything_to_the_right

#a funcao retorna tres booleans
#o primeiro indica se o botao apertado e valido
#o segundo indica se o pacman esta vivo
#o terceiro indica se ganhou o jogo
def play(map, key):
    next_x, next_y = new_position(map, key)

    #checa se a posicao e invalida
    if invalid_key(next_x, next_y):
        return False, True, False
    
    #checa se nao esta dentro das bordas do mapa
    if not within_borders(map, next_x, next_y):
        return False, True, False
    
    #se e uma parede  
    if is_a_wall(map, next_x, next_y):
        return False, True, False
    
    #se e um fantasma
    is_a_ghost = map[next_x][next_y] == "G"
    if is_a_ghost:
        return True, False, False
    
    move_pacman(map, next_x, next_y)

    remaining_pills = total_pills(map)
    if remaining_pills == 0:
        return True, True, True
    else:
        return True, True, False

def invalid_key(next_x, next_y):
    is_an_invalid_key = next_x == -1 and next_y == -1
    return is_an_invalid_key

def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == "|" or map[next_x][next_y] == "-"
    return is_a_wall

def is_a_ghost(map, next_x, next_y): 
    return map[next_x][next_y] == "G"

def is_a_pill(map, next_x, next_y): 
    return map[next_x][next_y] == "P"

def is_pacman(map, next_x, next_y): 
    return map[next_x][next_y] == "@"

def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows
    
    number_of_colums = len(map[0])
    y_is_valid = 0 <= next_y < number_of_colums

    return x_is_valid and y_is_valid

def total_pills(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total = total + 1
    return total 

def new_position(map, key):
    x, y = find_pacman(map)

    next_x = -1
    next_y = -1

    if key == "a":
        next_x = x
        next_y = y - 1
    elif key == "w":
        next_x = x - 1
        next_y = y
    elif key == "s":
        next_x = x + 1
        next_y = y
    elif key == "d":
        next_x = x
        next_y = y + 1
    return next_x,next_y
def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "G":
               all_ghosts.append([x,y])
    return all_ghosts

def move_ghosts(map):
    all_ghosts = find_ghosts(map)
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y],
            [ghost_x + 1, ghost_y]
        ]

        #escolhe uma posicao aleatoria pro ghost
        #e pega o x e y do movimento
        random_number= random.randint(0,3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]

        #checar algumas coisas antes de mover o ghost
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_wall(map, next_ghost_x,next_ghost_y):
            continue

        if is_a_ghost(map, next_ghost_x, next_ghost_y):
                continue

        if is_a_pill(map, next_ghost_x, next_ghost_y):
            continue
        
        if is_pacman(map, next_ghost_x, next_ghost_y):
            #O ghost encontrou o pacman
            return True

        #move o ghost pra uma posicao aleatoria
        everything_to_the_left = map[ghost_x][0:ghost_y]
        everything_to_the_right = map[ghost_x][ghost_y+1:]
        map[ghost_x] = everything_to_the_left+ "." + everything_to_the_right

        #a nova posição do ghost
        everything_to_the_left = map[next_ghost_x][0:next_ghost_y] 
        everything_to_the_right = map[next_ghost_x][next_ghost_y+1:]
        map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right

    return False

