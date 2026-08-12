# Gradient Descent for Slope

# Returns the direction of error respect to the slope
def get_gradient_at_m(x, y, m, b):
    diff = 0

    for i in range(len(x)):
        diff += x[i] * (y[i] - (m * x[i] + b))

    m_gradient = diff * (-2/len(x))
    
    return m_gradient