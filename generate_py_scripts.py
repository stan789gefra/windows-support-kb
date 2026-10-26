import os
import json

os.makedirs("scripts", exist_ok=True)

with open("practicals_data.json", "r", encoding="utf-8") as f:
    practicals = json.load(f)

for p in practicals:
    num = p["number"]
    py_filename = f"scripts/practical_{num}.py"
    
    code_lines = [
        f'"""',
        f'Practical {num}: {p["title"]}',
        f'Description: {p["description"]}',
        f'Original File: {p["filename"]}',
        f'"""\n'
    ]
    
    for sec in p["sections"]:
        for item in sec["items"]:
            if item["type"] == "markdown":
                # Convert markdown to python comment
                md_text = item["content"]
                code_lines.append("\n# " + "-"*60)
                for line in md_text.splitlines():
                    code_lines.append(f"# {line}")
                code_lines.append("# " + "-"*60 + "\n")
            elif item["type"] == "code":
                code_lines.append(item["code"])
                code_lines.append("\n")
                
    with open(py_filename, "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(code_lines))
        
    print(f"Generated {py_filename}")
