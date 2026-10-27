# -*- coding: utf-8 -*-
import build_website

all_txt = []
all_txt.append("=" * 70)
all_txt.append("  PROBABILITY & STOCHASTIC PROCESSES - COMPLETE LAB MANUAL")
all_txt.append("=" * 70)
all_txt.append("")

for i, p in enumerate(build_website.practicals, 1):
    py_lines = [
        "#" + "=" * 68,
        f"# Practical {i}: {p['title']}",
        "#" + "=" * 68 + "\n"
    ]
    
    txt_lines = [
        "=" * 70,
        f" PRACTICAL {i}: {p['title'].upper()}",
        f" THEORY: {p.get('theory_title', '')}",
        p.get('theory_desc', ''),
        "=" * 70,
        ""
    ]
    
    for q in p['questions']:
        py_lines.append(f"# --- [{q['badge']}] {q['title']} ---")
        py_lines.append(q['code'].strip())
        py_lines.append("\n")
        
        txt_lines.append("=" * 70)
        txt_lines.append(f"[Practical {i} - {q['badge']}] {q['title']}")
        txt_lines.append("=" * 70)
        txt_lines.append("PROBLEM:")
        txt_lines.append(q['desc'])
        txt_lines.append("\nPYTHON CODE:")
        txt_lines.append(q['code'].strip())
        txt_lines.append("\nVERIFIED OUTPUT:")
        txt_lines.append(q['output'].strip())
        if q.get('viva'):
            txt_lines.append(f"\nVIVA / KEY CONCEPT: {q['viva']}")
        txt_lines.append("\n")
        
    with open(f"p{i}.py", "w", encoding="utf-8") as f:
        f.write("\n".join(py_lines))
    with open(f"p{i}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines))
        
    all_txt.extend(txt_lines)

with open("all.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_txt))

print("Regenerated p1-p8 and all.txt with unified question blocks")
