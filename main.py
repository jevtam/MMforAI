import zipfile
import xml.etree.ElementTree as ET
import csv


NAMESPACE = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def read_shared_strings(zip_file):
    shared_strings = []

    try:
        xml_data = zip_file.read("xl/sharedStrings.xml")
    except KeyError:
        return shared_strings

    root = ET.fromstring(xml_data)

    for si in root.findall("main:si", NAMESPACE):
        parts = []
        for text_node in si.iterfind(".//main:t", NAMESPACE):
            parts.append(text_node.text or "")
        shared_strings.append("".join(parts))

    return shared_strings


def get_sheet_path(zip_file):
    workbook_xml = ET.fromstring(zip_file.read("xl/workbook.xml"))
    workbook_rels_xml = ET.fromstring(zip_file.read("xl/_rels/workbook.xml.rels"))

    rels_map = {}
    for rel in workbook_rels_xml:
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            rels_map[rel_id] = target

    sheets = workbook_xml.find("main:sheets", NAMESPACE)
    first_sheet = sheets[0]

    rel_id = first_sheet.attrib.get(
        "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    )

    if rel_id not in rels_map:
        raise ValueError("Не удалось найти путь к листу Excel.")

    return "xl/" + rels_map[rel_id]


def cell_value(cell, shared_strings):
    cell_type = cell.attrib.get("t")
    value_node = cell.find("main:v", NAMESPACE)

    if value_node is None:
        return ""

    raw_value = value_node.text

    if cell_type == "s":
        return shared_strings[int(raw_value)]

    return raw_value


def column_letters(cell_ref):
    letters = []
    for char in cell_ref:
        if char.isalpha():
            letters.append(char)
        else:
            break
    return "".join(letters)


def excel_column_to_index(column_name):
    result = 0
    for char in column_name:
        result = result * 26 + (ord(char.upper()) - ord("A") + 1)
    return result - 1


def read_xlsx_as_table(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_file:
        shared_strings = read_shared_strings(zip_file)
        sheet_path = get_sheet_path(zip_file)

        sheet_xml = ET.fromstring(zip_file.read(sheet_path))

        all_rows = []

        for row in sheet_xml.findall(".//main:row", NAMESPACE):
            row_data = {}

            for cell in row.findall("main:c", NAMESPACE):
                cell_ref = cell.attrib.get("r", "")
                col_name = column_letters(cell_ref)
                col_index = excel_column_to_index(col_name)
                row_data[col_index] = cell_value(cell, shared_strings)

            all_rows.append(row_data)

    if not all_rows:
        raise ValueError("Файл пустой или не удалось прочитать строки.")

    max_columns = max(max(row.keys(), default=-1) for row in all_rows) + 1

    normalized_rows = []
    for row in all_rows:
        normalized = []
        for col_index in range(max_columns):
            normalized.append(row.get(col_index, ""))
        normalized_rows.append(normalized)

    headers = normalized_rows[0]
    data_rows = normalized_rows[1:]

    records = []
    for row in data_rows:
        record = {}
        for i, header in enumerate(headers):
            record[header] = row[i]
        records.append(record)

    return headers, records


def save_to_csv(headers, records, output_path):
    """
    Сохраняет данные в CSV.
    """
    with open(output_path, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(records)


def main():
    input_file = "data.xlsx"
    output_file = "data.csv"

    headers, records = read_xlsx_as_table(input_file)

    print("Файл успешно прочитан.")
    print(f"Количество признаков: {len(headers)}")
    print(f"Количество записей: {len(records)}")
    print("\nСтолбцы:")
    for header in headers:
        print(f"- {header}")

    print("\nПервые 3 записи:")
    for record in records[:3]:
        print(record)

    save_to_csv(headers, records, output_file)
    print(f"\nCSV-файл сохранен как: {output_file}")


if __name__ == "__main__":
    main()