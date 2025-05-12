from config.db_config import get_connection

def insert_position(position_name, level):
    """
    직급 정보를 positions 테이블에 삽입
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO positions (position_id, position_name, level)
        VALUES (position_seq.NEXTVAL, :1, :2)
    """
    cursor.execute(query, (position_name, level))
    conn.commit()
    print(f"✅ 직급 '{position_name}' 등록 완료")

    cursor.close()
    conn.close()

def get_all_positions():
    """
    전체 직급 목록을 조회
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT position_id, position_name, level
        FROM positions
        ORDER BY level ASC
    """
    cursor.execute(query)
    positions = cursor.fetchall()

    cursor.close()
    conn.close()
    return positions