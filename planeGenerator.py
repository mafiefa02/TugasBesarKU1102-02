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
import mobilEngine

# --------------------------------------------------------------------------------------------- #
# KAMUS LOKAL
# 1. [function] generate_road(lebar_jalan) -> (print())
#       - lebar_jalan = int
#       - pos_matrix; dummy_obstacle_matrix = array (list of lists)

# --------------------------------------------------------------------------------------------- #
# KODE UTAMA

def generate_initial_positions(lebar_jalan, tinggi_jalan):
    pos_matrix = [[0 for i in range(lebar_jalan)] for j in range(tinggi_jalan)]

    # for kolom in range(lebar_jalan):
    #     if kolom == (lebar_jalan//2):
    #         pos_matrix[0][kolom] = '0'
    #     else:
    #         pos_matrix[0][kolom] = '-'

    # for baris in range(1, tinggi_jalan):
    #     for kolom in range(lebar_jalan):
    #         dummy_obstacle_matrix = random.choices([i for i in range(lebar_jalan)], k = lebar_jalan//8)
    #         if kolom in dummy_obstacle_matrix:
    #             pos_matrix[baris][kolom] = '#'
    #         else:
    #             pos_matrix[baris][kolom] = '-'

    for baris in range(tinggi_jalan):
        for kolom in range(lebar_jalan):
            dummy_obstacle_matrix = random.choices([i for i in range(lebar_jalan)], k = lebar_jalan//8)
            if kolom in dummy_obstacle_matrix:
                pos_matrix[baris][kolom] = '#'
            else:
                pos_matrix[baris][kolom] = '-'

    return pos_matrix

def generate_road(pos_matrix, lebar_jalan, tinggi_jalan):
    print('\n'*10)
    for baris in reversed(range(tinggi_jalan)):
            for kolom in reversed(range(lebar_jalan)):
                print(pos_matrix[baris][kolom], end=' ')
            print(' ')

def update_road(pos_matrix, lebar_jalan):
    dummy_obstacle_matrix = random.choices([i for i in range(lebar_jalan)], k = lebar_jalan//8)

    # for baris in reversed(range(tinggi_jalan-1)):
    #     pos_matrix[baris] = pos_matrix[baris + 1]

    pos_matrix.pop(0)

    dummy_matrix = [0 for i in range(lebar_jalan)]
    for kolom in range(lebar_jalan):
        if kolom in dummy_obstacle_matrix:
            dummy_matrix[kolom] = '#'
        else:
            dummy_matrix[kolom] = '-'
    pos_matrix.append(dummy_matrix)

    return pos_matrix