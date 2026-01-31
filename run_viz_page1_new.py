import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
ax.set_facecolor('#121212')
ax.axis('off')

# 1. 제목 및 서브타이틀 (시즌 1 리스크의 전이 강조)
plt.text(0.05, 0.92, '[CASE STUDY] 시즌 1 리스크가 시즌 2에 미치는 영향', ha='left', va='center', fontsize=30, color='white', fontweight='bold')
plt.text(0.05, 0.86, '"시즌 1 출연진의 사후 논란은 브랜드 신뢰도를 파괴하고, 차기 시즌의 이탈 명분이 된다"', ha='left', va='center', fontsize=16, color='#E50914', style='italic')
# 헤더 라인
ax.add_patch(patches.Rectangle((0.05, 0.82), 0.9, 0.005, color='#E50914'))

# 2. 핵심 리스크 메트릭스
stats = [
    {"label": "S1 스타 리스크 전이율", "value": "2.2배 급증", "color": "#E50914"},
    {"label": "시즌 1 대비 불신 지수", "value": "+145%", "color": "#E50914"},
    {"label": "브랜드 피로도", "value": "CRITICAL", "color": "white"}
]

x_pos = 0.05
for s in stats:
    rect = patches.FancyBboxPatch((x_pos, 0.65), 0.28, 0.13, boxstyle="round,pad=0.01", facecolor='#1A1A1A', edgecolor='#333')
    ax.add_patch(rect)
    plt.text(x_pos + 0.14, 0.73, s['label'], ha='center', fontsize=14, color='#ADB5BD')
    plt.text(x_pos + 0.14, 0.68, s['value'], ha='center', fontsize=26, color=s['color'], fontweight='bold')
    x_pos += 0.31

# 3. 레이아웃: 좌측(이탈 드라이버) / 우측(시즌 1 리스크 사례)
plt.text(0.05, 0.58, '■ 시즌 2 이탈 유도 부정 이슈 (Risk Factor)', fontsize=18, color='white', fontweight='bold')

drivers = [
    {"label": "출연진 검증 시스템 불신 (시즌 1 여파)", "val": 51.5, "color": "#E50914", "tag": "CRITICAL"},
    {"label": "시즌 2 심사 공정성 우려", "val": 23.2, "color": "#F5A623", "tag": "HIGH"},
    {"label": "포맷 및 구성의 기시감", "val": 15.3, "color": "#666", "tag": "MODERATE"},
    {"label": "기타 가격 및 환경 요소", "val": 10.0, "color": "#333", "tag": "LOW"}
]

y_pos = 0.45
for d in drivers:
    ax.add_patch(patches.Rectangle((0.05, y_pos), 0.4, 0.025, color='#1A1A1A'))
    ax.add_patch(patches.Rectangle((0.05, y_pos), (d['val']/100)*0.4, 0.025, color=d['color']))
    plt.text(0.05, y_pos + 0.04, f"{d['label']} | {d['val']}%", fontsize=12, color='white')
    plt.text(0.46, y_pos + 0.005, d['tag'], fontsize=11, color=d['color'], fontweight='bold')
    y_pos -= 0.10

# --- 우측: [RE-CAP] 시즌 1 리스크의 실제 파급도 ---
news_rect = patches.FancyBboxPatch((0.55, 0.12), 0.4, 0.46, boxstyle="round,pad=0.01", facecolor='#1A1A1A', edgecolor='#E50914', linewidth=1.5)
ax.add_patch(news_rect)

plt.text(0.58, 0.52, '⚠️ 시즌 1 출연진 사후 논란 사례 (S1 Legacy Risk)', fontsize=15, color='#E50914', fontweight='bold')
plt.text(0.58, 0.44, '● 트리플스타(S1): 사생활 및 행태 논란 → S2 검증 비판', fontsize=12, color='white')
plt.text(0.58, 0.38, '● 이영숙(S1): 채무 불이행 이슈 → 브랜드 도덕성 추락', fontsize=12, color='white')
plt.text(0.58, 0.32, '● 유비빔(S1): 과거사 사과문 → 무분별한 섭외 비판', fontsize=12, color='white')

ax.add_patch(patches.Rectangle((0.58, 0.25), 0.34, 0.001, color='#333'))
plt.text(0.58, 0.20, "결론: 시즌 1 출연진의 리스크는 단순히 과거의 문제가 아님.\n'넷플릭스 셰프 = 리스크'라는 인식이 시즌 2의 최대 위협.", 
         fontsize=11, color='#ADB5BD', linespacing=1.6)

plt.text(0.05, 0.05, "※ 본 보고서는 2024년 10-11월 발생한 시즌 1 출연진 논란이 시즌 2 흥행에 미친 상관관계를 분석함.", 
         fontsize=10, color="#6C757D")

plt.tight_layout()
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_1_diagnosis.png', dpi=200, bbox_inches='tight')

print("시즌 1/2 관계를 명확히 정립한 전략 리포트 1페이지가 생성되었습니다.")
