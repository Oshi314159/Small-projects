# Gradient Descent for Intercept

# Returns the direction of error respect to the intercept
def get_gradient_at_b(x, y, m, b):
    diff = 0

    for i in range(len(x)):
        diff += (y[i] - (m * x[i] + b))

    b_gradient = diff * (-2/len(x))
    
    return b_gradient