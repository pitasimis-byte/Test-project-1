import argparse
import json
import os
from typing import List

class NotesManager:
    def __init__(self, path: str = "notes.json"):
        self.path = path
        self._notes: List[str] = []
        self.load()

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self._notes = data
                else:
                    self._notes = []
        except FileNotFoundError:
            self._notes = []

    def save(self):
        dirpath = os.path.dirname(self.path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._notes, f, ensure_ascii=False, indent=2)

    def add(self, text: str):
        self._notes.append(text)
        self.save()

    def list(self) -> List[str]:
        return list(self._notes)

    def remove(self, index: int) -> str:
        if index < 0 or index >= len(self._notes):
            raise IndexError("note index out of range")
        note = self._notes.pop(index)
        self.save()
        return note

def main():
    parser = argparse.ArgumentParser(description="Mini notes CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Add a note")
    p_add.add_argument("text", help="Note text")

    p_list = sub.add_parser("list", help="List notes")

    p_rm = sub.add_parser("remove", help="Remove note by index")
    p_rm.add_argument("index", type=int, help="0-based index")

    p_clear = sub.add_parser("clear", help="Clear all notes")

    parser.add_argument("--file", "-f", default="notes.json", help="Notes storage file")

    args = parser.parse_args()

    nm = NotesManager(args.file)

    if args.cmd == "add":
        nm.add(args.text)
        print("Added note")
    elif args.cmd == "list":
        for i, n in enumerate(nm.list()):
            print(f"{i}: {n}")
    elif args.cmd == "remove":
        try:
            removed = nm.remove(args.index)
            print(f"Removed: {removed}")
        except IndexError as e:
            print(e)
    elif args.cmd == "clear":
        # remove file
        nm._notes = []
        nm.save()
        print("Cleared notes")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
