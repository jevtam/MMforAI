def safe_int(value):
    value = str(value).strip()
    if value == "":
        raise ValueError("Пустое числовое значение")
    return int(float(value))


def encode_record(record):
    x = [
        safe_int(record["Возраст"]),
        1 if record["Пол"].strip().lower() == "мужской" else 0,
        1 if record["Состоит в браке"].strip().lower() == "да" else 0,
        safe_int(record["Иждивенцы"]),
        safe_int(record["Доход"]),
        safe_int(record["Опыт работы"]),
        safe_int(record["Срок проживания"]),
        safe_int(record["Недвижимость"]),
        safe_int(record["Месячный платеж"]),
    ]

    y = 1 if safe_int(record["Число просрочек более 60 дн."]) > 0 else 0
    return x, y


def build_dataset(records):
    x_data = []
    y_data = []
    skipped = 0

    for i, record in enumerate(records, start=1):
        try:
            x, y = encode_record(record)
            x_data.append(x)
            y_data.append(y)
        except Exception:
            skipped += 1
            print(f"Пропущена строка {i}: некорректные или пустые данные")

    print(f"\nКорректных строк: {len(x_data)}")
    print(f"Пропущено строк: {skipped}")

    return x_data, y_data


def min_max_normalize(matrix):
    if not matrix:
        return [], [], []

    num_features = len(matrix[0])

    mins = [matrix[0][j] for j in range(num_features)]
    maxs = [matrix[0][j] for j in range(num_features)]

    for row in matrix:
        for j in range(num_features):
            if row[j] < mins[j]:
                mins[j] = row[j]
            if row[j] > maxs[j]:
                maxs[j] = row[j]

    normalized = []
    for row in matrix:
        new_row = []
        for j in range(num_features):
            if maxs[j] == mins[j]:
                new_row.append(0.0)
            else:
                value = (row[j] - mins[j]) / (maxs[j] - mins[j])
                new_row.append(value)
        normalized.append(new_row)

    return normalized, mins, maxs