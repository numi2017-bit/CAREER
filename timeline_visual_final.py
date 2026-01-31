import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_content_release_timeline_final():
    """요소별 간격을 대폭 넓힌 울트라 와이드 로드맵 시각화"""
    
    # 캔버스 크기 대폭 확대 (가로로 길게)
    fig, ax = plt.figure(figsize=(24, 10)), plt.gca()
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # --- 1. 타임라인 축 (최하단 레이어) ---
    ax.plot([10, 170], [15, 15], color='white', linewidth=3, alpha=0.8)
    
    # 구간 구분 점선
    ax.plot([60, 60], [10, 90], color='#444444', linestyle=':', linewidth=1.5)
    ax.plot([120, 120], [10, 90], color='#444444', linestyle=':', linewidth=1.5)
    
    # 구간 제목 (가독성 위해 상단 배치)
    ax.text(35, 92, "PHASE 1: 방영 중", ha='center', va='center', color='#ffffff', fontsize=18, fontweight='bold')
    ax.text(90, 92, "PHASE 2: 종영 및 이탈 위험기", ha='center', va='center', color='#ffffff', fontsize=18, fontweight='bold')
    ax.text(150, 92, "PHASE 3: 비활동기 확장", ha='center', va='center', color='#ffffff', fontsize=18, fontweight='bold')
    
    # --- 2. 골든타임 케어 (하단 레이어 y=20~30) ---
    push_x_positions = [20, 35, 50, 65, 80]
    for px in push_x_positions:
        ax.text(px, 28, "[PUSH]", ha='center', va='bottom', color='#FFD700', fontsize=14, fontweight='bold')
        ax.plot([px, px], [15, 27], color='#FFD700', linewidth=1.5, linestyle='--')
    
    ax.text(45, 10, "● 수요일 밤 10시 미공개 라이브/클립 정기 푸시 (리텐션 케어)", ha='center', va='top', color='#FFD700', fontsize=15, fontweight='bold')

    # --- 3. 이탈 방어 존 (상단 레이어 y=60~75) ---
    bbox_churn = dict(boxstyle="round,pad=1.0", fc="white", ec="#E50914", lw=3)
    ax.text(90, 72, "🚨 CHURN ZONE (이탈 집중 관리)\n콘텐츠 부재로 인한 구독 해제 방어 구간", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='black', bbox=bbox_churn)
    
    # PHASE 2 구체적 실행 과제 (Action Items)
    actions_p2 = [
        "① [Reward] 출연 셰프 식당 예약권 추첨 (재유입 유인)",
        "② [Interactive] 시즌 3 국민 심사단 모집 시작 (신뢰 회복)",
        "③ [Retention] 정기 미공개 영상 & 비하인드 공개 (체류 연장)"
    ]
    for i, action in enumerate(actions_p2):
        ax.text(90, 58 - i*5, action, ha='center', va='center', color='#ffcccc', fontsize=15, fontweight='bold')

    # 화살표 (길이 조정)
    ax.annotate("", xy=(90, 17), xytext=(90, 42), arrowprops=dict(arrowstyle="fancy", color="#E50914", alpha=0.6, lw=3))

    # --- 4. 스핀오프 런칭 (중상단 레이어 y=40~55) ---
    # 박스를 더 크게, 글자와 겹침 없게 우측 배치
    rect_spinoff = patches.FancyBboxPatch((125, 38), 50, 12, boxstyle="round,pad=0.5", linewidth=0, facecolor='#E50914')
    ax.add_patch(rect_spinoff)
    
    ax.text(150, 44, "[LAUNCH]\n임성근 셰프 오리지널 스핀오프", ha='center', va='center', color='white', fontweight='bold', fontsize=18)
    ax.text(150, 30, "→ 비활동기 트래픽의 본편 재유입 유도 (Lock-in)", ha='center', va='top', color='#ffcccc', fontsize=14, fontweight='bold')

    # --- 5. 피날레 타이틀 ---
    ax.text(90, 105, "[ 골든타임 케어 전략 & 스핀오프 로드맵 ]", ha='center', va='center', color='white', fontweight='bold', fontsize=32)
    
    # 최종 여백 조정
    plt.subplots_adjust(top=0.85, bottom=0.15, left=0.05, right=0.95)
    
    plt.savefig(os.path.join(output_path, 'content_release_timeline.png'), 
                dpi=150, 
                bbox_inches='tight', 
                pad_inches=1.0, 
                facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: content_release_timeline.png (Wide-Spread Edition)")

if __name__ == "__main__":
    create_content_release_timeline_final()
