#!/usr/bin/env python3
import shutil
import json
import sys
from pathlib import Path
from datetime import date

# Usage: python new_post.py <newname>
if len(sys.argv) < 2:
    print("Usage: python new_post.py <newname>")
    sys.exit(1)

new_name = sys.argv[1]

# Paths
template_dir = Path("./template")
target_dir = Path(f"./{new_name}")
json_file = Path("./posts.json")

# 1. Copy template directory
shutil.copytree(template_dir, target_dir)
print(f"Copied template to {target_dir}")

# 2. Append new entry to JSON file
with json_file.open("r", encoding="utf-8") as f:
    data = json.load(f)

# Calculate next ID
next_id = max(post["id"] for post in data) + 1 if data else 1

# Create new entry
new_entry = {
    "id": next_id,
    "title": "Blog Template",
    "url": f"/blog/{new_name}/",
    "date": date.today().isoformat(),
    "hidden": False,
    "tags": ["template", "writing"],
    "description": "A reusable base for new posts."
}

data.append(new_entry)

# Write updated JSON back
with json_file.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added new entry to {json_file}")

