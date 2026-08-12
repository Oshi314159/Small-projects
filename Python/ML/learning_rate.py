import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -(2/N) * diff
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff
    return m_gradient

def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    
    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)
    
    return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b = 0
m = 0
epochs = 1000

for i in range(epochs):
    b, m = step_gradient(months, revenue, b, m)

y = []
for x_val in (months):
    y.append(m * x_val + b)

plt.plot(months, revenue, "o")
plt.plot(months, y)
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()