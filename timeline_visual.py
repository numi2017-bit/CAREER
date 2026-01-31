import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_content_release_timeline():
    """콘텐츠 릴리즈 및 리텐션 케어 타임라인 시각화"""
    
    fig, ax = plt.figure(figsize=(16, 7)), plt.gca()
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # --- Timeline Axis ---
    # 메인 축
    ax.plot([5, 95], [20, 20], color='white', linewidth=2)
    
    # 구간 구분선
    ax.plot([35, 35], [10, 30], color='#555555', linestyle='--', linewidth=1)
    ax.plot([65, 65], [10, 30], color='#555555', linestyle='--', linewidth=1)
    
    # 구간 라벨
    ax.text(20, 32, "During Season\n(방영 중)", ha='center', va='center', color='#cccccc', fontsize=14)
    ax.text(50, 32, "Season End\n(종영 직후)", ha='center', va='center', color='#cccccc', fontsize=14)
    ax.text(80, 32, "Off-Season\n(비활동기)", ha='center', va='center', color='#cccccc', fontsize=14)
    
    # --- Action 1: Golden Time Care (반복적인 푸시) ---
    # 수요일 밤 10시 알림 반복 배치
    # Push 1
    ax.text(15, 23, "[PUSH]", ha='center', va='bottom', color='#FFD700', fontsize=12, fontweight='bold')
    ax.plot([15, 15], [20, 23], color='#FFD700', linewidth=1)
    # Push 2
    ax.text(25, 23, "[PUSH]", ha='center', va='bottom', color='#FFD700', fontsize=12, fontweight='bold')
    ax.plot([25, 25], [20, 23], color='#FFD700', linewidth=1)
    # Push 3
    ax.text(35, 23, "[PUSH]", ha='center', va='bottom', color='#FFD700', fontsize=12, fontweight='bold')
    ax.plot([35, 35], [20, 23], color='#FFD700', linewidth=1)
    
    # 설명
    ax.text(25, 15, "[Golden Time Care]\n매주 수요일 22:00\n미공개 클립 발송", ha='center', va='top', color='#FFD700', fontsize=12, fontweight='bold')
    
    # --- Action 2: Spin-off Launch (확장) ---
    # 화살표(x=65)와 겹침을 완벽히 방지하기 위해 박스를 x=75부터 시작하도록 더 오른쪽으로 이동
    rect_spinoff = patches.FancyBboxPatch((75, 24), 34, 6, boxstyle="round,pad=0.3", linewidth=0, facecolor='#E50914')
    ax.add_patch(rect_spinoff)
    
    # 텍스트 위치 가로 좌표를 92로 조정 (박스 내부 중앙)
    ax.text(92, 27, "[LAUNCH] 임성근 셰프 스핀오프 런칭", ha='center', va='center', color='white', fontweight='bold', fontsize=16)
    
    # 설명 위치도 92로 조정
    ax.text(92, 15, "[Bridging Content]\n공백기 이탈 방지용\n유튜브 콘텐츠", ha='center', va='top', color='#ffcccc', fontsize=13, fontweight='bold')
    
    # --- Highlight Bubble ---
    # 이탈 구간 방어
    bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="none", alpha=0.9)
    ax.text(65, 40, "CHURN ZONE (이탈 위험 구간)\n강력한 콘텐츠로 방어!", ha='center', va='center', fontsize=13, fontweight='bold', color='black', bbox=bbox_props)
    ax.annotate("", xy=(65, 23), xytext=(65, 36), arrowprops=dict(arrowstyle="->", color="white", lw=2))

    # 타이틀 (한글 제목으로 변경 및 여백 확보)
    ax.text(50, 62, "[골든타임 케어 전략 & 스핀오프 로드맵]", ha='center', va='center', color='white', fontweight='bold', fontsize=28)
    
    # 캔버스 범위 및 여백 대폭 재조정 (잘림 방지 초필살기)
    ax.set_xlim(-10, 130)  # 오른쪽을 130까지 대폭 확장
    ax.set_ylim(0, 75) 
    
    # 저장
    plt.savefig(os.path.join(output_path, 'content_release_timeline.png'), 
                dpi=150, 
                bbox_inches='tight', 
                pad_inches=0.8, 
                facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: content_release_timeline.png")

if __name__ == "__main__":
    create_content_release_timeline()
