import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('dark_background')

# 캐릭터 IP 가치 분석 데이터 (IP Asset Matrix)
labels = ['밈 전파력', '팬덤 충성도', '리텐션 기여', '브랜드 확장성']
choi_values = [98, 95, 92, 88] # 최강록
generic_values = [45, 60, 55, 70] # 일반 셰프

num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
choi_values += choi_values[:1]
generic_values += generic_values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), facecolor='white')
ax.set_facecolor('white')

# 최강록 데이터 (넷플릭스 레드 핵심 강조)
ax.fill(angles, choi_values, color='#E50914', alpha=0.2)
ax.plot(angles, choi_values, color='#E50914', linewidth=4, label='최강록 (캐릭터 IP형)')

# 일반 셰프 데이터 (차분한 그레이)
ax.fill(angles, generic_values, color='#888888', alpha=0.1)
ax.plot(angles, generic_values, color='#888888', linewidth=2, linestyle='--', label='Mass 아이콘 (고조회수형)')

# 레이블 설정 및 겹침 방지 (Padding 증가)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_ylim(0, 110)

# 외곽 라벨 배치 (거리 조절)
ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=15, fontweight='bold', color='#333')

# 개별 라벨 위치 미세 조정을 통한 겹침 차단
for label, angle in zip(ax.get_xticklabels(), angles):
    if angle == 0: label.set_position((0, 0.15)) # 밈 전파력 (위로)
    elif angle == np.pi: label.set_position((0, -0.15)) # 리텐션 기여 (아래로)

# 격자선 컬러 조정
ax.grid(color='#dddddd', linestyle='--')

plt.title('캐릭터 IP 자산 가치 비교 분석 (Matrix)', fontsize=22, pad=60, fontweight='bold', color='#004d00')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)

plt.tight_layout()
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\character_ip_value.png', dpi=150, bbox_inches='tight')

print("글씨 겹침이 해결된 화이트 테마 레이더 차트가 생성되었습니다.")
