import csv
import json
import os

path = "War-Thunder-Datamine/lang.vromfs.bin_u/lang/units.csv"
out = "out"

languages = {
    "<English>": "en", "<French>": "fr", "<Italian>": "it", "<German>": "de",
    "<Spanish>": "es", "<Russian>": "ru", "<Polish>": "pl", "<Czech>": "cs",
    "<Turkish>": "tr", "<Chinese>": "zh", "<Japanese>": "ja", "<Portuguese>": "pt",
    "<Ukrainian>": "uk", "<Serbian>": "sr", "<Hungarian>": "hu", "<Korean>": "ko",
    "<Belarusian>": "be", "<Romanian>": "ro", "<TChinese>": "zh_tw", "<HChinese>": "zh_cn",
    "<Vietnamese>": "vi"
}


os.makedirs(out, exist_ok=True)

def process(csv_data):
    units = {lang_code: {} for lang_code in languages.values()}
    for row in csv_data:
        unit_id = row.get("<ID|readonly|noverify>")
        if unit_id:
            for lang_key, lang_code in languages.items():
                name = row.get(lang_key)
                if name:
                    units[lang_code][unit_id] = name
    return units

def export(data, lang_code):
    file_name = f"units_{lang_code}.json"
    file_path = os.path.join(out, file_name)
    with open(file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f'Exported language "{lang_code}" to "{file_path}".')

def main():
    os.makedirs(out, exist_ok=True)
    with open(path, mode="r", encoding="utf-8") as csv_file:
        csv_data = list(csv.DictReader(csv_file, delimiter=";", quotechar="\""))
    units = process(csv_data)

    for lang_code, data in units.items():
        export(data, lang_code)

    print(f'Exported {len(languages)} language files to "{out}".')

if __name__ == "__main__":
    main()