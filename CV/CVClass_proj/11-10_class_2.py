import matplotlib.pyplot as plt

weight1 = [30, 20, 40, 15, 10]
names = ['apple', 'samsung', 'OPPO', 'MI', 'vivo']

plt.pie(weight1, autopct='%.2f%%', labels=names, pctdistance=10)
plt.show()
