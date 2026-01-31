"""
흑백요리사 시즌 2 댓글 수집 테스트
"""

import os
from googleapiclient.discovery import build
import pandas as pd

API_KEY = 'AIzaSyBk7IUzC0fCit6s2ofjS5lET7Dkzan5m5c'
SAVE_PATH = r"c:\Users\pc\Desktop\mypyproject\black\흑백요리사"

# 시즌 2 대표 영상 ID (예시 - 실제 영상으로 교체 필요)
# 유튜브에서 "흑백요리사 시즌2" 검색 후 인기 영상 URL의 v= 뒤 ID 복사
SEASON2_VIDEO_IDS = [
    'dQw4w9WgXcQ',  # 테스트용 - 실제 시즌2 영상 ID로 교체 필요
]

def get_youtube_service(api_key):
    """YouTube API 서비스 생성"""
    return build('youtube', 'v3', developerKey=api_key)

def test_api_connection(youtube):
    """API 연결 테스트"""
    try:
        # 간단한 영상 정보 요청으로 테스트
        request = youtube.videos().list(
            part='snippet',
            id='dQw4w9WgXcQ'  # 유명한 테스트 영상
        )
        response = request.execute()
        
        if response.get('items'):
            print("✓ API 연결 성공!")
            print(f"  테스트 영상: {response['items'][0]['snippet']['title']}")
            return True
        else:
            print("✗ API 응답 없음")
            return False
            
    except Exception as e:
        print(f"✗ API 연결 실패: {e}")
        return False

def get_video_comments(youtube, video_id, max_comments=100):
    """영상의 댓글 수집"""
    comments = []
    
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            order='relevance'
        )
        
        response = request.execute()
        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author': comment['authorDisplayName'],
                'published_at': comment['publishedAt'],
                'like_count': comment['likeCount'],
                'text': comment['textDisplay']
            })
                
    except Exception as e:
        print(f"댓글 수집 실패: {e}")
    
    return comments

def main():
    """메인 실행 함수"""
    
    print("=" * 60)
    print("YouTube API 연결 테스트")
    print("=" * 60)
    
    youtube = get_youtube_service(API_KEY)
    
    # API 연결 테스트
    if not test_api_connection(youtube):
        print("\nAPI 키에 문제가 있습니다.")
        print("YouTube Data API v3가 활성화되어 있는지 확인하세요.")
        return
    
    print("\n" + "=" * 60)
    print("댓글 수집 기능 테스트")
    print("=" * 60)
    
    # 테스트 영상으로 댓글 수집 시도
    test_video_id = 'dQw4w9WgXcQ'
    print(f"\n테스트 영상 ID: {test_video_id}")
    
    comments = get_video_comments(youtube, test_video_id, max_comments=10)
    
    if comments:
        print(f"✓ 댓글 수집 성공! ({len(comments)}개)")
        print("\n첫 3개 댓글:")
        for i, comment in enumerate(comments[:3], 1):
            print(f"  {i}. {comment['text'][:50]}...")
        
        print("\n" + "=" * 60)
        print("API가 정상 작동합니다!")
        print("이제 시즌 2 영상 URL을 알려주시면 댓글을 수집하겠습니다.")
        print("=" * 60)
    else:
        print("✗ 댓글 수집 실패")
        print("API 할당량이나 권한을 확인하세요.")

if __name__ == "__main__":
    main()
