import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 1, 3]
y_predicted1 = [1, 2, 3]
y_predicted2 = [1.5, 2, 2.5]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

total_loss1 = 0
total_loss2 = 0

for i in range(3):
  total_loss1 += (y_predicted1[i] - y[i])**2

for i in range(3):
  total_loss2 += (y_predicted2[i] - y[i])**2

print(total_loss1)
print(total_loss2)

better_fit = 1 if total_loss1 < total_loss2 else 2

print(better_fit)