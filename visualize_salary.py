
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Korean support (malgun gothic for windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

BASE_DIR = r"c:\Users\pc\Desktop\mypyproject\CAREER"
GUIDE_CSV = os.path.join(BASE_DIR, "brand_marketer_salary_guide.csv")
COMPANY_CSV = os.path.join(BASE_DIR, "salary_data.csv")

def parse_range(value):
    """Parses string like '3,600 ~ 4,000' to average float."""
    if isinstance(value, str):
        value = value.replace(',', '').replace('만원', '')
        if '~' in value:
            parts = value.split('~')
            try:
                low = float(parts[0].strip())
                high = float(parts[1].strip())
                return (low + high) / 2
            except:
                return 0
        else:
            try:
                return float(value.strip())
            except:
                return 0
    return 0

def parse_range_min_max(value):
    """Parses string like '3,600 ~ 4,000' to (min, max)."""
    if isinstance(value, str):
        value = value.replace(',', '').replace('만원', '')
        if '~' in value:
            parts = value.split('~')
            try:
                low = float(parts[0].strip())
                high = float(parts[1].strip())
                return low, high
            except:
                return 0, 0
        else:
            try:
                val = float(value.strip())
                return val, val
            except:
                return 0, 0
    return 0, 0


def visualize_market_guide():
    try:
        df = pd.read_csv(GUIDE_CSV, encoding='utf-8')
    except:
        df = pd.read_csv(GUIDE_CSV, encoding='cp949')
    
    # Clean up column names
    df.columns = [c.strip() for c in df.columns]
    
    # Parse Salary Ranges
    df['Parsed_Data'] = df['예상 평균 연봉 (만원)'].apply(parse_range_min_max)
    df['Min_Salary'] = df['Parsed_Data'].apply(lambda x: x[0])
    df['Max_Salary'] = df['Parsed_Data'].apply(lambda x: x[1])
    
    # Parse Top Tier
    def parse_top(val):
        if isinstance(val, str):
            val = val.replace(',', '').replace('만원', '').strip()
            # Handle "6000 이상" etc
            val = val.replace('이상', '').strip()
            try:
                return float(val)
            except:
                return None
        return None

    df['Top_Salary'] = df['상위권 연봉 (만원)'].apply(parse_top)

    # Handle single value case (Min == Max) for better visualization
    # If Min == Max, we'll create a small artificial visual range or just plot it clearly
    # But better strategy: Use a standard background bar for context, or just make sure it's visible.
    
    # Determine plot settings
    df['Label'] = df['직무'] + "\n(" + df['연차/직급'] + ")"
    x = range(len(df))
    
    plt.figure(figsize=(14, 7))
    
    # 1. Plot the "Range" bars (Floating bars)
    # If Min != Max, width = Max - Min. If Min == Max, width = small (to show a line)
    bar_heights = df['Max_Salary'] - df['Min_Salary']
    bar_heights = bar_heights.apply(lambda h: max(h, 50)) # Ensure at least 50만원 height for visibility
    
    bars = plt.bar(x, bar_heights, bottom=df['Min_Salary'], 
                   color='#87CEEB', edgecolor='blue', alpha=0.6, label='평균 연봉 범위', width=0.5)
    
    # 2. Plot "Top Tier" markers
    # valid_top = df.dropna(subset=['Top_Salary'])
    plt.scatter(x, df['Top_Salary'], color='red', marker='*', s=150, zorder=10, label='상위권(Top Tier)')
    
    # 3. Add Labels
    for idx, row in df.iterrows():
        # Min Label
        plt.text(idx, row['Min_Salary'] - 150, f"{int(row['Min_Salary'])}", ha='center', va='top', fontsize=9)
        # Max Label (only if distinct from Min)
        if row['Max_Salary'] > row['Min_Salary'] + 50:
            plt.text(idx, row['Max_Salary'] + 100, f"{int(row['Max_Salary'])}", ha='center', va='bottom', fontsize=9)
        
        # Top Label
        if pd.notnull(row['Top_Salary']):
            plt.text(idx, row['Top_Salary'] + 100, f"Top {int(row['Top_Salary'])}", 
                     ha='center', va='bottom', color='red', fontweight='bold', fontsize=9)

    plt.title('브랜드 마케터 및 관련 직무 시장 연봉 가이드 (단위: 만원)', fontsize=16, pad=20)
    plt.ylabel('연봉 (만원)', fontsize=12)
    plt.xticks(x, df['Label'], rotation=0)
    
    # Add grid and legend
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    

    # Set Y-axis limit to accommodate text
    # Calculate max Y value
    top_max = df['Top_Salary'].max()
    curr_max = df['Max_Salary'].max()
    # Handle NaN in Top_Salary which results in NaN max
    if pd.isna(top_max):
        top_max = 0
    y_max = max(top_max, curr_max) + 1000
    
    # Calculate min Y value
    y_min = df['Min_Salary'].min() - 1000
    plt.ylim(max(0, y_min), y_max)
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    save_path = os.path.join(BASE_DIR, "brand_marketer_salary_chart_v2.png")
    plt.savefig(save_path)
    print(f"Saved chart to {save_path}")

def visualize_personal_comparison(user_salary=3500, new_hire_salary=3200, market_avg_min=3800, market_avg_max=4500):
    """
    Visualizes My Salary vs Company New Hire vs Market Standard for 3-Year experience.
    """
    labels = ['회사 신입 공고', '내 연봉 (3년차)', '시장 평균 (3년차)']
    values = [new_hire_salary, user_salary, (market_avg_min + market_avg_max) / 2]
    
    plt.figure(figsize=(10, 6))
    
    # Define colors: Gray for New Hire, Blue for User, Green for Market
    colors = ['#B0B0B0', '#1E90FF', '#32CD32']
    
    bars = plt.bar(labels, values, color=colors, alpha=0.8, width=0.5)
    
    # Draw Market Range Box behind the Market Bar
    plt.fill_between([1.8, 2.2], market_avg_min, market_avg_max, color='#32CD32', alpha=0.2, label='시장 연봉 범위')
    
    # Add values on top of bars
    for i, v in enumerate(values):
        plt.text(i, v + 50, f"{int(v)}", ha='center', va='bottom', fontweight='bold', fontsize=12)

    # Gap Annotations
    # 1. New Hire vs My Salary
    gap_new = user_salary - new_hire_salary
    plt.annotate(f"+{gap_new}만원 (겨우 +{int((gap_new/new_hire_salary)*100)}%)", 
                 xy=(0.5, (user_salary + new_hire_salary)/2), 
                 xytext=(0.5, (user_salary + new_hire_salary)/2 + 200),
                 ha='center', fontsize=10, color='red',
                 arrowprops=dict(arrowstyle='-[, widthB=1.5, lengthB=0.2', color='red'))

    # 2. My Salary vs Market Avg
    market_avg = values[2]
    gap_market = market_avg - user_salary
    plt.annotate(f"격차: {int(gap_market)}만원", 
                 xy=(1.5, (user_salary + market_avg)/2), 
                 xytext=(1.5, (user_salary + market_avg)/2 + 200),
                 ha='center', fontsize=10, color='blue',
                 arrowprops=dict(arrowstyle='-[, widthB=1.5, lengthB=0.2', color='blue'))

    plt.ylim(2500, 5500)
    plt.title(f'연봉 협상 분석: 3년차 경력 가치 비교', fontsize=15)
    plt.ylabel('연봉 (만원)')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    save_path = os.path.join(BASE_DIR, "personal_salary_gap_analysis.png")
    plt.savefig(save_path)
    print(f"Saved chart to {save_path}")

def visualize_company_ranking():
    try:
        df = pd.read_csv(COMPANY_CSV, encoding='utf-8')
    except:
        df = pd.read_csv(COMPANY_CSV, encoding='cp949')

    # Remove extra quotes if present in csv parsing
    df.columns = [c.replace('"', '').strip() for c in df.columns]
    
    # Clean parsed data column name might assume header
    if '평균연봉 (만원)' not in df.columns:
         # Try to find the column that looks like salary
         for col in df.columns:
             if '평균연봉' in col:
                 df.rename(columns={col: '평균연봉 (만원)'}, inplace=True)
                 break
    
    df['Clean_Salary'] = df['평균연봉 (만원)'].astype(str).str.replace(',', '').str.replace('"', '').str.strip().astype(float)
    df['Clean_Company'] = df['회사명'].astype(str).str.replace('"', '').str.strip()

    # Sort
    df = df.sort_values('Clean_Salary', ascending=True)

    plt.figure(figsize=(12, 8))
    plt.barh(df['Clean_Company'], df['Clean_Salary'], color='salmon', alpha=0.8)
    
    for idx, value in enumerate(df['Clean_Salary']):
        plt.text(value + 100, idx, f"{int(value)}", va='center')

    plt.title('주요 기업 마케팅/광고/MD 부서 평균 연봉 (단위: 만원)', fontsize=15)
    plt.xlabel('연봉 (만원)')
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    save_path = os.path.join(BASE_DIR, "company_salary_comparison.png")
    plt.savefig(save_path)
    print(f"Saved chart to {save_path}")

def visualize_platform_comparison(user_salary=3500, new_hire_salary=3200):
    """
    Visualizes detailed platform-specific benchmarks vs Personal Salary.
    """
    csv_path = os.path.join(BASE_DIR, "salary_benchmark_sources.csv")
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
    except:
        df = pd.read_csv(csv_path, encoding='cp949')

    # Prepare Data
    # Add User and New Hire as rows for uniform plotting, or plot them as vertical lines/distinct bars
    # Let's plot platforms as bars, and overlay User/New Hire as vertical dashed lines for "Benchmark" effect
    
    df['Label'] = df['플랫폼'] + "\n(" + df['평균 연봉'].astype(str) + ")"
    df['Avg_Salary'] = pd.to_numeric(df['평균 연봉'], errors='coerce')
    
    # Sort by salary
    df = df.sort_values('Avg_Salary', ascending=True)
    
    plt.figure(figsize=(12, 7))
    
    # Plot Platform Bars
    bars = plt.barh(df['플랫폼'], df['Avg_Salary'], color='#66c2a5', alpha=0.7, label='플랫폼별 평균 (3년차)')
    
    # Add labels on bars
    for i, v in enumerate(df['Avg_Salary']):
        plt.text(v + 50, i, f"{int(v)}만원", va='center', fontweight='bold')
    
    # Add Vertical Lines for Personal Context
    plt.axvline(x=user_salary, color='#1E90FF', linestyle='-', linewidth=2, label=f'내 연봉 ({user_salary})')
    plt.axvline(x=new_hire_salary, color='#B0B0B0', linestyle='--', linewidth=2, label=f'신입 공고 ({new_hire_salary})')
    
    # Add gap text for User
    # Find the max salary in platforms to place the text nicely? No, just near the line.
    for i, row in df.iterrows():
        gap = row['Avg_Salary'] - user_salary
        if gap > 0:
            plt.text(row['Avg_Salary'] + 200, i - 0.2, f"(+{int(gap)})", color='red', fontsize=9)
        else:
            plt.text(row['Avg_Salary'] + 200, i - 0.2, f"({int(gap)})", color='blue', fontsize=9)

    plt.title('주요 채용 플랫폼별 3년차 마케터 평균 연봉 vs 내 연봉', fontsize=16)
    plt.xlabel('연봉 (만원)')
    plt.grid(axis='x', linestyle='--', alpha=0.4)
    plt.xlim(2500, 5500)
    plt.legend(loc='lower right')
    plt.tight_layout()
    
    save_path = os.path.join(BASE_DIR, "platform_benchmark_comparison.png")
    plt.savefig(save_path)
    print(f"Saved chart to {save_path}")

if __name__ == "__main__":
    # visualize_market_guide() # Skipping previous ones to focus on new request
    # visualize_company_ranking()
    # visualize_personal_comparison(3500, 3200, 3800, 4500)
    visualize_platform_comparison(3500, 3200)
