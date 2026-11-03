"""
Утилита импорта входящих документов из папки Входящие/ (Google Drive mirror / чаты)
Разбирает маркеры === ЖУРНАЛ ===, === ПОВЕСТВОВАНИЕ ===, === ПРАВКИ ===.
Перед записью выводит diff и требует подтверждения.
"""

import os
import re
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INBOX_DIR = os.path.join(ROOT_DIR, "mirror", "inbox")
PROCESSED_DIR = os.path.join(ROOT_DIR, "mirror", "inbox", "processed")

RE_JOURNAL = re.compile(r"===\s*ЖУРНАЛ\s+(S-\d{8}-\d+)\s*===\s*\n(.*?)(?====\s*ПОВЕСТВОВАНИЕ|===\s*ПРАВКИ|===\s*КОНЕЦ|$)", re.DOTALL)
RE_NARRATIVE = re.compile(r"===\s*ПОВЕСТВОВАНИЕ\s+(S-\d{8}-\d+)\s*===\s*\n(.*?)(?====\s*ПРАВКИ|===\s*КОНЕЦ|$)", re.DOTALL)
RE_EDITS = re.compile(r"===\s*ПРАВКИ:\s*([^\n=]+?)\s*===\s*\n(.*?)(?====\s*ПРАВКИ|===\s*КОНЕЦ|$)", re.DOTALL)

def parse_inbox_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
        
    journal_match = RE_JOURNAL.search(text)
    narrative_match = RE_NARRATIVE.search(text)
    edits_matches = RE_EDITS.findall(text)
    
    if not journal_match and not narrative_match and not edits_matches:
        return None  # Неразобранный документ
        
    result = {
        "file": file_path,
        "journal_id": journal_match.group(1) if journal_match else None,
        "journal_content": journal_match.group(2).strip() if journal_match else None,
        "narrative_id": narrative_match.group(1) if narrative_match else None,
        "narrative_content": narrative_match.group(2).strip() if narrative_match else None,
        "edits": [{"target": e[0].strip(), "content": e[1].strip()} for e in edits_matches]
    }
    return result

def scan_inbox(inbox_path=INBOX_DIR):
    if not os.path.isdir(inbox_path):
        return []
        
    parsed = []
    unparsed = []
    
    for fn in os.listdir(inbox_path):
        fp = os.path.join(inbox_path, fn)
        if os.path.isfile(fp) and fn.endswith((".md", ".txt")):
            res = parse_inbox_file(fp)
            if res:
                parsed.append(res)
            else:
                unparsed.append(fp)
                
    return parsed, unparsed

if __name__ == "__main__":
    p, u = scan_inbox()
    print(f"Разобрано документов: {len(p)}, Нераспознано: {len(u)}")
