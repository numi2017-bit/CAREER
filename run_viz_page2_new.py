import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 (추정치 기반 전략 데이터)
chefs = ['최강록', '안성재', '백종원', '최현석', '정지선', '이영숙', '임성근', '에드워드 리']
reach = [85, 95, 98, 88, 75, 65, 80, 70] # 대중적 인지도 (X축)
loyalty = [98, 55, 60, 65, 50, 45, 82, 75] # 팬덤 응집력 (Y축)
bubble_size = [2500, 1800, 2000, 1500, 1000, 800, 1500, 1200] # 화제성 강도

fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
ax.set_facecolor('#121212')

# 4분면 가이드라인
plt.axvline(x=70, color='#333', linestyle='--', linewidth=2)
plt.axhline(y=70, color='#333', linestyle='--', linewidth=2)

# 버블 차트 (Scatter)
for i, chef in enumerate(chefs):
    color = '#E50914' if chef == '최강록' else '#50E3C2' if chef == '임성근' else '#666'
    alpha = 0.9 if chef in ['최강록', '임성근'] else 0.4
    
    plt.scatter(reach[i], loyalty[i], s=bubble_size[i], color=color, alpha=alpha, edgecolors='white', linewidth=2)
    plt.text(reach[i], loyalty[i], chef, ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# 분면 이름 (Labeling)
plt.text(85, 90, 'SUPER CHARACTER IP\n(팬덤 & 대중성 장악)', color='#E50914', fontsize=18, fontweight='bold', alpha=0.8)
plt.text(85, 45, 'MASS PUBLIC\n(대중적 인지도군)', color='#ADB5BD', fontsize=15, alpha=0.6)
plt.text(45, 90, 'FANATIC NICHE\n(강력한 마니아층)', color='#ADB5BD', fontsize=15, alpha=0.6)
plt.text(45, 45, 'RISING STARS\n(신규 발굴 대상)', color='#ADB5BD', fontsize=15, alpha=0.6)

# 축 및 제목 설정
plt.title('ASSET: 셰프 IP 포트폴리오 분석 매트릭스', fontsize=28, color='white', fontweight='bold', pad=40)
plt.xlabel('Mass Reach (대중적 인지도/조회수) →', fontsize=16, color='#ADB5BD')
plt.ylabel('Engagement Intensity (팬덤 응집력/로열티) →', fontsize=16, color='#ADB5BD')

# 격자 숨기기 및 영역 조정
plt.xlim(30, 110)
plt.ylim(30, 110)
ax.spines['bottom'].set_color('#333')
ax.spines['left'].set_color('#333')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 캡션
plt.text(32, 25, "※ 분석 데이터: 유튜브 댓글 참여율 및 소셜 버즈 공유 강도 기반 (Value Metrics 2026)", 
         fontsize=11, color="#6C757D", style='italic')

plt.tight_layout()
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_2_asset.png', dpi=200, bbox_inches='tight')

print("새로운 셰프 IP 포트폴리오 분석 매트릭스가 생성되었습니다.")
