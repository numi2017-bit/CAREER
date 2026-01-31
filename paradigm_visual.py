import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def create_paradigm_shift_visual():
    """패러다임 시프트 (View -> Engagement) 시각화"""
    
    fig, ax = plt.figure(figsize=(16, 9)), plt.gca()
    ax.set_facecolor('#1a1a1a')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # --- Left: OLD WAY (단순 시청) ---
    # 배경 박스 (회색톤)
    rect_old = patches.FancyBboxPatch((5, 10), 40, 35, boxstyle="round,pad=1", linewidth=2, edgecolor='#555555', facecolor='#2d2d2d', alpha=0.8)
    ax.add_patch(rect_old)
    
    # 타이틀
    ax.text(25, 40, "OLD WAY", ha='center', va='center', color='#888888', fontweight='bold', fontsize=20)
    ax.text(25, 35, "View (시청)", ha='center', va='center', color='white', fontweight='bold', fontsize=28)
    
    # 키워드
    keywords_old = ["One-way (일방향)", "Traffic (트래픽)", "Contents (콘텐츠)", "Subscribers (단순 구독자)"]
    for i, kw in enumerate(keywords_old):
        ax.text(25, 28 - i*4, kw, ha='center', va='center', color='#aaaaaa', fontsize=14)
        
    # --- Right: NEW WAY (관계 비즈니스) ---
    # 배경 박스 (넷플릭스 레드톤)
    rect_new = patches.FancyBboxPatch((55, 10), 40, 35, boxstyle="round,pad=1", linewidth=0, facecolor='#E50914', alpha=0.9)
    ax.add_patch(rect_new)
    
    # 타이틀
    ax.text(75, 40, "NEW PARADIGM", ha='center', va='center', color='#ffcccc', fontweight='bold', fontsize=20)
    ax.text(75, 35, "Engagement (관계)", ha='center', va='center', color='white', fontweight='bold', fontsize=28)
    
    # 키워드
    keywords_new = ["Interactive (양방향)", "Fandom (팬덤/락인)", "Character (캐릭터 IP)", "Advocates (지지자)"]
    for i, kw in enumerate(keywords_new):
        ax.text(75, 28 - i*4, kw, ha='center', va='center', color='white', fontweight='bold', fontsize=14)

    # --- Arrow (Shift) ---
    # 중앙 화살표
    arrow = patches.FancyArrowPatch((47, 27.5), (53, 27.5), mutation_scale=40, color='white', linewidth=5)
    ax.add_patch(arrow)
    ax.text(50, 32, "SHIFT", ha='center', va='center', color='white', fontweight='bold', fontsize=12)

    # --- Footer Message ---
    ax.text(50, 5, "'흑백요리사'는 요리 경연이 아니라,\n캐릭터와 팬덤이 만든 [관계의 비즈니스]였다.", 
            ha='center', va='center', color='white', fontsize=16, fontweight='bold', 
            bbox=dict(facecolor='#1a1a1a', edgecolor='#ffffff', boxstyle='round,pad=0.5', alpha=0.8))

    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'paradigm_shift_visual.png'), dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
    plt.close()
    print("✓ Saved: paradigm_shift_visual.png")

if __name__ == "__main__":
    create_paradigm_shift_visual()
