def verificar_ganador(tablero):
    gano = True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 1:
                gano = False
    return gano


def imprimir_tablero(titulo, tablero, ocultar_barcos=False):
    print(titulo)
    print("┏━━━━━━━━━┓")
    for i in range(len(tablero)):
        print("┃", end="")
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                print("‐", end="┃")
            elif tablero[i][j] == 1 and not ocultar_barcos:
                print('◉', end="┃")
            elif tablero[i][j] == 1 and ocultar_barcos:
                print('-', end="┃")
            elif tablero[i][j] == 2:
                print('✦', end="┃")
            elif tablero[i][j] == 3:
                print('✘', end="┃")
        print("")
    print("┗━━━━━━━━━┛")
    print("TIPS: ◉ = BARCO   ‐ = NADA    ✘ = HUNDIDO    ✦ = AGUA")


def colocar_barco(tablero, columna, fila):
    if tablero[columna][fila] == 1:
        print('𝐘𝐚 𝐞𝐱𝐢𝐬𝐭𝐞 𝐮𝐧 𝐛𝐚𝐫𝐜𝐨 𝐞𝐧 𝐞𝐬𝐭𝐚 𝐮𝐛𝐢𝐜𝐚𝐜𝐢𝐨𝐧')
        return False
    else:
        tablero[columna][fila] = 1
        return True


def tiro(tablero, columna, fila):
    resultado = 'AGUA!!!🥶🥶'
    if tablero[columna][fila] == 1:
        tablero[columna][fila] = 3
        resultado = 'HUNDIDO!!!🤩🤩'
    elif tablero[columna][fila] == 0:
        tablero[columna][fila] = 2
    return resultado
