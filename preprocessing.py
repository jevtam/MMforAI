# подготовка данных

def prepare_data(df):
    df = df.copy()
    # кодирование категориальный признаков
    df["Пол"] = df["Пол"].str.strip().str.lower().map({
        "мужской": 1,
        "женский": 0
    })
    # кодирование категориальный признаков
    df["Состоит в браке"] = df["Состоит в браке"].str.strip().str.lower().map({
        "да": 1,
        "нет": 0
    })
    # формирование target, правильный ответ, если просрочек 0 то target 0, если 1+, то target 1
    df["target"] = df["Число просрочек более 60 дн."].apply(
        lambda value: 1 if value > 0 else 0
    )
    # формируется матрица признаков
    feature_columns = [
        "Возраст",
        "Пол",
        "Состоит в браке",
        "Иждивенцы",
        "Доход",
        "Опыт работы",
        "Срок проживания",
        "Недвижимость",
        "Месячный платеж",
    ]

    df = df.dropna(subset=feature_columns + ["target"])

    x = df[feature_columns]
    y = df["target"]

    x_min = x.min()
    x_max = x.max()

    x_norm = (x - x_min) / (x_max - x_min)

    return x_norm.values.tolist(), y.values.tolist(), feature_columns