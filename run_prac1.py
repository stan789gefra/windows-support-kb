import json
import io
import contextlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('practicals_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

prac1 = data[0] # Practical 1
items = prac1['sections'][0]['items']

img_count = 0
for idx, it in enumerate(items):
    if it['type'] == 'code':
        code = it['code']
        # We will execute the code and capture stdout and plot if any
        plt.clf()
        plt.close('all')
        
        output_io = io.StringIO()
        # Mock plt.show to save plot
        def mock_show():
            global img_count
            fname = f"prac1_img{img_count}.png"
            path = f"assets/images/{fname}"
            plt.savefig(path, bbox_inches='tight', dpi=150)
            it['outputs'].append({
                "type": "image",
                "src": f"assets/images/{fname}",
                "alt": f"Practical 1 Plot {img_count+1}"
            })
            img_count += 1
            plt.clf()
            
        custom_globals = {
            'np': np,
            'plt': plt,
            'print': print
        }
        plt.show = mock_show
        
        try:
            with contextlib.redirect_stdout(output_io):
                exec(code, custom_globals)
        except Exception as e:
            print(f"Error in cell {it['cell_index']}: {e}")
            
        text_out = output_io.getvalue().strip()
        if text_out:
            it['outputs'].insert(0, {
                "type": "text",
                "content": text_out
            })

with open('practicals_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Practical 1 executed! Created {img_count} plot images and captured all outputs.")
