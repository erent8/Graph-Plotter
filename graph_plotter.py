import matplotlib.pyplot as plt

x = [1, 7, 9, 15, 16, 17, 19, 30, 45 ]
y = [2, 9, 16, 19, 22, 24, 30, 32, 46]
z = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
plt.plot(x, y, z, marker='o', linestyle='-', color='red', linewidth=2)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph')

plt.grid(True)  # Izgara çizgileri ekle

plt.xticks([1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 44, 45, 46])  # x ekseni işaretleri için özelleştirilmiş değerler belirle
plt.yticks([1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 44, 45, 46])  # y ekseni işaretleri için özelleştirilmiş değerler belirle

plt.axhline(0, color='green', linewidth=0.5)  # x ekseni etrafında yatay çizgi çiz
plt.axvline(0, color='purple', linewidth=0.5)  # y ekseni etrafında dikey çizgi çiz

plt.legend(['Data Points'], loc='upper left')  # Grafik için açıklama ekleyin

plt.show()
