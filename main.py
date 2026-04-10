from excel_reader import read_xlsx_as_table
from preprocessing import build_dataset, min_max_normalize
from csv_utils import save_to_csv
from training import train_linear_neuron
from neuron import predict_linear, predict_class


def main():
    input_file = r"C:\MMforAI\data.xlsx"

    headers, records = read_xlsx_as_table(input_file)

    print("Файл успешно прочитан.")
    print(f"Количество исходных записей: {len(records)}")
    print(f"Количество исходных признаков: {len(headers)}")

    x_raw, y = build_dataset(records)
    x_norm, mins, maxs = min_max_normalize(x_raw)

    print("\nПервые 3 объекта до нормализации:")
    for i in range(3):
        print(x_raw[i], "->", y[i])

    print("\nПервые 3 объекта после нормализации:")
    for i in range(3):
        print(x_norm[i], "->", y[i])

    output_headers = [
        "Возраст",
        "Пол",
        "Состоит в браке",
        "Иждивенцы",
        "Доход",
        "Опыт работы",
        "Срок проживания",
        "Недвижимость",
        "Месячный платеж",
        "target",
    ]

    output_rows = []
    for i in range(len(x_norm)):
        output_rows.append(x_norm[i] + [y[i]])

    save_to_csv(output_headers, output_rows, "data_normalized.csv")

    print("\nНормализованный файл сохранён как data_normalized.csv")
    print("\nМинимумы по признакам:", mins)
    print("Максимумы по признакам:", maxs)

    weights, bias = train_linear_neuron(
        x_data=x_norm,
        y_data=y,
        learning_rate=0.05,
        epochs=1000
    )

    print("\nОбучение завершено.")
    print("Веса нейрона:")
    for i, w in enumerate(weights, start=1):
        print(f"w{i} = {w:.6f}")
    print(f"bias = {bias:.6f}")

    print("\nПервые 10 предсказаний:")
    for i in range(10):
        raw_prediction = predict_linear(x_norm[i], weights, bias)
        class_prediction = predict_class(x_norm[i], weights, bias)

        print(
            f"Объект {i + 1}: "
            f"raw = {raw_prediction:.6f}, "
            f"class = {class_prediction}, "
            f"true = {y[i]}"
        )


if __name__ == "__main__":
    main()