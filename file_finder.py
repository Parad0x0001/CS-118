"""
File Tree Program / Largest File Finder
Author: Parad0x
v1.2
03/01/22
This program lists all files within the specified folder while also displaying the largest 10 files found.
"""
from os.path import join, basename, getsize, exists
from os import walk, sep
from filecmp import cmp

start_dir = input("Enter the start directory: ")

if not exists(start_dir):
    print(f"I couldn't find the file path `{start_dir}`")
    exit()
    
f_list, d_list, fil = {},{},0

for root, dirs, files in walk(start_dir):
    level = root.replace(start_dir, '').count(sep)
    print(root)
    print(f"{' ' * 3 * (level)+'>'}{basename(root)}{sep}")
    for f in files:
        print(f"{(' ' * 4 * (level)+'>')}{f}")
        fil+=1
        d_list |= {join(root,cfile):join(root,f) for cfile in files if cmp((join(root,f)), join(root,cfile)) and not join(root,f) == join(root,cfile)}
        d_list |= {v:join(root,f) for v in f_list.values() if cmp((join(root,f)), v) and not join(root,f) == v}
    f_list |= {getsize(join(root,k)):join(root,k) for k in files if f_list.get(getsize(join(root,k))) is None}

f_list_sorted = sorted(f_list, reverse=True)
print(f"Finished scanning {fil} files!\nHere are the largest {min(10, len(f_list_sorted))} files!\n")
for i in range(min(10, len(f_list_sorted))):
    print(f"{i+1} -> {f_list[f_list_sorted[i]]} | {f_list_sorted[i]//1024:,d} KB")
if len(d_list) > 0:
    print("\nDuplicate Files!")
    for k,v in d_list.items():
        print(f"{k} | {v}")
