"""
흑백요리사 시즌 2 댓글 수집 (영상 ID 직접 입력 방식)
"""

import os
from googleapiclient.discovery import build
import pandas as pd

API_KEY = 'AIzaSyBk7IUzC0fCit6s2ofjS5lET7Dkzan5m5c'
SAVE_PATH = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

# 시즌 2 관련 영상 ID 목록 (유튜브에서 직접 찾아서 입력)
# URL에서 v= 뒤의 ID만 복사해서 넣으세요
# 예: https://www.youtube.com/watch?v=ABC123 -> 'ABC123'

SEASON2_VIDEO_IDS = [
    # 여기에 시즌 2 영상 ID를 입력하세요
    # 예시:
    # 'dQw4w9WgXcQ',
    # 'abc123def45',
]

def get_youtube_service(api_key):
    """YouTube API 서비스 생성"""
    return build('youtube', 'v3', developerKey=api_key)

def get_video_info(youtube, video_id):
    """영상 정보 가져오기"""
    try:
        request = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            item = response['items'][0]
            return {
                'video_id': video_id,
                'title': item['snippet']['title'],
                'channel': item['snippet']['channelTitle'],
                'view_count': item['statistics'].get('viewCount', 0)
            }
    except Exception as e:
        print(f"Error getting video info for {video_id}: {e}")
    
    return None

def get_video_comments(youtube, video_id, max_comments=1000):
    """영상의 댓글 수집"""
    comments = []
    
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            order='relevance'
        )
        
        while request and len(comments) < max_comments:
            response = request.execute()
            
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'author': comment['authorDisplayName'],
                    'published_at': comment['publishedAt'],
                    'like_count': comment['likeCount'],
                    'text': comment['textDisplay']
                })
            
            # 다음 페이지
            if 'nextPageToken' in response and len(comments) < max_comments:
                request = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    maxResults=100,
                    pageToken=response['nextPageToken'],
                    order='relevance'
                )
            else:
                break
                
    except Exception as e:
        print(f"Error fetching comments for {video_id}: {e}")
    
    return comments

def main():
    """메인 실행 함수"""
    
    if not SEASON2_VIDEO_IDS:
        print("=" * 60)
        print("영상 ID를 입력해주세요!")
        print("=" * 60)
        print("\n방법:")
        print("1. 유튜브에서 '흑백요리사 시즌2' 검색")
        print("2. 인기 영상 5-10개 선택")
        print("3. 각 영상 URL에서 v= 뒤의 ID 복사")
        print("   예: https://www.youtube.com/watch?v=ABC123 -> 'ABC123'")
        print("4. 이 스크립트의 SEASON2_VIDEO_IDS 리스트에 추가")
        print("\n또는 영상 URL을 알려주시면 제가 추가해드립니다!")
        return
    
    youtube = get_youtube_service(API_KEY)
    
    print("=" * 60)
    print("흑백요리사 시즌 2 댓글 수집 시작")
    print("=" * 60)
    
    # 각 영상의 댓글 수집
    for i, video_id in enumerate(SEASON2_VIDEO_IDS, 1):
        print(f"\n[{i}/{len(SEASON2_VIDEO_IDS)}] 영상 ID: {video_id}")
        
        # 영상 정보 가져오기
        video_info = get_video_info(youtube, video_id)
        if video_info:
            print(f"  제목: {video_info['title'][:50]}...")
            print(f"  조회수: {video_info['view_count']:,}")
        
        # 댓글 수집
        comments = get_video_comments(youtube, video_id, max_comments=1000)
        
        if comments:
            # CSV로 저장
            df = pd.DataFrame(comments)
            filename = f"{video_id}_comments_s2.csv"
            filepath = os.path.join(SAVE_PATH, filename)
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            print(f"  저장 완료: {len(comments)}개 댓글 -> {filename}")
        else:
            print(f"  댓글 없음")
    
    print("\n" + "=" * 60)
    print("수집 완료!")
    print(f"저장 위치: {SAVE_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()
