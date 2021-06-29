from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

# 左右声道分离
def separate(file_data):
    left_sound = []
    right_sound = []
    for item in file_data:
        left_sound.append(item[0])
        right_sound.append(item[1])
    left_sound = np.array(left_sound)
    right_sound = np.array(right_sound)
    return [left_sound, right_sound]

# 画出声音图像
def draw_sound(soung_data, sample_rate):
    X_list = [i / sample_rate for i in len(soung_data)]
    plt.plot(X_list, soung_data)
    plt.xlabel("second")
    plt.ylabel("amplitude")
    plt.show()

