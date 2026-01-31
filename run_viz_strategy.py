import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background') 

# 1. 팬덤 응집도 TOP 5 데이터
chefs_engagement = ['최강록', '백종원', '최현석', '안성재', '정지선']
rates = [0.057, 0.039, 0.029, 0.024, 0.024]

plt.figure(figsize=(10, 6))
colors = ['#E50914' if x == '최강록' else '#444444' for x in chefs_engagement]
bars = plt.bar(chefs_engagement, rates, color=colors, edgecolor='white', alpha=0.8)

plt.title('팬덤 응집도 TOP 5 (댓글 참여율)', fontsize=16, pad=20, fontweight='bold', color='#E50914')
plt.ylabel('반응률 (%)', color='#888')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.001, f'{height}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.tight_layout()
# 흑백요리사 폴더로 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\fandom_top5.png')

# 2. IP 포트폴리오 맵
views = [117, 73, 15, 3] # 백만 단위
loyalty = [0.024, 0.039, 0.057, 0.311]
names = ['안성재', '백종원', '최강록', '임성근']

plt.figure(figsize=(10, 7))
plt.scatter(views, loyalty, s=500, c=['#444', '#666', '#E50914', '#FFD700'], alpha=0.7, edgecolors='white')

for i, txt in enumerate(names):
    plt.annotate(txt, (views[i], loyalty[i]), xytext=(10,10), textcoords='offset points', fontsize=12, fontweight='bold')

plt.title('IP 포트폴리오 전략 분석', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('대중성 (조회수) -> 규모(Scale)', color='#888')
plt.ylabel('팬덤 로열티 (참여율 %) -> 밀도(Density)', color='#888')

plt.grid(linestyle=':', alpha=0.3)
plt.tight_layout()
# 흑백요리사 폴더로 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\ip_portfolio_map.png')

print("차트가 '흑백요리사' 폴더에 성공적으로 생성되었습니다.")
