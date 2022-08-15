# Estados_Del_Barco:
# 0 = Vacio
# 1 = Barco
# 2 = Tirado
# 3 = Barco Hundido

# Diagrama_Estado
# 0 --> si pone tiro pasa a 2
# 0 --> si pone barco pasa a 1
# 1 --> si pone tiro(2) pasa a 3

from random import randint


def verificar_ganador(tablero):
    gano = True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 1:
                gano = False
    if gano:
        print('Usted ha sido el ganador')
    else:
        print('Usted no ha ganado')
    return gano


def imprimir_tablero(titulo):
    print(titulo)
    print("┏━━━━━━━━━┓")
    for i in range(len(tablero_j1)):
        print("┃", end="")
        for j in range(len(tablero_j1[i])):
            if tablero_j1[i][j] == 0:
                print("‐", end="┃")
            elif tablero_j1[i][j] == 1:
                print('◉', end="┃")
            elif tablero_j1[i][j] == 2:
                print('✦', end="┃")
            elif tablero_j1[i][j] == 3:
                print('✘', end="┃")
        print("")
    print("┗━━━━━━━━━┛")
    print(" ◉ = BARCO   ‐ = NADA    ✘ = HUNDIDO    ✦ = AGUA")


def colocar_barco(tablero, columna, fila):
    tablero[columna][fila] = 1


def tiro(tablero, columna, fila):
    resultado = 'AGUA!!!'
    if tablero[columna][fila] == 1:
        tablero[columna][fila] = 3
        resultado = 'HUNDIDO!!!'
    elif tablero[columna][fila] == 0:
        tablero[columna][fila] = 2
    return resultado


print('╔═══════════════════════════════╗')
print('║ BIENVENIDO A LA BATALLA NAVAL ║')
print('╚═══════════════════════════════╝')

tablero_j1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

imprimir_tablero("━▶ 𝐄𝐬𝐭𝐞 𝐞𝐬 𝐞𝐥 𝐓𝐚𝐛𝐥𝐞𝐫𝐨 𝐞𝐧 𝐁𝐥𝐚𝐧𝐜𝐨 ◀━")

for i in range(5):
    print(f'━▶ 𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐥𝐚 𝐮𝐛𝐢𝐜𝐚𝐜𝐢𝐨𝐧 𝐝𝐞𝐥 𝐛𝐚𝐫𝐜𝐨 {i + 1} ◀━')
    columna = int(input('\n𝐂𝐎𝐋𝐔𝐌𝐍𝐀 ━▶ '))
    fila = int(input('\n𝐅𝐈𝐋𝐀 ━▶ '))
    colocar_barco(tablero_j1, columna, fila)
imprimir_tablero("𝐓𝐀𝐁𝐋𝐄𝐑𝐎 𝐈𝐍𝐈𝐂𝐈𝐀𝐋")

tablero_computadora = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
print('𝐂𝐎𝐌𝐏𝐔: 𝐄𝐬𝐭𝐨𝐲 𝐮𝐛𝐢𝐜𝐚𝐧𝐝𝐨 𝐦𝐢𝐬 𝐛𝐚𝐫𝐜𝐨𝐬...')
for i in range(5):
    columna = randint(0, 4)
    fila = randint(0, 4)
    colocar_barco(tablero_computadora, columna, fila)
print('𝐂𝐎𝐌𝐏𝐔: 𝐋𝐢𝐬𝐭𝐨!!!')

while verificar_ganador(tablero_j1) == False and verificar_ganador(tablero_computadora) == False:
    print('𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐮𝐛𝐢𝐜𝐚𝐜𝐢𝐨𝐧 𝐝𝐞𝐥 𝐭𝐢𝐫𝐨')
    columna = int(input('\n𝐂𝐎𝐋𝐔𝐌𝐍𝐀 ━▶ '))
    fila = int(input('\n𝐅𝐈𝐋𝐀 ━▶ '))
    resultado_tiro = tiro(tablero_computadora, columna, fila)
    print(resultado_tiro)

    print('𝐂𝐎𝐌𝐏𝐔: 𝗔𝗵𝗼𝗿𝗮 𝗲𝘀 𝗺𝗶 𝘁𝘂𝗿𝗻𝗼...')

    columna = randint(0, 4)
    fila = randint(0, 4)
    print(f'𝐂𝐎𝐌𝐏𝐔: 𝐓𝐞 𝐭𝐢𝐫𝐨 𝐚𝐥 {columna}, {fila}')
    resultado_tiro = tiro(tablero_j1, columna, fila)
    print(resultado_tiro)
    imprimir_tablero("𝐓𝐮 𝐭𝐚𝐛𝐥𝐞𝐫𝐨 𝐡𝐚 𝐪𝐮𝐞𝐝𝐚𝐝𝐨 𝐚𝐬𝐢")
