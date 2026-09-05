import re

with open('prensa.html', 'r', encoding='utf-8') as f:
    content = f.read()

grids = re.findall(r'<div class="prensa-grid">(.*?)</div>\s*</section>', content, re.DOTALL)

if len(grids) >= 3:
    first_grid = grids[0]
    third_grid = grids[2]
    
    articles = re.findall(r'<article class="prensa-card".*?</article>', first_grid, re.DOTALL)
    
    keep_in_first = []
    move_to_third = []
    
    for article in articles:
        if 'COMUNICADO URGENTE' in article:
            keep_in_first.append(article)
        elif '>INSTAGRAM' in article or '>X / REDES SOCIALES' in article:
            move_to_third.append(article)
        else:
            keep_in_first.append(article)
            
    new_first_grid = '\n'.join(keep_in_first)
    new_third_grid = third_grid + '\n' + '\n'.join(move_to_third)
    
    new_content = content.replace(first_grid, '\n' + new_first_grid + '\n')
    new_content = new_content.replace(third_grid, new_third_grid)
    
    with open('prensa.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully moved cards')
else:
    print('Error: Could not find 3 grids')
