import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 및 스타일 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터
labels = ['밈 전파력', '팬덤 충성도', '리텐션 기여', '브랜드 확장성']
choi_values = [98, 95, 92, 88]
generic_values = [45, 60, 55, 70]

num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
choi_values += choi_values[:1]
generic_values += generic_values[:1]
angles += angles[:1]

# 그래프 생성
fig = plt.figure(figsize=(10, 10), facecolor='#F8F9FA') # 깨끗한 미색 배경
ax = fig.add_subplot(111, polar=True)
ax.set_facecolor('#F8F9FA')

# 1. 원형 그리드 설정 (기본형 탈피)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], labels, color='#212529', size=16, fontweight='bold')

# 눈금 숨기기 및 원형 가이드라인
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="#ADB5BD", size=10)
plt.ylim(0, 120)

# 2. 데이터 시각화 (프리미엄 채색)
# 일반 셰프 (그림자처럼 배경으로)
ax.plot(angles, generic_values, color='#DEE2E6', linewidth=2, linestyle='solid')
ax.fill(angles, generic_values, color='#DEE2E6', alpha=0.3, label='Mass Public IP (대중적 인지도군)')

# 최강록 (Netflix Red & Bold)
ax.plot(angles, choi_values, color='#E50914', linewidth=5, marker='o', markersize=10, 
        markerfacecolor='white', markeredgewidth=3, label='SUPER CHARACTER IP (최강록)')
ax.fill(angles, choi_values, color='#E50914', alpha=0.15)

# 3. 브랜딩 및 캡션
plt.title('셰프 IP 전략적 가치 비교 분석 Matrix', size=26, color='#212529', weight='bold', pad=60)
plt.figtext(0.5, 0.02, "※ 분석 데이터: 유튜브 댓글 참여율 및 바이럴 강도 결합 지표 (Source: All-Chef Comparison)", 
            ha="center", fontsize=11, color="#6C757D", style='italic')

# 범례 위치 조정 (겹침 원천 차단: 우측 하단으로 이동)
plt.legend(loc='lower right', bbox_to_anchor=(1.25, 0), frameon=True, facecolor='white', edgecolor='#DEE2E6', fontsize=12)

plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # 하단 캡션 공간 확보
# 흑백요리사 폴더에 저장
plt.savefig(r'c:\Users\pc\Desktop\mypyproject\black\흑백요리사\character_ip_value_premium.png', dpi=200, bbox_inches='tight')

print("범례 겹침이 해결된 프리미엄 리포트 이미지가 재생성되었습니다.")
