import json
import os
import base64

notebooks = [
    ("Practical 1", "pRAC_1.ipynb", "Simulation of Random Experiments (Coin Toss & Dice Roll)"),
    ("Practical 2", "prac2.ipynb", "Probability Distributions & Parameter Estimation (Normal, Poisson, Exponential, Noise Analysis)"),
    ("Practical 3", "prac3.ipynb", "Joint & Conditional Probability (Titanic & Palmer Penguins Datasets)"),
    ("Practical 4", "Prac4.ipynb", "Markov Chains & Customer Churn Modeling"),
    ("Practical 5", "Prac5.ipynb", "Hidden Markov Models (HMM) - Part-of-Speech Tagging"),
    ("Practical 6", "Prac6.ipynb", "Monte Carlo Simulation & Financial Risk Analysis (Value at Risk - VaR)"),
    ("Practical 7", "Prac7.ipynb", "Bayesian Inference & Parameter Estimation (Titanic Survival Rate)"),
    ("Practical 8", "Prac8.ipynb", "PageRank Algorithm & Random Walk Simulation (Directed Graphs)")
]

os.makedirs("assets/images", exist_ok=True)

extracted = []

for p_num, (title, fname, desc) in enumerate(notebooks, 1):
    with open(fname, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    practical_data = {
        "id": f"prac-{p_num}",
        "number": p_num,
        "title": title,
        "filename": fname,
        "description": desc,
        "sections": [],
        "all_code": []
    }
    
    current_section = {
        "title": "General",
        "description": "",
        "items": []
    }
    
    img_counter = 0

    for c_idx, cell in enumerate(nb["cells"]):
        ctype = cell.get("cell_type")
        source = "".join(cell.get("source", []))
        
        if ctype == "markdown":
            stripped = source.strip()
            if stripped:
                current_section["items"].append({
                    "type": "markdown",
                    "content": stripped
                })
        elif ctype == "code":
            clean_source = source.strip()
            if not clean_source:
                continue
                
            practical_data["all_code"].append(clean_source)
            
            # Extract outputs
            outputs = []
            for out in cell.get("outputs", []):
                # Text output
                if "text" in out:
                    text_str = "".join(out["text"]).strip()
                    if text_str:
                        outputs.append({"type": "text", "content": text_str})
                elif "data" in out:
                    data = out["data"]
                    if "text/plain" in data:
                        text_str = "".join(data["text/plain"]).strip()
                        if text_str:
                            outputs.append({"type": "text", "content": text_str})
                    # Image output
                    for mime, b64 in data.items():
                        if mime.startswith("image/"):
                            ext = mime.split("/")[1]
                            img_filename = f"prac{p_num}_img{img_counter}.{ext}"
                            img_path = os.path.join("assets", "images", img_filename)
                            with open(img_path, "wb") as img_f:
                                img_f.write(base64.b64decode(b64))
                            outputs.append({
                                "type": "image",
                                "src": f"assets/images/{img_filename}",
                                "alt": f"Output plot for {title} (cell {c_idx})"
                            })
                            img_counter += 1
            
            current_section["items"].append({
                "type": "code",
                "cell_index": c_idx,
                "code": clean_source,
                "outputs": outputs
            })
            
    if current_section["items"]:
        practical_data["sections"].append(current_section)
        
    extracted.append(practical_data)

with open("practicals_data.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, indent=2)

print(f"Extracted {len(extracted)} practicals successfully!")
for p in extracted:
    code_cells = sum(1 for sec in p["sections"] for it in sec["items"] if it["type"] == "code")
    imgs = sum(1 for sec in p["sections"] for it in sec["items"] if it["type"] == "code" for out in it.get("outputs", []) if out["type"] == "image")
    print(f"{p['title']}: {code_cells} code blocks, {imgs} images extracted")
