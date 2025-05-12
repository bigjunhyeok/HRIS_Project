from config.db_config import get_connection

def insert_department(dept_name, location):
    """
    부서 정보를 departments 테이블에 삽입
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO departments (dept_id, dept_name, location)
        VALUES (dept_seq.NEXTVAL, :1, :2)
    """
    cursor.execute(query, (dept_name, location))
    conn.commit()
    print(f"✅ 부서 '{dept_name}' 등록 완료")

    cursor.close()
    conn.close()

def get_all_departments():
    """
    전체 부서 목록을 조회
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT dept_id, dept_name, location
        FROM departments
        ORDER BY dept_id
    """
    cursor.execute(query)
    departments = cursor.fetchall()

    cursor.close()
    conn.close()
    return departments