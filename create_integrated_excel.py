
import pandas as pd
import os

base_dir = r"c:\Users\pc\Desktop\mypyproject\CAREER"
output_file = os.path.join(base_dir, "salary_analysis_report.xlsx")

files = {
    "플랫폼별_벤치마크": "salary_benchmark_sources.csv",
    "시장_연봉_가이드": "brand_marketer_salary_guide.csv",
    "주요기업_연봉리스트": "salary_data.csv"
}

try:
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for sheet_name, filename in files.items():
            file_path = os.path.join(base_dir, filename)
            if os.path.exists(file_path):
                try:
                    # Generic reader trying utf-8-sig first then cp949
                    try:
                        df = pd.read_csv(file_path, encoding='utf-8-sig')
                    except UnicodeDecodeError:
                        df = pd.read_csv(file_path, encoding='cp949')
                    
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    print(f"Added sheet: {sheet_name}")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
            else:
                print(f"File not found: {filename}")
                
    print(f"Successfully created: {output_file}")

except Exception as e:
    print(f"Detailed Error: {e}")
    # Fallback to xlsxwriter if openpyxl is missing
    try:
        print("Retrying with xlsxwriter...")
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            for sheet_name, filename in files.items():
                file_path = os.path.join(base_dir, filename)
                if os.path.exists(file_path):
                    try:
                        try:
                            df = pd.read_csv(file_path, encoding='utf-8-sig')
                        except UnicodeDecodeError:
                            df = pd.read_csv(file_path, encoding='cp949')
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                    except:
                        pass
        print(f"Successfully created with xlsxwriter: {output_file}")
    except Exception as e2:
        print(f"Failed with xlsxwriter too: {e2}")
