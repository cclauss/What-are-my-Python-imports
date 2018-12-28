# What are my Python imports?
### Find all the imports in a Python repo

Steps tested on macOS:
1. cd to the root of you Python project
2. grep -r import . > files.txt
3. python3 find_imports.py
