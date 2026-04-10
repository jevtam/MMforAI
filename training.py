from neuron import predict_linear


def compute_error(x_data, y_data, weights, bias):
    """
    сумма квадратов ошибок:
    E(φ, D) = sum((y - f(x, φ))^2)
    """
    total_error = 0.0

    for x, y in zip(x_data, y_data):
        prediction = predict_linear(x, weights, bias)
        total_error += (y - prediction) ** 2

    return total_error


def train_linear_neuron(x_data, y_data, learning_rate=0.05, epochs=1000):
    """
    обучение одного нейрона методом градиентного спуска.
    """
    num_features = len(x_data[0])

    weights = [0.0] * num_features
    bias = 0.0

    dataset_size = len(x_data)

    for epoch in range(epochs):
        grad_w = [0.0] * num_features
        grad_b = 0.0

        for x, y in zip(x_data, y_data):
            prediction = predict_linear(x, weights, bias)
            error = prediction - y

            for j in range(num_features):
                grad_w[j] += 2 * error * x[j]

            grad_b += 2 * error

        for j in range(num_features):
            weights[j] -= learning_rate * grad_w[j] / dataset_size

        bias -= learning_rate * grad_b / dataset_size

        if epoch % 100 == 0:
            current_error = compute_error(x_data, y_data, weights, bias)
            print(f"Эпоха {epoch}: ошибка = {current_error:.6f}")

    return weights, bias