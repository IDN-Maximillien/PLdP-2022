import matplotlib.pyplot as gmbr
from sklearn.linear_model import LinearRegression

x = [[1],[2],[3],[4],[5],[6],[7]]
y = [[25],[32],[36],[29],[30],[54],[59]]
error = [[25],[34],[26],[21],[30],[54],[59]]

jumlah = 0
for i in range(len(y)):
    jumlah += y[i][0]

print(jumlah)

model = LinearRegression()
model.fit(x,y)
y_predict = model.predict(x)

for i in range(len(x)):
    error[i][0] -= y_predict[i][0]

print(y)
print(y_predict)
print('Error Prediksi = ', error)

gmbr.figure()
gmbr.plot(x,y,'b.')
gmbr.axis([0,8,20,60])
gmbr.xlabel('Hari')
gmbr.ylabel('Penjualan (gelas)')
gmbr.grid(True)
gmbr.plot(x, y_predict, color='r')
gmbr.show()
