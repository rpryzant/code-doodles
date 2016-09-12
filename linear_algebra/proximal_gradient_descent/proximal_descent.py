import Math


def proximal_descent(g, g_prime, h_prox, x0, iterations = 1000, gamma = 1.0, epsilon = 1e-4):
    """
    minimizes a non-differentiable function f(x) = g(x) + h(x)

    PARAMS
    g: function
        g(x), the differentiable part of f
    
    g_prime: function
        g'(x) aka the gradient of g
        returns the direction of steepest increase along g

    h_prox: function
        h_prox(x, gamma) returns proximal operator of h at x using gamma as a distance weighting param
        h_prox gives a new x' which is a tradeoff of reducing h and staying close to x

    x0: vector
        initial stariting point

    iterations: self explanitory

    gamma: step size
    
    epsilon: self explanitory


    RETURNS
    x* = argmin_x { f(x) } if x* is reachable in the given num iterations. else None
    """
    # initialize current guess at x0
    xk = x0
    gk = g(xk)

    for _ in range(iterations):
        xk_old = xk
        # compute gradient for differentiable  part of f
        gk_gradient = g_prime(xk)
        # take gradient step to reduce g(x)
        xk_gradient = xk - gamma * gk_gradient
        # proximal update to reduce h(x) but stay close to xk_gradient
        xk = h_prox(xk_gradient, gamma)

        if Math.abs(xk - xk_old) < epsilon:
            return xk

    return None

