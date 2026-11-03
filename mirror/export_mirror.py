"""
Утилита подготовки текстов зеркала Google Drive для Kenshi Compain.
Формирует нормализованные документы для Google Docs в mirror/out/ согласно mirror/drive-map.json.
"""

import os
import json
import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DRIVE_MAP_PATH = os.path.join(ROOT_DIR, "mirror", "drive-map.json")
OUT_DIR = os.path.join(ROOT_DIR, "mirror", "out")

HEADER_PREFIX = "Зеркало репозитория Kenshi-Compain; обновлено {today}; правки вносятся через сессию.\n\n"

def build_mirror():
    os.makedirs(OUT_DIR, exist_ok=True)
    today = datetime.date.today().isoformat()
    
    with open(DRIVE_MAP_PATH, "r", encoding="utf-8") as f:
        drive_map = json.load(f)
        
    for doc in drive_map.get("documents", []):
        doc_name = doc["name"]
        folder = doc["folder"]
        sources = doc["sources"]
        
        folder_out = os.path.join(OUT_DIR, folder)
        os.makedirs(folder_out, exist_ok=True)
        
        combined_text = [HEADER_PREFIX.format(today=today)]
        found_sources = 0
        
        for src in sources:
            src_path = os.path.join(ROOT_DIR, src)
            if os.path.isfile(src_path):
                found_sources += 1
                with open(src_path, "r", encoding="utf-8") as sf:
                    content = sf.read().replace("\r\n", "\n")
                    combined_text.append(f"<!-- Источник: {src} -->\n\n" + content + "\n\n---\n\n")
            elif os.path.isdir(src_path):
                # Для глав / сессий собираем файлы по порядку
                files = sorted(os.listdir(src_path))
                for fn in files:
                    fp = os.path.join(src_path, fn)
                    if os.path.isfile(fp) and fn.endswith(".md"):
                        found_sources += 1
                        with open(fp, "r", encoding="utf-8") as sf:
                            content = sf.read().replace("\r\n", "\n")
                            combined_text.append(f"<!-- Источник: {src}/{fn} -->\n\n" + content + "\n\n---\n\n")
                            
        target_path = os.path.join(folder_out, f"{doc_name}.md")
        if found_sources > 0:
            with open(target_path, "w", encoding="utf-8") as tf:
                tf.write("".join(combined_text))
            print(f"Сформирован документ: {folder}/{doc_name}.md ({found_sources} источников)")
        else:
            print(f"Источники пока отсутствуют для: {folder}/{doc_name} (ожидается после миграции)")

if __name__ == "__main__":
    build_mirror()
