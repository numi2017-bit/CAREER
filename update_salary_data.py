
import csv

# Existing data from previous scrape (approx 10)
existing_data = [
    ["대림산업","7,600","건설·시공·토목·조경","마케팅·광고·MD","전체 평균"],
    ["현대오토에버(주)","7,500","솔루션·SI·CRM·ERP","마케팅·광고·MD","전체 평균"],
    ["삼성전자(주)","6,713","전기·전자·제어","마케팅·광고·MD","전체 평균"],
    ["코웨이(주)","6,087","생활용품·소비재·기타","마케팅·광고·MD","전체 평균"],
    ["대한제분(주)","6,014","식품가공","마케팅·광고·MD","전체 평균"],
    ["에스케이하이닉스","6,000","전기·전자·제어","마케팅·광고·MD","전체 평균"],
    ["농심","5,512","식품가공","마케팅·광고·MD","전체 평균"],
    ["대상","4,990","식품가공","마케팅·광고·MD","전체 평균"],
    ["삼양식품","4,515","식품가공","마케팅·광고·MD","전체 평균"],
    ["유한킴벌리(주)","4,398","목재·제지·가구","마케팅·광고·MD","전체 평균"]
]

# New data from search results (Manual curation to expand the list)
# Values are estimated based on 'New Hire' or 'Average' mentions in search
new_data = [
    ["LG에너지솔루션", "5,200", "2차전지/화학", "마케팅 (신입)", "대기업 신입 기준"],
    ["네이버", "5,000", "IT/포털", "마케팅 (신입)", "대기업 신입 기준"],
    ["카카오", "4,900", "IT/플랫폼", "마케팅 (신입)", "대기업 신입 기준"],
    ["제일기획", "5,000", "광고/대행사", "광고기획/AE", "업계 상위 (추정)"],
    ["이노션", "4,800", "광고/대행사", "광고기획/AE", "업계 상위 (추정)"],
    ["HS Ad", "4,600", "광고/대행사", "광고기획/AE", "업계 상위 (추정)"],
    ["그로스 마케터 (평균)", "6,672", "직무별 통계", "그로스 마케팅", "직무별 상위"],
    ["브랜드 마케터 (평균)", "5,416", "직무별 통계", "브랜드 마케팅", "직무별 평균"],
    ["CRM 마케터 (평균)", "5,123", "직무별 통계", "CRM 마케팅", "직무별 평균"],
    ["콘텐츠 마케터 (평균)", "4,226", "직무별 통계", "콘텐츠 마케팅", "직무별 평균"]
]

# Combine
combined_header = ["회사명/직무", "연봉 정보 (만원)", "산업군/구분", "직무 상세", "비고"]
combined_rows = []

# Map existing to new structure
for row in existing_data:
    combined_rows.append(row)

for row in new_data:
    combined_rows.append(row)

# Save to CSV
file_path = r"c:\Users\pc\Desktop\mypyproject\CAREER\salary_data.csv"
with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(combined_header)
    writer.writerows(combined_rows)

print(f"Updated {file_path} with {len(combined_rows)} entries.")
