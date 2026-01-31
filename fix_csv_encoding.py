
import os

files_to_fix = [
    r"c:\Users\pc\Desktop\mypyproject\CAREER\salary_benchmark_sources.csv"
]

for file_path in files_to_fix:
    if os.path.exists(file_path):
        try:
            # Try reading as UTF-8 first
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # If failed, try cp949
                with open(file_path, 'r', encoding='cp949') as f:
                    content = f.read()
            
            # Write back as UTF-8-SIG
            with open(file_path, 'w', encoding='utf-8-sig') as f:
                f.write(content)
            print(f"Fixed encoding for: {file_path}")
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")
