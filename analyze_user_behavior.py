import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

base_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사\csv_파일"
output_path = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

def analyze_user_data():
    """작성자(Author) 중심의 유저 행동 데이터 분석"""
    
    # 다양한 파일 패턴 지원
    all_files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    
    all_dfs = []
    print(f"데이터 로딩 중... (대상 폴더: {base_path})")
    
    for file in all_files:
        # 시즌 구분 로직
        if "S2" in file or "_s2" in file or "시즌2" in file:
            suffix = "Season 2"
        elif "S1" in file or "시즌1" in file:
            suffix = "Season 1"
        else:
            suffix = "Unknown"  # 기본값
            
        try:
            # 인코딩 문제 해결 시도
            file_path = os.path.join(base_path, file)
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except:
                try:
                    df = pd.read_csv(file_path, encoding='cp949')
                except:
                    df = pd.read_csv(file_path, encoding='utf-8-sig') # One more try
            
            # 필수 컬럼 확인 (author, text)
            if 'author' in df.columns:
                df['season'] = suffix
                df['source_file'] = file
                
                # video_id가 없으면 파일명에서 추출 시도
                if 'video_id' not in df.columns:
                    df['video_id'] = file.split(".")[0]
                    
                # like_count 없으면 0으로 채움
                if 'like_count' not in df.columns:
                    df['like_count'] = 0
                
                all_dfs.append(df)
        except Exception as e:
            print(f"  Skipping {file}: {e}")
            continue
    
    if not all_dfs:
        print("❌ 로드된 데이터가 없습니다!")
        return None
            
    full_df = pd.concat(all_dfs, ignore_index=True)
    print(f"✅ 총 {len(full_df):,}개 댓글 데이터 로드 완료")
    
    # 1. 유저별 활동량 계산 (댓글 수)
    user_activity = full_df.groupby('author').agg({
        'text': 'count',
        'like_count': 'sum',
        'season': 'nunique',
        'video_id': 'nunique'
    }).rename(columns={
        'text': 'comment_count',
        'like_count': 'total_likes_received',
        'season': 'seasons_active',
        'video_id': 'videos_watched'
    })

    # 2. 유저 세그먼트 정의 (대시보드 RFM 개념 차용)
    def segment_user(row):
        if row['videos_watched'] >= 3 and row['seasons_active'] == 2:
            return '충성 팬덤 (Core)'
        elif row['videos_watched'] >= 2:
            return '적극 참여자 (Active)'
        elif row['total_likes_received'] >= 50:
            return '여론 주도자 (Influencer)'
        else:
            return '일반 시청자 (Casual)'

    user_activity['segment'] = user_activity.apply(segment_user, axis=1)
    
    # 3. 결과 시각화
    # 3-1. 세그먼트 분포 (인원수 + 퍼센트 표시)
    segment_counts = user_activity['segment'].value_counts()
    
    # 라벨에 인원수 추가
    labels = [f'{idx}\n({val:,}명)' for idx, val in zip(segment_counts.index, segment_counts.values)]
    
    plt.figure(figsize=(12, 8))
    colors = ['#FFD700', '#4ECDC4', '#FF6B6B', '#C7C7C7']
    
    # autopct를 사용하여 퍼센트 표시
    patches, texts, autotexts = plt.pie(
        segment_counts, 
        labels=labels,
        autopct='%1.1f%%', 
        colors=colors, 
        explode=[0.05, 0.05, 0.05, 0], # Core Fans 0.1 강조는 도넛 차트에서 어색할 수 있으므로 통일하거나 조정. 원래대로 0.05
        startangle=140,
        pctdistance=0.85, # 도넛 형태에 맞게 조정
        textprops={'fontsize': 11}
    )
    
    # 퍼센트 텍스트 스타일 조정
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_weight('bold')
        
    # 도넛 차트로 만들기
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    plt.title(f'유튜브 커뮤니티 유저 세그먼트 분석 (총 {len(user_activity):,}명)', fontsize=16, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'user_segments_pie_ko.png'), dpi=150)
    plt.close()

    # 3-2. 상위 헤비 유저 (Hardcore)
    top_users = user_activity.sort_values('comment_count', ascending=False).head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_users, x='comment_count', y=top_users.index, palette='coolwarm')
    plt.title('댓글 참여 최상위 유저 TOP 10', fontsize=14, weight='bold')
    plt.xlabel('댓글 수')
    plt.savefig(os.path.join(output_path, 'top_active_users_ko.png'), dpi=150)
    plt.close()

    print(f"총 분석 유저 수: {len(user_activity):,}명")
    print("\n세그먼트별 결과:")
    print(segment_counts)
    
    return user_activity

if __name__ == "__main__":
    analyze_user_data()
