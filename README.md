# 📊 Probability & Statistics with Python (PSP) - Lab Solutions Website

A modern, responsive, and interactive web application hosting complete solutions, tested Python implementations, mathematical formulations, terminal outputs, and visual plots for **Probability and Statistics for Programmers (PSP)**.

Built with clean **HTML5, CSS3, and modern JavaScript**, featuring **1-click Copy Code buttons**, instant search, dark/light theme switching, and full optimization for **GitHub Pages**.

---

## 🚀 Live Demo on GitHub Pages

When you push this repository to GitHub and enable Pages, your website will be live at:
```
https://<YOUR_GITHUB_USERNAME>.github.io/PSP/
```

---

## ✨ Features

- 📋 **1-Click "Copy Code" Buttons**: Every single Python snippet has an individual copy button with visual "Copied! ✓" feedback and toast notifications.
- 📦 **"Copy All Code" per Practical**: Copy the complete executable Python code for an entire lab in one click.
- ⬇️ **Direct Downloads**: Download each practical as a clean `.py` script or the original `.ipynb` Jupyter notebook.
- 🔍 **Instant Search & Filter**: Real-time search across all 8 practicals, questions, code, and statistical concepts (`Markov`, `Bayes`, `Dice`, `Penguin`, etc.).
- 🌓 **Dark & Light Mode**: Seamless theme switcher with persistent user preference stored in `localStorage`.
- 🖼️ **Interactive Plot Lightbox**: Click on any of the 13 Matplotlib plots to enlarge, inspect in high resolution, or download.
- 📱 **Mobile & Desktop Responsive**: Clean responsive sidebar drawer for tablets and phones, sticky navigation for desktop.
- ⚡ **Zero Dependencies / No Build Step**: Open `index.html` directly in any web browser without needing npm, webpack, or any local server!

---

## 📚 Practicals Directory

| Lab | Title | Notebook | Script | Key Topics & Algorithms |
|---|---|---|---|---|
| **Practical 1** | Simulation of Random Experiments | [`pRAC_1.ipynb`](pRAC_1.ipynb) | [`scripts/practical_1.py`](scripts/practical_1.py) | Coin toss, Dice rolls, Law of Large Numbers, Two-dice sums |
| **Practical 2** | Probability Distributions & Noise | [`prac2.ipynb`](prac2.ipynb) | [`scripts/practical_2.py`](scripts/practical_2.py) | Normal, Poisson, Exponential, Sensor noise modeling ($\epsilon \sim \mathcal{N}(0, 4)$) |
| **Practical 3** | Joint & Conditional Probability | [`prac3.ipynb`](prac3.ipynb) | [`scripts/practical_3.py`](scripts/practical_3.py) | Contingency tables, Titanic survival, Palmer Penguins, Independence test |
| **Practical 4** | Discrete-Time Markov Chains | [`Prac4.ipynb`](Prac4.ipynb) | [`scripts/practical_4.py`](scripts/practical_4.py) | Transition matrix, 1-step & 5-step evolution, 1000-customer churn curve |
| **Practical 5** | Hidden Markov Models (HMM) | [`Prac5.ipynb`](Prac5.ipynb) | [`scripts/practical_5.py`](scripts/practical_5.py) | POS tagging (Noun/Verb), Observation emission (dogs/bark), Sequence probability |
| **Practical 6** | Monte Carlo & Financial VaR | [`Prac6.ipynb`](Prac6.ipynb) | [`scripts/practical_6.py`](scripts/practical_6.py) | 10,000 portfolio simulations, 95% Value at Risk (VaR), Loss tail distribution |
| **Practical 7** | Bayesian Inference & Parameter Estimation | [`Prac7.ipynb`](Prac7.ipynb) | [`scripts/practical_7.py`](scripts/practical_7.py) | Titanic female survival, Binomial log-likelihood, Uniform prior, MAP estimate ($\theta=0.7$) |
| **Practical 8** | PageRank Algorithm & Random Walk | [`Prac8.ipynb`](Prac8.ipynb) | [`scripts/practical_8.py`](scripts/practical_8.py) | 4-node web graph, 100,000-step random surfer simulation, NetworkX comparison |

---

## 🛠️ Step-by-Step Guide: How to Host on GitHub Pages

Hosting this website on GitHub Pages takes less than 2 minutes:

### Step 1: Initialize Git and Commit
Open PowerShell or Command Prompt in this folder (`c:\Users\asdf\Downloads\PSP`):

```bash
git init
git add .
git commit -m "Initial commit: PSP Lab Solutions website with copy buttons"
```

### Step 2: Create a New GitHub Repository
1. Go to [github.com/new](https://github.com/new).
2. Set the repository name to `PSP` (or any name you prefer).
3. Choose **Public** (required for free GitHub Pages).
4. Do **not** check "Add a README file" (we already have this one).
5. Click **Create repository**.

### Step 3: Link and Push to GitHub
Copy and run the commands shown on GitHub:

```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/PSP.git
git push -u origin main
```
*(Replace `<YOUR_GITHUB_USERNAME>` with your actual GitHub username)*

### Step 4: Enable GitHub Pages
1. In your GitHub repository, click the **Settings** tab at the top.
2. In the left navigation menu, click **Pages** (under "Code and automation").
3. Under **Build and deployment > Source**, select:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main`
   - **Folder**: `/ (root)`
4. Click **Save**.

Within 1-2 minutes, GitHub will deploy your website! You will see the live link:
```
Your site is live at https://<YOUR_GITHUB_USERNAME>.github.io/PSP/
```

---

## 💻 How to Run Locally

### Option 1: Direct File Open
Simply double-click `index.html` in Windows File Explorer. It opens instantly in your default web browser (Chrome, Edge, Firefox, Brave) with full styling and copy button support!

### Option 2: Python Local Web Server
If you prefer testing via localhost:
```bash
python -m http.server 8000
```
Then visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📂 Project Structure

```
PSP/
├── index.html                 # Main website homepage (all 8 practicals)
├── .nojekyll                  # Signals GitHub Pages to serve all static assets
├── README.md                  # Documentation and GitHub Pages deployment guide
├── css/
│   └── style.css              # Modern responsive CSS (Dark/Light themes, code styling)
├── js/
│   ├── app.js                 # Universal copy-to-clipboard, search, modals, shortcuts
│   └── practicals.js          # Extracted metadata & lab configuration
├── assets/
│   └── images/                # 13 high-resolution Matplotlib output plots
│       ├── prac1_img0.png ... prac1_img2.png
│       ├── prac2_img0.png ... prac2_img3.png
│       ├── prac4_img0.png
│       ├── prac6_img0.png ... prac6_img1.png
│       ├── prac7_img0.png
│       └── prac8_img0.png ... prac8_img1.png
├── scripts/                   # Ready-to-run Python scripts (.py) for download
│   ├── practical_1.py
│   ├── practical_2.py
│   ├── ...
│   └── practical_8.py
└── *.ipynb                    # Original Jupyter Notebooks (Prac 1 to 8)
```

---

## ⌨️ Keyboard Shortcuts

- <kbd>/</kbd> : Focus instant search bar
- <kbd>T</kbd> : Toggle between Dark and Light mode
- <kbd>Esc</kbd> : Close open plot image modal or guide modal

---

© PSP Labs • Designed for students and educators.
