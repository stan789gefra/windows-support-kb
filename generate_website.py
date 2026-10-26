import json
import os
import re
import html

# Ensure directories exist
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("assets/images", exist_ok=True)
os.makedirs("scripts", exist_ok=True)

# Create .nojekyll for GitHub Pages
with open(".nojekyll", "w", encoding="utf-8") as f:
    f.write("")

# Load extracted practical data
with open("practicals_data.json", "r", encoding="utf-8") as f:
    practicals_data = json.load(f)

# Metadata for each practical
metadata = [
    {
        "id": "prac-1",
        "num": 1,
        "title": "Practical 1: Simulation of Random Experiments",
        "subtitle": "Coin Toss & Dice Roll Simulations, Law of Large Numbers",
        "filename": "pRAC_1.ipynb",
        "py_script": "scripts/practical_1.py",
        "tags": ["numpy", "matplotlib", "Monte Carlo", "Probability"],
        "objectives": "Verify the Law of Large Numbers through large-scale stochastic trials; simulate coin tosses with varying sample sizes (N=10 to 100,000); analyze discrete frequency distributions for single die and two-dice sum experiments."
    },
    {
        "id": "prac-2",
        "num": 2,
        "title": "Practical 2: Probability Distributions & Noise Modeling",
        "subtitle": "Normal, Poisson, Exponential Distributions & Sensor Noise Analysis",
        "filename": "prac2.ipynb",
        "py_script": "scripts/practical_2.py",
        "tags": ["numpy", "scipy.stats", "matplotlib", "Distributions"],
        "objectives": "Generate and fit continuous and discrete distributions (Normal, Poisson, Exponential); calculate sample parameter estimators (mean, variance, rate λ); model additive zero-mean Gaussian noise on real-world sensor measurements."
    },
    {
        "id": "prac-3",
        "num": 3,
        "title": "Practical 3: Joint, Conditional Probability & Independence",
        "subtitle": "Contingency Tables & Independence Testing (Titanic & Palmer Penguins)",
        "filename": "prac3.ipynb",
        "py_script": "scripts/practical_3.py",
        "tags": ["pandas", "seaborn", "Contingency Tables", "Bayes Rule"],
        "objectives": "Construct cross-tabulated contingency tables; compute marginal, joint, and conditional probabilities P(A|B); evaluate survival disparities on Titanic data; verify statistical independence P(A ∩ B) = P(A) · P(B) on Palmer Penguins."
    },
    {
        "id": "prac-4",
        "num": 4,
        "title": "Practical 4: Discrete-Time Markov Chains",
        "subtitle": "Customer State Transitions, Multi-step Evolution & Churn Modeling",
        "filename": "Prac4.ipynb",
        "py_script": "scripts/practical_4.py",
        "tags": ["numpy", "pandas", "matplotlib", "Markov Chains"],
        "objectives": "Model customer lifecycle states (New, Active, Churned) using stochastic transition matrices; compute n-step transition distributions via matrix multiplication; simulate 1000-customer cohort trajectories and plot churn curves."
    },
    {
        "id": "prac-5",
        "num": 5,
        "title": "Practical 5: Hidden Markov Models (HMM)",
        "subtitle": "Part-of-Speech (POS) Tagging with State Transitions & Emissions",
        "filename": "Prac5.ipynb",
        "py_script": "scripts/practical_5.py",
        "tags": ["numpy", "pandas", "HMM", "NLP"],
        "objectives": "Set up Hidden Markov Models with hidden states (Noun, Verb) and observations (dogs, bark); validate initial, transition, and emission matrices; calculate joint probabilities of hidden state and observation sequences."
    },
    {
        "id": "prac-6",
        "num": 6,
        "title": "Practical 6: Monte Carlo Simulation & Risk Analysis",
        "subtitle": "Value at Risk (95% VaR) for Financial Portfolio Modeling",
        "filename": "Prac6.ipynb",
        "py_script": "scripts/practical_6.py",
        "tags": ["numpy", "matplotlib", "Financial Risk", "Monte Carlo"],
        "objectives": "Simulate 10,000 portfolio profit/loss outcomes under lognormal return assumptions; compute 95% Value at Risk (VaR) using empirical percentile ranking; visualize loss tail distribution with VaR threshold markers."
    },
    {
        "id": "prac-7",
        "num": 7,
        "title": "Practical 7: Bayesian Inference & Parameter Estimation",
        "subtitle": "Binomial Likelihood, Prior, Posterior & MAP on Titanic Survival Data",
        "filename": "Prac7.ipynb",
        "py_script": "scripts/practical_7.py",
        "tags": ["pandas", "seaborn", "numpy", "Bayesian Stats"],
        "objectives": "Apply Bayes' theorem to estimate female survival rate parameter θ; compute Binomial log-likelihood; update a uniform prior to obtain posterior probabilities; determine MAP estimate (θ* = 0.7) and posterior mean."
    },
    {
        "id": "prac-8",
        "num": 8,
        "title": "Practical 8: PageRank Algorithm & Random Walk",
        "subtitle": "Random Surfer Simulation & Stationary Distribution on Directed Graphs",
        "filename": "Prac8.ipynb",
        "py_script": "scripts/practical_8.py",
        "tags": ["networkx", "matplotlib", "Graph Theory", "PageRank"],
        "objectives": "Simulate a random surfer on a 4-node directed web graph with 85% damping and 15% teleportation over 100,000 steps; compare empirical visit frequencies against NetworkX's analytical PageRank; visualize network graph topology."
    }
]

def highlight_python(code_str):
    tokens = [
        ('COMMENT', r'#[^\n]*'),
        ('STRING', r"('''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\"|'([^'\\]|\\.)*'|\"([^\"\\]|\\.)*\")"),
        ('KEYWORD', r'\b(def|class|import|from|as|return|if|elif|else|for|while|in|is|not|and|or|try|except|finally|with|lambda|yield|raise|global|assert|pass|break|continue|None|True|False)\b'),
        ('BUILTIN', r'\b(print|len|range|zip|enumerate|map|filter|sum|min|max|abs|round|int|float|str|list|dict|set|tuple|type|open|super|idxmax|dropna|groupby|crosstab|head|describe|copy)\b'),
        ('NUMBER', r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),
        ('DECORATOR', r'@[a-zA-Z_]\w*'),
        ('FUNCTION', r'\b([a-zA-Z_]\w*)\s*(?=\()'),
        ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
        ('OPERATOR', r'(\+|-|\*|/|%|@|==|!=|<=|>=|<|>|=|&|\||\^|~)'),
        ('WHITESPACE', r'\s+'),
        ('OTHER', r'.')
    ]
    master_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens))
    
    out = []
    lines = code_str.split('\n')
    for line in lines:
        line_out = []
        for match in master_regex.finditer(line):
            kind = match.lastgroup
            val = html.escape(match.group())
            if kind == 'COMMENT':
                line_out.append(f'<span class="tok-comment">{val}</span>')
            elif kind == 'STRING':
                line_out.append(f'<span class="tok-string">{val}</span>')
            elif kind == 'KEYWORD':
                line_out.append(f'<span class="tok-keyword">{val}</span>')
            elif kind == 'BUILTIN':
                line_out.append(f'<span class="tok-builtin">{val}</span>')
            elif kind == 'NUMBER':
                line_out.append(f'<span class="tok-number">{val}</span>')
            elif kind == 'FUNCTION':
                line_out.append(f'<span class="tok-func">{val}</span>')
            elif kind == 'OPERATOR':
                line_out.append(f'<span class="tok-op">{val}</span>')
            else:
                line_out.append(val)
        out.append(''.join(line_out))
    return '\n'.join(out)

def format_text_md(text):
    text = text.strip()
    if not text:
        return ""
    text = html.escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    text = text.replace('P(H)=0.5', '<code>P(H) = 0.5</code>')
    text = text.replace('P(T)=0.5', '<code>P(T) = 0.5</code>')
    text = text.replace('P(A∩B)=P(A)P(B)', '<code>P(A ∩ B) = P(A) · P(B)</code>')
    
    lines = text.split('\n')
    res = []
    in_ul = False
    for l in lines:
        l_s = l.strip()
        if not l_s:
            if in_ul: res.append('</ul>'); in_ul = False
            continue
        if l_s.startswith('# '):
            if in_ul: res.append('</ul>'); in_ul = False
            res.append(f'<h4 class="q-title-lg">{l_s[2:]}</h4>')
        elif l_s.startswith('## '):
            if in_ul: res.append('</ul>'); in_ul = False
            res.append(f'<h5 class="q-title-md">{l_s[3:]}</h5>')
        elif l_s.startswith('- ') or l_s.startswith('* '):
            if not in_ul: res.append('<ul class="q-list">'); in_ul = True
            res.append(f'<li>{l_s[2:]}</li>')
        elif re.match(r'^\d+\.\s', l_s):
            if in_ul: res.append('</ul>'); in_ul = False
            res.append(f'<div class="q-step">{l_s}</div>')
        else:
            if in_ul: res.append('</ul>'); in_ul = False
            res.append(f'<p class="q-p">{l_s}</p>')
    if in_ul:
        res.append('</ul>')
    return '\n'.join(res)

# Build JSON data file for front-end JS (search & dynamic features)
js_data_path = os.path.join("js", "practicals.js")
with open(js_data_path, "w", encoding="utf-8") as f:
    f.write("// Autogenerated practicals data\n")
    f.write("const PRACTICALS_DATA = " + json.dumps(metadata, indent=2) + ";\n")

# Generate HTML Cards for each Practical
practicals_html = []
nav_items_html = []

for idx, p_meta in enumerate(metadata):
    p_data = practicals_data[idx]
    p_id = p_meta["id"]
    p_num = p_meta["num"]
    p_title = p_meta["title"]
    p_subtitle = p_meta["subtitle"]
    p_tags = p_meta["tags"]
    p_obj = p_meta["objectives"]
    p_filename = p_meta["filename"]
    p_pyscript = p_meta["py_script"]
    
    # Navigation link in sidebar
    nav_items_html.append(f'''
      <a href="#{p_id}" class="nav-link" data-target="{p_id}">
        <span class="nav-num">{p_num}</span>
        <span class="nav-label">{p_title.split(":")[1].strip()}</span>
      </a>
    ''')
    
    # Combined full code for practical
    full_code = "\n\n".join(p_data["all_code"])
    escaped_full_code = html.escape(full_code)
    
    tags_html = " ".join([f'<span class="badge badge-tag">{html.escape(t)}</span>' for t in p_tags])
    
    # Build blocks inside the practical
    blocks_html = []
    items = p_data["sections"][0]["items"]
    
    step_num = 1
    code_block_index = 1
    
    i = 0
    while i < len(items):
        item = items[i]
        
        if item["type"] == "markdown":
            md_content = item["content"]
            # Look ahead to see if the next item is code
            next_code = None
            if i + 1 < len(items) and items[i+1]["type"] == "code":
                next_code = items[i+1]
                i += 1 # advance past code
                
            code_html = ""
            outputs_html = ""
            if next_code:
                raw_code = next_code["code"]
                escaped_raw_code = html.escape(raw_code)
                highlighted_code = highlight_python(raw_code)
                line_count = len(raw_code.splitlines())
                
                # Output handling
                if next_code.get("outputs"):
                    for out in next_code["outputs"]:
                        if out["type"] == "text":
                            esc_out = html.escape(out["content"])
                            outputs_html += f'''
                            <div class="output-container">
                              <div class="output-header">
                                <span class="output-title"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg> Console Output</span>
                                <button class="btn-copy-output" data-copy="{esc_out}" title="Copy Output">
                                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy
                                </button>
                              </div>
                              <pre class="output-pre"><code>{esc_out}</code></pre>
                            </div>
                            '''
                        elif out["type"] == "image":
                            outputs_html += f'''
                            <div class="plot-container">
                              <div class="plot-header">
                                <span class="plot-title"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg> Graphical Output</span>
                                <span class="plot-badge">Click image to expand</span>
                              </div>
                              <div class="plot-image-wrapper" onclick="openLightbox('{out["src"]}', '{html.escape(out.get("alt", "Plot Output"))}')">
                                <img src="{out["src"]}" alt="{html.escape(out.get("alt", "Plot Output"))}" class="plot-img" loading="lazy" />
                                <div class="plot-overlay"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg></div>
                              </div>
                            </div>
                            '''
                
                code_html = f'''
                <div class="code-card">
                  <div class="code-card-header">
                    <div class="code-info">
                      <span class="file-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></span>
                      <span class="code-filename">Snippet {code_block_index}</span>
                      <span class="code-lines">{line_count} lines</span>
                      <span class="code-lang">Python</span>
                    </div>
                    <button class="btn-copy-code" data-copy="{escaped_raw_code}" aria-label="Copy code to clipboard">
                      <span class="copy-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg></span>
                      <span class="copy-text">Copy Code</span>
                    </button>
                  </div>
                  <div class="code-body">
                    <pre><code class="language-python">{highlighted_code}</code></pre>
                  </div>
                  {outputs_html}
                </div>
                '''
                code_block_index += 1
            
            blocks_html.append(f'''
            <div class="question-block" id="{p_id}-step-{step_num}">
              <div class="question-header">
                <span class="q-badge">Part {step_num}</span>
              </div>
              <div class="question-text">
                {format_text_md(md_content)}
              </div>
              {code_html}
            </div>
            ''')
            step_num += 1
            
        elif item["type"] == "code":
            # Code without preceding markdown
            raw_code = item["code"]
            escaped_raw_code = html.escape(raw_code)
            highlighted_code = highlight_python(raw_code)
            line_count = len(raw_code.splitlines())
            
            outputs_html = ""
            if item.get("outputs"):
                for out in item["outputs"]:
                    if out["type"] == "text":
                        esc_out = html.escape(out["content"])
                        outputs_html += f'''
                        <div class="output-container">
                          <div class="output-header">
                            <span class="output-title"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg> Console Output</span>
                            <button class="btn-copy-output" data-copy="{esc_out}" title="Copy Output">
                              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy
                            </button>
                          </div>
                          <pre class="output-pre"><code>{esc_out}</code></pre>
                        </div>
                        '''
                    elif out["type"] == "image":
                        outputs_html += f'''
                        <div class="plot-container">
                          <div class="plot-header">
                            <span class="plot-title"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg> Graphical Output</span>
                            <span class="plot-badge">Click image to expand</span>
                          </div>
                          <div class="plot-image-wrapper" onclick="openLightbox('{out["src"]}', '{html.escape(out.get("alt", "Plot Output"))}')">
                            <img src="{out["src"]}" alt="{html.escape(out.get("alt", "Plot Output"))}" class="plot-img" loading="lazy" />
                            <div class="plot-overlay"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg></div>
                          </div>
                        </div>
                        '''
                        
            blocks_html.append(f'''
            <div class="question-block" id="{p_id}-step-{step_num}">
              <div class="code-card">
                <div class="code-card-header">
                  <div class="code-info">
                    <span class="file-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></span>
                    <span class="code-filename">Snippet {code_block_index}</span>
                    <span class="code-lines">{line_count} lines</span>
                    <span class="code-lang">Python</span>
                  </div>
                  <button class="btn-copy-code" data-copy="{escaped_raw_code}" aria-label="Copy code to clipboard">
                    <span class="copy-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg></span>
                    <span class="copy-text">Copy Code</span>
                  </button>
                </div>
                <div class="code-body">
                  <pre><code class="language-python">{highlighted_code}</code></pre>
                </div>
                {outputs_html}
              </div>
            </div>
            ''')
            step_num += 1
            code_block_index += 1
        i += 1
        
    all_blocks_rendered = "\n".join(blocks_html)
    
    practicals_html.append(f'''
    <!-- PRACTICAL {p_num} CARD -->
    <article class="practical-card" id="{p_id}" data-practical="{p_num}">
      <header class="practical-header">
        <div class="practical-header-top">
          <div class="header-badge-row">
            <span class="badge badge-primary">Practical 0{p_num}</span>
            <span class="badge badge-sub">PSP Lab</span>
            {tags_html}
          </div>
          <div class="header-action-buttons">
            <button class="btn btn-action btn-copy-all" data-copy="{escaped_full_code}" title="Copy complete Python code for Practical {p_num}">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              <span>Copy All Code</span>
            </button>
            <a href="{p_pyscript}" download class="btn btn-action btn-download" title="Download Python script (practical_{p_num}.py)">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              <span>Download .py</span>
            </a>
            <a href="{p_filename}" download class="btn btn-action btn-download-alt" title="Download Jupyter Notebook ({p_filename})">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
              <span>.ipynb</span>
            </a>
          </div>
        </div>
        
        <h2 class="practical-title">{html.escape(p_title)}</h2>
        <p class="practical-subtitle">{html.escape(p_subtitle)}</p>
        
        <div class="objective-box">
          <div class="objective-icon">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          </div>
          <div class="objective-text">
            <strong>Lab Objective:</strong> {html.escape(p_obj)}
          </div>
        </div>
      </header>
      
      <div class="practical-content">
        {all_blocks_rendered}
      </div>
      
      <footer class="practical-footer">
        <a href="#top" class="back-to-top-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg>
          Back to Top
        </a>
      </footer>
    </article>
    ''')

rendered_practicals = "\n".join(practicals_html)
rendered_nav = "\n".join(nav_items_html)

# Now construct the complete index.html
html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PSP Lab Solutions | Probability & Statistics in Python</title>
  <meta name="description" content="Complete lab solutions, tested Python code, mathematical questions, terminal outputs, and visualizations for Probability and Statistics for Programmers (PSP). Hosted on GitHub Pages.">
  <meta name="keywords" content="PSP, Probability, Statistics, Python, Jupyter, Markov Chains, Bayesian Inference, PageRank, Monte Carlo, Distributions, GitHub Pages">
  <meta name="author" content="PSP Team">
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📊</text></svg>">
  
  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Custom CSS -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body id="top">
  <!-- Top Navigation Bar -->
  <header class="site-header">
    <div class="header-container">
      <div class="brand-section">
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle navigation menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <a href="#top" class="brand-logo">
          <span class="logo-icon">📊</span>
          <div class="brand-text">
            <span class="brand-title">PSP<span class="accent-text">Labs</span></span>
            <span class="brand-badge">Python 3</span>
          </div>
        </a>
      </div>

      <!-- Search Bar -->
      <div class="search-section">
        <div class="search-input-wrapper">
          <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="globalSearchInput" placeholder="Search practicals, topics, code (e.g. Markov, Bayes, Dice)..." aria-label="Search code and practicals" />
          <kbd class="search-shortcut">/</kbd>
        </div>
      </div>

      <!-- Header Actions -->
      <div class="header-actions">
        <button class="icon-btn theme-toggle" id="themeToggleBtn" aria-label="Toggle dark/light theme" title="Toggle Theme (T)">
          <svg class="sun-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          <svg class="moon-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>

        <button class="btn btn-gh-guide" id="btnGhGuide" title="GitHub Pages Deployment Guide">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <span>Host Guide</span>
        </button>

        <a href="https://github.com" target="_blank" rel="noopener" class="icon-btn gh-link" title="Open GitHub">
          <svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
      </div>
    </div>
  </header>

  <!-- Layout Container -->
  <div class="app-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-title">All Practicals (1-8)</span>
        <span class="sidebar-count">8 Labs</span>
      </div>
      
      <div class="filter-pills-sidebar">
        <button class="pill-btn active" data-filter="all">All Labs</button>
        <button class="pill-btn" data-filter="sim">Simulations</button>
        <button class="pill-btn" data-filter="prob">Probability</button>
        <button class="pill-btn" data-filter="stoch">Stochastic</button>
      </div>

      <nav class="sidebar-nav" id="sidebarNav">
        {rendered_nav}
      </nav>

      <div class="sidebar-footer">
        <div class="stat-card">
          <div class="stat-number">8 / 8</div>
          <div class="stat-desc">Practicals Solved & Tested</div>
        </div>
        <button class="btn btn-block btn-copy-all-global" id="btnCopyAllGlobal">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span>Copy Complete Lab Repo</span>
        </button>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Hero Banner -->
      <section class="hero-banner">
        <div class="hero-badge">
          <span class="pulse-dot"></span> Probability and Statistics with Python
        </div>
        <h1 class="hero-title">
          PSP Practical Lab <span class="gradient-text">Solutions</span>
        </h1>
        <p class="hero-subtitle">
          Interactive practical notebook codes, math formulations, terminal outputs, and high-resolution plot visualizations — designed with 1-click copy buttons and ready for GitHub Pages hosting.
        </p>

        <!-- Highlights Row -->
        <div class="hero-stats">
          <div class="hero-stat-item">
            <span class="stat-val">8</span>
            <span class="stat-label">Lab Practicals</span>
          </div>
          <div class="hero-stat-item">
            <span class="stat-val">55+</span>
            <span class="stat-label">Code Snippets</span>
          </div>
          <div class="hero-stat-item">
            <span class="stat-val">13</span>
            <span class="stat-label">Matplotlib Plots</span>
          </div>
          <div class="hero-stat-item">
            <span class="stat-val">1-Click</span>
            <span class="stat-label">Copy & Download</span>
          </div>
        </div>

        <!-- Quick Jump Bar -->
        <div class="quick-jump-bar">
          <span class="jump-label">Jump to:</span>
          <div class="jump-links">
            <a href="#prac-1" class="jump-chip">Prac 1: Coin & Dice</a>
            <a href="#prac-2" class="jump-chip">Prac 2: Distributions</a>
            <a href="#prac-3" class="jump-chip">Prac 3: Contingency Tables</a>
            <a href="#prac-4" class="jump-chip">Prac 4: Markov Chains</a>
            <a href="#prac-5" class="jump-chip">Prac 5: HMM POS Tagging</a>
            <a href="#prac-6" class="jump-chip">Prac 6: Monte Carlo VaR</a>
            <a href="#prac-7" class="jump-chip">Prac 7: Bayesian Inference</a>
            <a href="#prac-8" class="jump-chip">Prac 8: PageRank</a>
          </div>
        </div>
      </section>

      <!-- Search results banner (hidden by default) -->
      <div class="search-feedback" id="searchFeedback" style="display: none;">
        <span id="searchResultText">Showing matches</span>
        <button id="clearSearchBtn" class="btn-clear-search">Clear Search</button>
      </div>

      <!-- Practicals Container -->
      <div class="practicals-container" id="practicalsContainer">
        {rendered_practicals}
      </div>
      
      <!-- Footer -->
      <footer class="site-footer">
        <div class="footer-content">
          <div class="footer-left">
            <div class="footer-brand">📊 PSP Labs</div>
            <p class="footer-text">Probability and Statistics with Python Practical Lab Solutions</p>
          </div>
          <div class="footer-right">
            <div class="keyboard-hints">
              <span class="kbd-hint"><kbd>/</kbd> Search</span>
              <span class="kbd-hint"><kbd>T</kbd> Theme</span>
              <span class="kbd-hint"><kbd>Esc</kbd> Close modal</span>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <span>Ready to host on GitHub Pages • Built with HTML5, CSS3 & JavaScript</span>
        </div>
      </footer>
    </main>
  </div>

  <!-- Image Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal" aria-hidden="true">
    <div class="lightbox-backdrop" onclick="closeLightbox()"></div>
    <div class="lightbox-content">
      <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close image preview">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
      <img src="" alt="" id="lightboxImg" class="lightbox-img" />
      <div class="lightbox-footer">
        <span id="lightboxCaption" class="lightbox-caption"></span>
        <a href="" id="lightboxDownloadBtn" download class="btn btn-sm btn-download-img">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Save Image
        </a>
      </div>
    </div>
  </div>

  <!-- GitHub Pages Guide Modal -->
  <div class="guide-modal" id="guideModal" aria-hidden="true">
    <div class="guide-backdrop" onclick="closeGuide()"></div>
    <div class="guide-dialog">
      <div class="guide-header">
        <div class="guide-title-box">
          <span class="guide-icon">🚀</span>
          <h3>How to Host this on GitHub Pages</h3>
        </div>
        <button class="guide-close" onclick="closeGuide()" aria-label="Close guide">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="guide-body">
        <p class="guide-intro">Follow these 3 simple steps to host this project completely free on GitHub Pages:</p>
        
        <div class="guide-step">
          <div class="step-num-badge">1</div>
          <div class="step-info">
            <h4>Initialize Git & Commit</h4>
            <p>Open Terminal in this folder (<code>c:\\Users\\asdf\\Downloads\\PSP</code>) and run:</p>
            <div class="code-card">
              <div class="code-card-header">
                <span class="code-filename">Terminal</span>
                <button class="btn-copy-code" data-copy="git init&#10;git add .&#10;git commit -m &quot;Deploy PSP Labs website with copy buttons&quot;"><span class="copy-text">Copy</span></button>
              </div>
              <div class="code-body">
                <pre><code>git init
git add .
git commit -m "Deploy PSP Labs website with copy buttons"</code></pre>
              </div>
            </div>
          </div>
        </div>

        <div class="guide-step">
          <div class="step-num-badge">2</div>
          <div class="step-info">
            <h4>Create a GitHub Repository & Push</h4>
            <p>Go to <a href="https://github.com/new" target="_blank" rel="noopener">github.com/new</a>, name it <code>PSP</code> (or anything you like), set to <strong>Public</strong>, then run:</p>
            <div class="code-card">
              <div class="code-card-header">
                <span class="code-filename">Terminal</span>
                <button class="btn-copy-code" data-copy="git branch -M main&#10;git remote add origin https://github.com/YOUR_USERNAME/PSP.git&#10;git push -u origin main"><span class="copy-text">Copy</span></button>
              </div>
              <div class="code-body">
                <pre><code>git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/PSP.git
git push -u origin main</code></pre>
              </div>
            </div>
          </div>
        </div>

        <div class="guide-step">
          <div class="step-num-badge">3</div>
          <div class="step-info">
            <h4>Turn On GitHub Pages in Repo Settings</h4>
            <ul class="guide-bullets">
              <li>In your GitHub repo, click <strong>Settings</strong> (top tab).</li>
              <li>In the left sidebar, click <strong>Pages</strong>.</li>
              <li>Under <strong>Build and deployment &gt; Source</strong>, select <code>Deploy from a branch</code>.</li>
              <li>Under <strong>Branch</strong>, select <code>main</code> and folder <code>/ (root)</code>, then click <strong>Save</strong>!</li>
              <li>In ~60 seconds, your website will be live at: <code>https://YOUR_USERNAME.github.io/PSP/</code> 🎉</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="guide-footer">
        <button class="btn btn-primary" onclick="closeGuide()">Got it, let's go!</button>
      </div>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div class="toast-container" id="toastContainer" aria-live="polite"></div>

  <!-- JavaScript -->
  <script src="js/practicals.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated index.html successfully ({len(html_content)} chars)")
