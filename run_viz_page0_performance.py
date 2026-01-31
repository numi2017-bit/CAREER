import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(16, 9), facecolor='#0D0D0D')
ax.set_facecolor('#0D0D0D')
ax.axis('off')

# 1. 헤더
plt.text(0.05, 0.92, '01. 현황 및 성과: 시장권을 탈환한 구원 투수', ha='left', va='center', fontsize=30, color='white', fontweight='bold')
plt.text(0.05, 0.86, '"조회수 절대량을 넘어, 참여 밀도(Engagement) 1.82배 성장의 기록"', ha='left', va='center', fontsize=16, color='#E50914', style='italic')
ax.add_patch(patches.Rectangle((0.05, 0.82), 0.9, 0.005, color='#E50914'))

# 2. V자 반등 그래프 (Conceptual Line Chart)
ax_line = fig.add_axes([0.05, 0.15, 0.4, 0.55])
ax_line.set_facecolor('#161616')
weeks = ['-4주', '-2주', '방영직전(8위)', '방영후(1위)', '+2주', '+4주']
indices = [30, 20, 10, 95, 98, 92]
ax_line.plot(weeks, indices, marker='o', color='#E50914', linewidth=4, markersize=10)
ax_line.fill_between(weeks, indices, color='#E50914', alpha=0.1)
ax_line.set_title('브랜드 관심도 변화 (V자 반등)', color='white', fontsize=16, pad=20, fontweight='bold')
ax_line.tick_params(colors='white', labelsize=10)
for i, txt in enumerate(indices):
    ax_line.annotate(f"{txt}%", (weeks[i], indices[i]+3), color='white', ha='center', fontweight='bold')

# 3. 참여 밀도 비교 (Bar Chart)
ax_bar = fig.add_axes([0.55, 0.15, 0.35, 0.25])
ax_bar.set_facecolor('#161616')
labels = ['시즌 1', '시즌 2']
density = [271, 494]
bars = ax_bar.barh(labels, density, color=['#666', '#E50914'])
ax_bar.set_title('참여 밀도 (1M 조회당 댓글 수)', color='white', fontsize=14, pad=15)
ax_bar.tick_params(colors='white')
for bar in bars:
    width = bar.get_width()
    ax_bar.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width}개', va='center', color='white', fontweight='bold')

# 4. 하이라이트 지표 (Boxes)
stats = [
    {"label": "시장 점유율", "val": "35%+", "sub": "OTT 시장 1위 탈환"},
    {"label": "참여도 성장", "val": "1.82배", "sub": "시즌 1 대비 82%↑"},
    {"label": "글로벌 랭킹", "val": "TOP 10", "sub": "비영어권 TV 부문"}
]

y_box = 0.68
for s in stats:
    rect = patches.FancyBboxPatch((0.55, y_box), 0.35, 0.1, boxstyle="round,pad=0.01", facecolor='#1A1A1A')
    ax.add_patch(rect)
    plt.text(0.57, y_box + 0.05, s['label'], color='#ADB5BD', fontsize=12)
    plt.text(0.72, y_box + 0.05, s['val'], color='#E50914', fontsize=22, fontweight='bold')
    plt.text(0.83, y_box + 0.05, s['sub'], color='white', fontsize=10)
    y_box -= 0.13

# 캡션
plt.text(0.05, 0.05, "※ 분석 데이터: 2024.09~2026.01 넷플릭스 유저 로그 및 시장 점유율 데이터 기반", fontsize=10, color="#6C757D")

plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_0_performance.png', dpi=200, bbox_inches='tight')
print("성과 및 V자 반등 분석을 담은 0페이지 대시보드가 성공적으로 생성되었습니다.")
