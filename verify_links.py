import os
import re

def check_site():
    errors = []
    html_files = []
    
    # Collect all HTML files
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
                
    # Regex to find href="..."
    href_pattern = re.compile(r'href="([^"]+)"')
    src_pattern = re.compile(r'src="([^"]+)"')
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        current_dir = os.path.dirname(filepath)
            
        # Check hrefs
        for match in href_pattern.finditer(content):
            link = match.group(1)
            # Ignore absolute URLs, mailto, tel, anchors
            if link.startswith('http') or link.startswith('mailto:') or link.startswith('#') or link == '#':
                continue
                
            # Resolve relative path
            target_path = os.path.normpath(os.path.join(current_dir, link))
            
            if not os.path.exists(target_path):
                errors.append(f"Broken HREF in {filepath}: {link} (resolved to {target_path})")
                
        # Check srcs
        for match in src_pattern.finditer(content):
            link = match.group(1)
            if link.startswith('http') or link.startswith('//'):
                continue
                
            target_path = os.path.normpath(os.path.join(current_dir, link))
            
            if not os.path.exists(target_path):
                errors.append(f"Broken SRC in {filepath}: {link} (resolved to {target_path})")
                
    if not errors:
        print("SUCCESS: No broken local links or missing assets found!")
    else:
        print(f"FOUND {len(errors)} ERRORS:")
        for e in set(errors):  # Use set to deduplicate
            print(e)

if __name__ == "__main__":
    check_site()
