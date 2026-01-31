import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def analyze_economic_impact():
    """셰프별 경제적 미디어 가치 및 구독 방어 수익 분석"""
    
    # 1. 셰프별 조회수 데이터 (기존 분석 결과 바탕으로 하드코딩 - 데이터 정합성 유지)
    # 기존 데이터: 안성재(117.9M), 백종원(73.7M), 최현석(29.8M), 임성근(3.1M) 등
    # 단위: 회
    chef_views = {
        '안성재': 117900000,
        '백종원': 73700000,
        '최현석': 29800000,
        '최강록': 15200000, # 추정치
        '정지선': 31600000, # 추정치
        '임성근': 3100000   # 추정치
    }
    
    # 미디어 가치 단가 (CPV 30원 가정 - 업계 통상적 유튜브 브랜디드 콘텐츠 효율)
    CPV = 30 
    
    # 데이터프레임 변환
    df = pd.DataFrame(list(chef_views.items()), columns=['Chef', 'Views'])
    df['Media_Value'] = df['Views'] * CPV
    df = df.sort_values('Media_Value', ascending=False)
    
    # 2. 구독 방어 가치 시뮬레이션
    risk_users = 4356 # 위험팬 수
    subscription_fee = 13500 # 월 구독료
    retention_rate = 0.3 # 캠페인 성공률 가정 (30%)
    
    monthly_save = risk_users * retention_rate * subscription_fee
    yearly_save = monthly_save * 12
    
    # 시각화
    fig = plt.figure(figsize=(16, 8))
    gs = fig.add_gridspec(1, 2, width_ratios=[2, 1])
    
    # 차트 1: 셰프별 창출 미디어 가치
    ax1 = fig.add_subplot(gs[0])
    bars = ax1.barh(df['Chef'], df['Media_Value'], color=['#E50914' if x == df['Media_Value'].max() else '#555555' for x in df['Media_Value']])
    ax1.invert_yaxis()
    
    # 값 표시 (억 단위)
    for bar in bars:
        width = bar.get_width()
        ax1.text(width + 100000000, bar.get_y() + bar.get_height()/2, 
                 f'{width/100000000:.1f}억 원', 
                 va='center', fontweight='bold', color='white', fontsize=12)
        
    ax1.set_title('셰프별 창출 미디어 가치 (추정)', fontsize=16, fontweight='bold', pad=20)
    ax1.set_xlabel('가치 환산액 (원)', fontsize=12)
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    
    # 차트 2: 구독 방어 기대 수익 (단일 바 차트)
    ax2 = fig.add_subplot(gs[1])
    revenue_types = ['월간 방어 수익', '연간 기대 수익']
    revenue_values = [monthly_save, yearly_save]
    
    bars2 = ax2.bar(revenue_types, revenue_values, color=['#FFA726', '#66BB6A'], width=0.5)
    
    # 값 표시 (천만/억 단위)
    for i, bar in enumerate(bars2):
        height = bar.get_height()
        label = f'{height/100000000:.2f}억 원' if height >= 100000000 else f'{height/10000:.0f}만 원'
        ax2.text(bar.get_x() + bar.get_width()/2, height + 5000000, 
                 label, 
                 ha='center', va='bottom', fontweight='bold', color='white', fontsize=14)
        
    ax2.set_title('위험팬 방어 시 기대 수익\n(Target: 4,356명, 성공률 30%)', fontsize=16, fontweight='bold', pad=20)
    ax2.set_ylim(0, yearly_save * 1.2) # 여백 확보
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'chef_monetization_impact.png'), dpi=150, bbox_inches='tight', facecolor='#121212')
    plt.close()
    print("✓ Saved: chef_monetization_impact.png")

if __name__ == "__main__":
    analyze_economic_impact()
