# функция нейрона: f(x,φ)=x1​w1​+x2​w2​+⋯+x9​w9​+bias
def predict_raw(x, weights, bias):
    result = bias

    for i in range(len(x)):
        result += x[i] * weights[i]

    return result

# классификация
def predict_class(x, weights, bias):
    raw = predict_raw(x, weights, bias)
    return 1 if raw >= 0.5 else 0

# функция потерь: MSE=N1​∑(y−y^​)2
def mse_loss(x_data, y_data, weights, bias, alpha=0.0, regularization="l2"):
    total_error = 0.0

    for x, y in zip(x_data, y_data):
        prediction = predict_raw(x, weights, bias)
        total_error += (y - prediction) ** 2

    mse = total_error / len(x_data)

    if regularization == "l2":
        penalty = alpha * sum(w ** 2 for w in weights)
    elif regularization == "l1":
        penalty = alpha * sum(abs(w) for w in weights)
    else:
        penalty = 0.0

    return mse + penalty

# обучение, производная: ∂E/∂wj​=2(y^​−y)xj​
def train_network(
    x_data,
    y_data,
    learning_rate=0.05,
    epochs=1000,
    alpha=0.01,
    regularization="l2"
):
    weights = [0.0] * len(x_data[0])
    bias = 0.0

    n = len(x_data)

    for epoch in range(epochs):
        grad_weights = [0.0] * len(weights)
        grad_bias = 0.0

        for x, y in zip(x_data, y_data):
            prediction = predict_raw(x, weights, bias)
            error = prediction - y

            for j in range(len(weights)):
                grad_weights[j] += 2 * error * x[j] # нормализация в коде

            grad_bias += 2 * error

        for j in range(len(weights)):
            grad_weights[j] /= n

           ## if regularization == "l2":
             ##   grad_weights[j] += 2 * alpha * weights[j] # Loss=MSE+α∑i​wi^2​
            ##elif regularization == "l1":
              ##  if weights[j] > 0:
                ##    grad_weights[j] += alpha
                ## elif weights[j] < 0:
                   ## grad_weights[j] -= alpha

            weights[j] -= learning_rate * grad_weights[j] # нормализция весов: wj​=wj​−η∂E/∂wj​​

        bias -= learning_rate * grad_bias / n # обновление bias:  bias=bias−η∂E/∂bias​

        if epoch % 100 == 0:
            loss = mse_loss(x_data, y_data, weights, bias, alpha, regularization)
            print(f"Эпоха {epoch}: loss = {loss:.6f}")

    return weights, bias

# оценка качества
def accuracy(x_data, y_data, weights, bias):
    correct = 0

    for x, y in zip(x_data, y_data):
        prediction = predict_class(x, weights, bias)

        if prediction == y:
            correct += 1

    return correct / len(y_data) * 100