import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

site_packages = os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages')

my_pth = os.path.join(site_packages, 'my.pth')

with open(my_pth, 'r', encoding='utf8') as f:
    lines = [i.strip() for i in f.readlines()]

if this_dir not in lines:
    lines.append(this_dir)

with open(my_pth, 'w', encoding='utf8') as f:
    f.writelines([i + '\n' for i in lines])

with open(my_pth, 'r', encoding='utf8') as f:
    print(f.read())
    
input()