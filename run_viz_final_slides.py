import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_base_slide(title, subtitle):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#0D0D0D')
    ax.set_facecolor('#0D0D0D')
    ax.axis('off')
    # 상단 헤더 라인
    ax.add_patch(patches.Rectangle((0.05, 0.82), 0.9, 0.005, color='#E50914'))
    plt.text(0.05, 0.90, title, ha='left', va='center', fontsize=30, color='white', fontweight='bold')
    plt.text(0.05, 0.85, subtitle, ha='left', va='center', fontsize=16, color='#E50914', style='italic')
    return fig, ax

# --- Page 3: 전략 로드맵 (상세 카드형) ---
fig, ax = create_base_slide('STRATEGY: IP 가치 극대화 로드맵', '"푸시 알림은 시작일 뿐, 우리의 목표는 IP 유니버스다."')

cards = [
    {
        "step": "STEP 01", "title": "Defense: 구독 가치 재정립", 
        "solve": "식당 예약 우선권(Fast Track) 추첨",
        "desc": "13,500원 구독료를 '예약권 가치'로 전환하여\n가격 저항(89건)을 즉각적 혜택으로 해소",
        "color": "#E50914", "x": 0.05
    },
    {
        "step": "STEP 02", "title": "Quality: 유저 참여형 심사", 
        "solve": "시즌 3 '국민 심사단 100인' 도입",
        "desc": "불투명한 인성/공정성 불만을 '참여형 효능감'으로\n반전시켜 코어 팬덤을 제작 파트너로 포섭",
        "color": "#F5A623", "x": 0.36
    },
    {
        "step": "STEP 03", "title": "Expansion: IP 유니버스 가동", 
        "solve": "최강록x임성근 더블 엔진 스핀오프",
        "desc": "팬덤 타겟 '만화책 식당' 등 전용 콘텐츠 런칭\n위험팬 4,356명 해지 방어 (ROI 2.1억 실현)",
        "color": "#50E3C2", "x": 0.67
    }
]

for c in cards:
    # 카드 배경
    rect = patches.FancyBboxPatch((c['x'], 0.15), 0.28, 0.6, boxstyle="round,pad=0.02", facecolor='#161616', edgecolor='#222', linewidth=1)
    ax.add_patch(rect)
    # 상단 컬러 띠
    ax.add_patch(patches.Rectangle((c['x'], 0.73), 0.28, 0.02, color=c['color']))
    
    # 간격 최적화 (y좌표 미세 조정)
    plt.text(c['x']+0.02, 0.67, c['step'], fontsize=18, color=c['color'], fontweight='bold')
    plt.text(c['x']+0.02, 0.61, c['title'], fontsize=16, color='white', fontweight='bold')
    
    # 구분선
    ax.add_patch(patches.Rectangle((c['x']+0.02, 0.57), 0.24, 0.001, color='#333'))
    
    plt.text(c['x']+0.02, 0.52, "■ SOLUTION", fontsize=12, color=c['color'], fontweight='bold')
    plt.text(c['x']+0.02, 0.47, c['solve'], fontsize=13, color='white', fontweight='bold')
    
    plt.text(c['x']+0.02, 0.38, "■ IMPACT", fontsize=12, color=c['color'], fontweight='bold')
    plt.text(c['x']+0.02, 0.28, c['desc'], fontsize=12, color='#ADB5BD', linespacing=1.6, va='top')

plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_3_roadmap.png', dpi=200, bbox_inches='tight')

# --- Page 4: 실행 과제 및 골든타임 (와이드 레이아웃) ---
fig, ax = create_base_slide('EXECUTION: 2.1억을 지키는 3대 액션', '"위험기(Churn Zone)를 수익 창출의 골든타임으로"')

actions = [
    {"num": "01", "title": "구독 유인 (Reward)", "detail": "셰프 식당 패스트트랙 이벤트", "effect": "구독 유지 동기부여 및 락인(Lock-in) 강화"},
    {"num": "02", "title": "참여 유도 (Interactive)", "detail": "국민 심사단 100인 공개 모집", "effect": "제작 파트너 격상을 통한 공정성 논란 종식"},
    {"num": "03", "title": "지속 노출 (Retention)", "detail": "수요일 밤 10시 정기 푸시 (최강록)", "effect": "미공개 컷 제공으로 습관적 재방문 유도"}
]

y_top = 0.70
for a in actions:
    # 행 배경
    ax.add_patch(patches.FancyBboxPatch((0.05, y_top-0.15), 0.55, 0.16, boxstyle="round,pad=0.01", facecolor='#161616'))
    plt.text(0.08, y_top-0.03, a['num'], fontsize=22, color='#E50914', fontweight='bold')
    plt.text(0.14, y_top-0.03, a['title'], fontsize=18, color='white', fontweight='bold')
    plt.text(0.14, y_top-0.08, f"내용: {a['detail']}", fontsize=14, color='#ADB5BD')
    plt.text(0.14, y_top-0.12, f"효과: {a['effect']}", fontsize=14, color='#ADB5BD')
    y_top -= 0.20

# 골든타임 스페셜 카드 (우측) - 왼쪽 박스들과 높이 대칭 맞춤 (0.71-0.15 = 0.56)
golden_rect = patches.FancyBboxPatch((0.65, 0.15), 0.3, 0.56, boxstyle="round,pad=0.01", facecolor='#1A1A1A', edgecolor='#50E3C2', linewidth=2)
ax.add_patch(golden_rect)
plt.text(0.8, 0.64, "Golden Time Care", ha='center', fontsize=24, color='#50E3C2', fontweight='bold')
plt.text(0.8, 0.54, "WED 22:00 PUSH", ha='center', fontsize=18, color='white', fontweight='bold')

plt.text(0.68, 0.44, "● 최강록 미공개 서사(B-컷)", fontsize=14, color='white')
plt.text(0.68, 0.38, "● 임성근 바이럴 숏폼 레시피", fontsize=14, color='white')
plt.text(0.68, 0.32, "● CU 콜라보 2차 상품 상시화", fontsize=14, color='white')

# ROI 강조 배지
plt.text(0.8, 0.21, "PROJECTION\nROI 2.1억 원", ha='center', fontsize=20, color='#50E3C2', fontweight='bold', bbox=dict(facecolor='none', edgecolor='#50E3C2', boxstyle='round,pad=0.5'))

plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\report_page_4_execution.png', dpi=200, bbox_inches='tight')

print("디자인과 가독성이 개선된 최종 전략 슬라이드가 생성되었습니다.")
