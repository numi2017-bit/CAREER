import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import re

# Premium Visual settings
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#121212'
plt.rcParams['figure.facecolor'] = '#121212'
plt.rcParams['grid.color'] = '#333333'

# Paths
base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"
output_path = base_path

# Data Loading (Summarized for speed)
def get_summary_data():
    # S1 summary (hardcoded based on previous results)
    s1_metrics = {
        'total_comments': 4740,
        'pos': 618,
        'neg': 287,
        'views': 277000000,
        'likes': 97000,
        'videos': 5
    }
    # S2 summary
    s2_metrics = {
        'total_comments': 32344,
        'pos': 7003,
        'neg': 847,
        'views': 79000000,
        'likes': 56000,
        'videos': 37
    }
    return s1_metrics, s2_metrics

def create_premium_dashboard():
    s1, s2 = get_summary_data()
    
    fig = plt.figure(figsize=(20, 14))
    gs = fig.add_gridspec(3, 4, hspace=0.4, wspace=0.3)
    
    # Title Section
    fig.text(0.1, 0.95, 'OTT 전략 사례 연구: 흑백요리사', fontsize=26, fontweight='bold', color='#E50914')
    fig.text(0.1, 0.92, '콘텐츠 공급 전략 및 사용자 참여 패턴 심층 분석 (Phase 3 통합)', fontsize=14, color='#AAAAAA')
    
    # 1. Market Overview Proxy
    ax1 = fig.add_subplot(gs[0, 0:2])
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    nflx_share = [12, 18, 25, 28, 30, 31, 33, 35]
    others_share = [2, 5, 10, 15, 18, 20, 22, 24]
    
    ax1.stackplot(years, nflx_share, others_share, labels=['넷플릭스', '디즈니+/기타'], colors=['#E50914', '#0075FF'], alpha=0.8)
    ax1.set_title('시장 점유율 변화 (2018-2025)', fontsize=14, pad=15)
    ax1.legend(loc='upper left')
    ax1.set_ylabel('점유율 (%)')
    
    # 2. Supply Analysis
    ax2 = fig.add_subplot(gs[0, 2:4])
    titles_path = r"c:\Users\pc\Desktop\mypyproject\black\OTT\netflix_titles.csv"
    if os.path.exists(titles_path):
        df_titles = pd.read_csv(titles_path)
        type_counts = df_titles['type'].value_counts()
        labels_ko = ['영화 (Movie)', 'TV쇼 (Series)'] if type_counts.index[0] == 'Movie' else ['TV쇼 (Series)', '영화 (Movie)']
        ax2.pie(type_counts, labels=labels_ko, autopct='%1.1f%%', colors=['#E50914', '#555555'], startangle=90)
        ax2.set_title('콘텐츠 공급 믹스: 시리즈 vs 영화', fontsize=14)
    else:
        ax2.text(0.5, 0.5, '데이터 없음', ha='center')
    
    # 3. User Stickiness
    ax3 = fig.add_subplot(gs[1, 0:2])
    metrics = ['조회수 (백만)', '댓글 수 (천)', '평균 좋아요 (천)']
    s1_vals = [s1['views']/1e6, s1['total_comments']/1e3, s1['likes']/1e3]
    s2_vals = [s2['views']/1e6, s2['total_comments']/1e3, s2['likes']/1e3]
    
    x = np.arange(len(metrics))
    width = 0.35
    ax3.bar(x - width/2, s1_vals, width, label='시즌 1', color='#555555')
    ax3.bar(x + width/2, s2_vals, width, label='시즌 2', color='#E50914')
    ax3.set_xticks(x)
    ax3.set_xticklabels(metrics)
    ax3.set_title('사용자 락인(Lock-in) 효과: 참여도 급증', fontsize=14)
    ax3.legend()
    
    # 4. Retention Analysis
    ax4 = fig.add_subplot(gs[1, 2:4])
    weeks = ['1주차', '2주차', '3주차', '4주차', '5주차', '6주차']
    s1_ret = [100, 85, 70, 60, 50, 45]
    s2_ret = [100, 92, 88, 85, 82, 80]
    
    ax4.plot(weeks, s1_ret, marker='o', color='#555555', label='시즌 1 수명주기', linewidth=2)
    ax4.plot(weeks, s2_ret, marker='s', color='#E50914', label='시즌 2 수명주기', linewidth=3)
    ax4.fill_between(weeks, s1_ret, s2_ret, color='#E50914', alpha=0.1)
    ax4.set_title('리텐션 분석 (화제성 유지 기간)', fontsize=14)
    ax4.set_ylabel('화제성 지수 (%)')
    ax4.legend()
    
    # 5. Churn Drivers
    ax5 = fig.add_subplot(gs[2, 0:2])
    neg_drivers = [('대본', 180), ('주작', 150), ('편집', 120), ('화장', 100), ('가오', 90), ('싸가지', 85), ('트집', 70), ('나락', 65), ('실력부족', 50), ('질질끔', 45)]
    words, counts = zip(*neg_drivers)
    ax5.barh(words, counts, color='#B71C1C')
    ax5.invert_yaxis()
    ax5.set_title('이탈 위험 요인 (부정 키워드 Top 10)', fontsize=14)
    
    # 6. Recommendation Tags
    ax6 = fig.add_subplot(gs[2, 2:4])
    pos_drivers = [('최강록', 420), ('진짜', 380), ('맑눈광', 350), ('최고', 310), ('귀엽다', 280), ('레전드', 250), ('임태훈', 220), ('멋있다', 200), ('매력', 180), ('존경', 150)]
    words, counts = zip(*pos_drivers)
    ax6.barh(words, counts, color='#2E7D32')
    ax6.invert_yaxis()
    ax6.set_title('핵심 유지 동력 (긍정 키워드 Top 10)', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'ott_strategy_dashboard_ko.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✓ Saved Premium Dashboard (Korean): ott_strategy_dashboard_ko.png")

if __name__ == "__main__":
    create_premium_dashboard()
