import numpy as np
import matplotlib.pyplot as gambar
import statistics

# data_x = [31,41,59,26,53,58,97,23,23,84,23]
# data_y = [1,2,3,4,5,6,7,8,9,10,11]

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,23]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,110]

q0 = np.quantile(y, 0)
q1 = np.quantile(y, 0.25)
q2 = np.quantile(y, 0.5)
q3 = np.quantile(y, 0.75)
q4 = np.quantile(y, 1)
r = np.mean(x)
med = np.median(x)
mode = statistics.multimode(x)
var = statistics.variance(x)

print(f'''Rata-rata = {r}
Median = {med}
Mode = {mode}
Quantile 0 = {q0}
Quantile 1 = {q1}
Quantile 2 = {q2}
Quantile 3 = {q3}
Quantile 4 = {q4}
''')

gambar.plot(x, y)
gambar.scatter(x, y)
gambar.show()

mymodel = np.poly1d(np.polyfit(x,y,1))
myline = np.linspace(1,24,100)
gambar.scatter(x,y)
gambar.plot(myline, mymodel(myline))
gambar.show()
