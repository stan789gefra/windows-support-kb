# -*- coding: utf-8 -*-
"""
Live Search for Probability & Statistics Lab Practicals (1-8)
Works in Terminal, CMD, PowerShell, and Jupyter Notebooks.
"""
import sys
import os
import urllib.request
import subprocess

# Ensure safe output on Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def copy_to_clipboard(text):
    try:
        p = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
        p.communicate(input=text.encode("utf-8"))
        return True
    except Exception:
        return False

def search(query=None, copy_first=False):
    """
    Search all 8 practicals by keyword (e.g. 'poisson', 'markov', 'coin', 'clt', 'bayes').
    Usage:
        search('poisson')
        search('markov', copy_first=True)
    """
    if query is None:
        args = [a for a in sys.argv[1:] if not a.startswith("-")]
        if args:
            query = " ".join(args)
        else:
            try:
                query = input("Enter search keyword: ").strip()
            except EOFError:
                query = ""

    if not query:
        print("Please enter a keyword to search. Example: search('poisson')")
        return

    text = None
    if os.path.exists("all.txt"):
        try:
            with open("all.txt", "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except Exception:
            pass

    if not text:
        try:
            url = "https://doxiya.in/all.txt"
            with urllib.request.urlopen(url) as resp:
                text = resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            print(f"Error fetching from https://doxiya.in: {e}")
            return

    # Split into clean question blocks
    raw_blocks = text.split("=" * 70)
    blocks = []
    for b in raw_blocks:
        b_clean = b.strip()
        # Keep blocks that contain actual questions and code
        if "PYTHON CODE:" in b_clean or "THEORY:" in b_clean:
            blocks.append(b_clean)

    matches = [b for b in blocks if query.lower() in b.lower()]

    if not matches:
        print(f"\n[!] No practical or question found matching: '{query}'")
        return

    print("=" * 70)
    print(f"  FOUND {len(matches)} MATCHES FOR: '{query.upper()}'")
    print("=" * 70 + "\n")

    for i, m in enumerate(matches, 1):
        print(f">>> [RESULT {i} of {len(matches)}] " + "=" * 45)
        print(m)
        print("=" * 70 + "\n")

    if copy_first or "-c" in sys.argv or len(matches) == 1:
        first = matches[0]
        if "PYTHON CODE:" in first:
            code = first.split("PYTHON CODE:")[1].split("VERIFIED OUTPUT:")[0].strip()
            if copy_to_clipboard(code):
                print(f">>> [SUCCESS] Code from Result 1 is copied to clipboard! (Ctrl + V to paste)")

if __name__ == "__main__":
    search()
