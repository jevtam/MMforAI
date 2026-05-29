from data_loader import load_excel
from preprocessing import prepare_data
from neural_network import train_network, predict_raw, predict_class, accuracy


def main():
    file_path = "data.xlsx"
    # загрузка данных
    df = load_excel(file_path)

    print("Файл успешно прочитан через pandas")
    print(f"Количество строк: {len(df)}")
    print(f"Количество столбцов: {len(df.columns)}")
    
    # подготовка данных
    x_data, y_data, feature_columns = prepare_data(df)

    print("\nДанные подготовлены и нормализованы")
    print(f"Количество объектов: {len(x_data)}")
    print(f"Количество входных параметров: {len(feature_columns)}")

    # обучение нейросети
    weights, bias = train_network(
        x_data=x_data,
        y_data=y_data,
        learning_rate=0.05,
        epochs=1000,
        alpha=0.01,
        regularization="l2"
    )

    print("\nОбучение завершено")
    # вывод весов
    print("\nВеса:")
    for name, weight in zip(feature_columns, weights):
        print(f"{name}: {weight:.6f}")

    print(f"\nBias: {bias:.6f}")
    # вывод первых предсказаний
    print("\nПервые 10 предсказаний:")
    for i in range(10):
        raw = predict_raw(x_data[i], weights, bias)
        predicted = predict_class(x_data[i], weights, bias)
        true = y_data[i]

        print(
            f"Объект {i + 1}: "
            f"raw = {raw:.6f}, "
            f"predicted = {predicted}, "
            f"true = {true}"
        )

    acc = accuracy(x_data, y_data, weights, bias)

    print(f"\nПроцент правильности: {acc:.2f}%")


if __name__ == "__main__":
    main()