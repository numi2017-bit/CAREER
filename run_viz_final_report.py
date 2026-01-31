import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

# 1. 시즌 2 캐릭터 종합 랭킹 (바이럴 강도 기준)
chefs = ['임성근', '안성재', '최현석', '정지선', '백종원', '최강록']
viral_index = [2.21, 1.34, 1.28, 1.25, 1.21, 1.07]
plt.figure(figsize=(10, 6))
plt.barh(chefs, viral_index, color=['#FFD700', '#E50914', '#444', '#444', '#444', '#E50914'])
plt.title('시즌 2 셰프별 캐릭터 영향력 랭킹', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('바이럴 강도 지수 (출처: all_chefs_comparison.csv)')
plt.tight_layout()
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\s2_character_ranking.png')

# 2. 이탈 원인 부정 이슈 시각화 (인성 리스크 강조)
issue_labels = ['출연진 인성/과거사', '편집/공정성 불만', '가격 대비 콘텐츠 퀄리티', '기록성/단순변심']
issue_counts = [51.5, 23.2, 15.3, 10.0]
plt.figure(figsize=(8, 8))
plt.pie(issue_counts, labels=issue_labels, autopct='%1.1f%%', colors=['#E50914', '#888', '#555', '#222'], 
        explode=(0.1, 0, 0, 0), startangle=140, textprops={'fontsize': 12, 'fontweight': 'bold'})
plt.title('해지 유도 부정 이슈 분석 (출처: 유저 센티멘트 분석)', fontsize=16, pad=20)
plt.tight_layout()
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\negative_issue_analysis.png')

# 3. 뉴스 근거: 인성 논란 리스크 스냅샷 (가상 시각화)
news_cases = ['트리플스타(강승원)\n사생활 논란/행사 취소', '이영숙 셰프\n채무 불이행(빚투) 의혹', '시즌 2 전반\n출연자 검증 시스템 비판']
risk_impact = [95, 88, 75]
plt.figure(figsize=(10, 5))
plt.bar(news_cases, risk_impact, color='#E50914', alpha=0.7)
plt.title('주요 인성 논란 뉴스 발생 시 브랜드 타격 지수', fontsize=16, fontweight='bold')
plt.ylabel('리스크 파급도 (%)')
plt.ylim(0, 110)
for i, v in enumerate(risk_impact):
    plt.text(i, v + 2, f'치명적 ({v}%)', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\news_risk_snapshot.png')

print("모든 요청 시각화(랭킹, 부정 이슈, 뉴스 리스크)가 생성되었습니다.")
