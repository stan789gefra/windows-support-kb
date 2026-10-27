# -*- coding: utf-8 -*-
"""
Terminal Knowledge Base & Practical Code Assistant
Allows interactive searching, viewing, and 1-click clipboard copying in CMD / Terminal.
"""
import sys
import subprocess
import json
import os

PRACTICALS = [
    ("Practical 1", "Probability Simulations & LLN (Coin, Dice, Pi)", "p1.py", "p1.txt"),
    ("Practical 2", "Discrete Distributions (Binomial, Poisson, Geometric)", "p2.py", "p2.txt"),
    ("Practical 3", "Continuous Distributions (Normal, Uniform, Exponential)", "p3.py", "p3.txt"),
    ("Practical 4", "Joint, Marginal & Conditional Distributions, Covariance", "p4.py", "p4.txt"),
    ("Practical 5", "Law of Large Numbers & Central Limit Theorem", "p5.py", "p5.txt"),
    ("Practical 6", "Transition Probability Matrices & Markov Chains", "p6.py", "p6.txt"),
    ("Practical 7", "Poisson Process, Inter-arrival & Queuing Simulations", "p7.py", "p7.txt"),
    ("Practical 8", "Continuous Time Markov Chains & Steady State", "p8.py", "p8.txt"),
]

def copy_to_clipboard(text):
    try:
        if sys.platform == "win32":
            p = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
            p.communicate(input=text.encode("utf-8"))
            return True
        elif sys.platform == "darwin":
            p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
            p.communicate(input=text.encode("utf-8"))
            return True
        else:
            p = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
            p.communicate(input=text.encode("utf-8"))
            return True
    except Exception:
        return False

def get_file_content(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    else:
        # Fallback to fetching from live domain
        import urllib.request
        url = f"https://doxiya.in/{filename}"
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")

def main():
    while True:
        print("\n" + "=" * 70)
        print("  MICROSOFT KB & CODE ASSISTANT - TERMINAL CONSOLE")
        print("=" * 70)
        for i, (name, desc, _, _) in enumerate(PRACTICALS, 1):
            print(f"  [{i}] {name}: {desc}")
        print("  [S] Search by keyword (e.g. 'markov', 'poisson', 'clt', 'bayes')")
        print("  [Q] Exit")
        print("=" * 70)
        
        choice = input("Enter choice (1-8, S, Q): ").strip()
        if not choice:
            continue
        
        if choice.lower() == 'q':
            print("Exiting. Good luck with your practicals!")
            break
            
        if choice.lower() == 's':
            keyword = input("\nEnter search keyword: ").strip().lower()
            if not keyword:
                continue
            all_content = get_file_content("all.txt")
            blocks = all_content.split("-" * 70)
            matches = [b for b in blocks if keyword in b.lower()]
            print(f"\nFound {len(matches)} matching sections for '{keyword}':\n")
            for idx, m in enumerate(matches, 1):
                header = m.strip().split("\n")[0]
                print(f"  [{idx}] {header[:70]}")
            
            if matches:
                sub = input("\nEnter match number to view (or Enter to skip): ").strip()
                if sub.isdigit() and 1 <= int(sub) <= len(matches):
                    sel = matches[int(sub) - 1]
                    print("\n" + "-" * 70 + sel + "\n" + "-" * 70)
                    copy_opt = input("Copy this code snippet to clipboard? (y/n): ").strip().lower()
                    if copy_opt == 'y':
                        # extract python code
                        if "PYTHON CODE:" in sel:
                            code_part = sel.split("PYTHON CODE:")[1].split("VERIFIED OUTPUT:")[0].strip()
                        else:
                            code_part = sel
                        if copy_to_clipboard(code_part):
                            print(">>> [SUCCESS] Code copied to clipboard! Paste with Ctrl + V.")
                        else:
                            print(">>> Could not access clipboard automatically.")
            continue
            
        if choice.isdigit() and 1 <= int(choice) <= 8:
            idx = int(choice) - 1
            name, desc, py_file, txt_file = PRACTICALS[idx]
            
            print(f"\n--- {name}: {desc} ---")
            print("  [1] View full question, code & outputs in terminal")
            print("  [2] Copy entire Python script to clipboard (Ctrl + V to paste)")
            print("  [3] Save script to local folder (as {name.replace(' ', '_').lower()}.py)")
            print("  [B] Back to main menu")
            
            sub_choice = input("Select option (1/2/3/B): ").strip().lower()
            if sub_choice == '1':
                content = get_file_content(txt_file)
                print("\n" + content)
            elif sub_choice == '2':
                py_code = get_file_content(py_file)
                if copy_to_clipboard(py_code):
                    print(f"\n>>> [SUCCESS] {name} Python code copied to clipboard! Paste directly into editor (Ctrl + V).")
                else:
                    print("\n>>> Clipboard copy failed.")
            elif sub_choice == '3':
                py_code = get_file_content(py_file)
                out_name = f"practical_{choice}.py"
                with open(out_name, "w", encoding="utf-8") as f:
                    f.write(py_code)
                print(f"\n>>> [SUCCESS] Saved to {out_name}")
        else:
            print("Invalid selection. Please choose 1-8, S, or Q.")

if __name__ == "__main__":
    main()
