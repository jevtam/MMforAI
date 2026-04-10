def predict_linear(x, weights, bias):
    """
    f(x, φ) = sum(x_j * φ_j) + φ_0
    """
    result = bias
    for j in range(len(x)):
        result += x[j] * weights[j]
    return result


def predict_class(x, weights, bias, threshold=0.5):
    raw_output = predict_linear(x, weights, bias)
    return 1 if raw_output >= threshold else 0