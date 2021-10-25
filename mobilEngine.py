# --------------------------------------------------------------------------------------------- #
# CATATAN

# IDEAS:
# 1. 

# TODO:
# 1. 

# NOTE:
# 1. 

# FIXME:
# 1. 

# --------------------------------------------------------------------------------------------- #
# LIBRARY/FILE PYTHON LAIN YANG DIGUNAKAN

import random           # Library random digunakan untuk men-generate obstacle secara random.
import planeGenerator
import time

# --------------------------------------------------------------------------------------------- #
# KAMUS LOKAL
# 1. 

# --------------------------------------------------------------------------------------------- #
# KODE UTAMA

def placeCar(pos_matrix, direction, car_position):
    if direction == 'up':
        pos_matrix[1][car_position] = '0'
        pos_matrix[0][car_position] = '-'

    if direction == 'right':
        pos_matrix[0][car_position + 1] = '0'
        pos_matrix[0][car_position] = '-'

    if direction == 'left':
        pos_matrix[0][car_position - 1] = '0'
        pos_matrix[0][car_position] = '-'

def getCarPosition(pos_matrix, lebar_jalan):
    for kolom in range(lebar_jalan):
        if pos_matrix[0][kolom] == '0':
            return kolom

# def optimalRoute(pos_matrix, lebar_jalan, car_position):
#     jalur_yang_tersedia = []

#     for kolom in range(lebar_jalan):
#         if pos_matrix[1][kolom] != '#':
#             jalur_yang_tersedia.append(kolom)

#     for jalur in jalur_yang_tersedia:
#         if car_position < jalur:
#             for kolom in range(car_position + 1, jalur + 1):
#                 if pos_matrix[0][kolom] == '#':
#                     jalur_yang_tersedia.remove(jalur)
#                     break
#         elif car_position > jalur:
#             for kolom in range(jalur, car_position):
#                 if pos_matrix[0][kolom] == '#':
#                     jalur_yang_tersedia.remove(jalur)
#                     break
#         else:
#             pass

#     difference = []
#     for jalur in jalur_yang_tersedia:
#         difference.append(abs(car_position - jalur))

#     return min(difference)

def checkSurroundings(pos_matrix, car_position):
    if pos_matrix[1][car_position] != '#':
        return True
    else:
        return False

# def moveCar(pos_matrix, car_position, lebar_jalan, tinggi_jalan):
#     optimal_route = optimalRoute(pos_matrix, lebar_jalan, car_position)

#     if checkSurroundings(pos_matrix, car_position):
#         placeCar(pos_matrix, car_position)

#     elif optimal_route == False:
#         print('Mohon maaf, mobil Anda terjebak.')
#         print('Anda tidak bisa melanjutkan perjalanan.')
#         quit()

#     elif optimal_route != False:
#         if car_position > optimal_route:
#             while car_position != optimal_route:
#                 car_position -= 1
#                 placeCar(pos_matrix, car_position)
#             placeCar(pos_matrix, car_position)

#         elif car_position < optimal_route:
#             while car_position != optimal_route:
#                 car_position += 1
#                 placeCar(pos_matrix, car_position)
#             placeCar(pos_matrix, car_position)

def obstacleDetector(pos_matrix, lebar_jalan):
    front_obstacle = []
    side_obstacle = []

    for kolom in range(lebar_jalan):
        if pos_matrix[1][kolom] == '#':
            front_obstacle.append(kolom)
        else:
            pass

    for kolom in range(lebar_jalan):
        if pos_matrix[0][kolom] == '#':
            side_obstacle.append(kolom)
        else:
            pass

    returned_matrix = [side_obstacle, front_obstacle]
    return returned_matrix

def optimalRoute(pos_matrix, car_position, obstacle_position, lebar_jalan):
    side_obstacle = obstacle_position[0]
    front_obstacle = obstacle_position[1]

    jalur_yang_tersedia = []

    side_obstacle.sort()
    front_obstacle.sort()

    for kolom in range(lebar_jalan):
        if kolom not in front_obstacle:
            jalur_yang_tersedia.append(kolom)

    for jalur in jalur_yang_tersedia:
        if jalur < car_position:
            for kolom in range(jalur, car_position):
                if pos_matrix[0][kolom] == '#':
                    jalur_yang_tersedia.remove(jalur)
                else:
                    pass
        if jalur > car_position:
            for kolom in range(car_position + 1, jalur + 1):
                if pos_matrix[0][kolom] == '#':
                    jalur_yang_tersedia.remove(jalur)
                else:
                    pass

    if jalur_yang_tersedia == []:
        print('Mohon maaf, mobil Anda terjebak. \n Anda tidak dapat melanjutkan perjalanan.')
        print('Sekali lagi, mohon maaf atas ketidaknyamanan ini.')
        quit()

    minimum = 100000
    min_jalur = []
    for jalur in jalur_yang_tersedia:
        if abs(car_position - jalur) < minimum:
            minimum = abs(car_position - jalur)
            min_jalur = [jalur]
        if abs(car_position - jalur) == minimum:
            min_jalur.append(jalur)
        else:
            pass

    return min_jalur

def moveCar(pos_matrix, car_position, lebar_jalan, tinggi_jalan, jalur_yang_mungkin):
    jalur = random.choice(jalur_yang_mungkin)
    if jalur > car_position:
        while car_position != jalur:
            placeCar(pos_matrix, 'right', car_position)
            planeGenerator.generate_road(pos_matrix,lebar_jalan, tinggi_jalan)
            car_position = getCarPosition(pos_matrix, lebar_jalan)
            time.sleep(0.5)
        placeCar(pos_matrix, 'up', car_position)

    if jalur < car_position:
        while car_position != jalur:
            placeCar(pos_matrix, 'left', car_position)
            planeGenerator.generate_road(pos_matrix, lebar_jalan, tinggi_jalan)
            car_position = getCarPosition(pos_matrix, lebar_jalan)
            time.sleep(0.5)
        placeCar(pos_matrix, 'up', car_position)