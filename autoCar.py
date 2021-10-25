# --------------------------------------------------------------------------------------------- #
# CATATAN

# IDEAS:
# 1. Menghindari obstacle.
# 2. Menentukan rute (jangan lurus aja)
# 3. Ada kemacetan. (damn, ini ribet jujurly)

# TODO:
# 1. Buat sebuah space/bidang menggunakan matriks.
# 2. Buat obstacle, jika bisa menggunakan library random, gunakan.
# 3. Buat infinite loop, dengan fitur:
#   - Pengecekan keadaan sekitar mobil (area yang di cek sebesar 3 x 3).
#   - Mobil bergerak (maju, kanan, kiri, atau bahkan berhenti) setiap kali pengulangan loop.
# 4. Jika bisa, tambahkan mobil lain yang bisa mengganggu jalannya mobil kita.

# NOTE:
# 1. Fungsi/fitur yang bisa digunakan:
#   - If/elif/else
#   - Loop
#   - Array
#   - Function

# FIXME:
# 1. Kadang mobilnya nabrak obstacle wkaokoawk (mobil gerak dua kali ke kanan/kiri jika dia terjebak.)
# 2. Mobil cenderung belok ke kanan (ini karena urutan 'if')

# --------------------------------------------------------------------------------------------- #
# LIBRARY/FILE PYTHON LAIN YANG DIGUNAKAN

import random           # Library random digunakan untuk men-generate obstacle secara random.
import mobilEngine      # import mobilEngine.py yang ada di dalam satu folder.
import planeGenerator   # import planeGenerator.py yang ada di dalam satu folder.
import time             # Library random digunakan agar dapat menampilkan update tepat setiap 1 sekon.

# --------------------------------------------------------------------------------------------- #
# KAMUS LOKAL
# 1. lebar_jalan;
# 2. positions;

# --------------------------------------------------------------------------------------------- #
# KODE UTAMA

if __name__ == "__main__":
    lebar_jalan = 9
    tinggi_jalan = 10
    car_position = lebar_jalan//2                                                           # di tengah

    pos_matrix = planeGenerator.generate_initial_positions(lebar_jalan, tinggi_jalan)
    pos_matrix[0][car_position] = '0'
    planeGenerator.generate_road(pos_matrix, lebar_jalan, tinggi_jalan)                     # print jalan
    time.sleep(1)

    car_can_move = mobilEngine.checkSurroundings(pos_matrix, car_position)                  # cek depan mobil

    while True:
        car_position = mobilEngine.getCarPosition(pos_matrix, lebar_jalan)
        car_can_move = mobilEngine.checkSurroundings(pos_matrix, car_position)
        if car_can_move == False:
            obstacle_position = mobilEngine.obstacleDetector(pos_matrix, lebar_jalan)
            jalur_optimal = mobilEngine.optimalRoute(pos_matrix,car_position, obstacle_position, lebar_jalan)
            mobilEngine.moveCar(pos_matrix, car_position, lebar_jalan, tinggi_jalan, jalur_optimal)
            pos_matrix = planeGenerator.update_road(pos_matrix, lebar_jalan)
            planeGenerator.generate_road(pos_matrix, lebar_jalan, tinggi_jalan)             # print jalan
            time.sleep(0.5)

        if car_can_move:
            mobilEngine.placeCar(pos_matrix, 'up', car_position)
            pos_matrix = planeGenerator.update_road(pos_matrix, lebar_jalan)  # remove baris paling bawah dari jalan
            planeGenerator.generate_road(pos_matrix, lebar_jalan, tinggi_jalan)             # print jalan
            time.sleep(0.5)
