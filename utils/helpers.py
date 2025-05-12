from datetime import datetime

def parse_date(date_str):
    """
    문자열을 날짜(datetime)로 변환
    Args:
        date_str (str): 'YYYY-MM-DD' 형식의 문자열
    Returns:
        datetime: 파싱된 날짜
    """
    return datetime.strptime(date_str, "%Y-%m-%d")

def format_phone(phone):
    """
    숫자만 있는 전화번호를 하이픈 형식으로 변환
    예: 01012345678 → 010-1234-5678
    """
    if len(phone) == 11:
        return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
    return phone