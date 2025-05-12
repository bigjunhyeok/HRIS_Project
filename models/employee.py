from config.db_config import get_connection

def insert_employee(name, birthdate, gender, phone, email, join_date, status="재직"):
    """
    사원 정보를 employees 테이블에 삽입
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO employees (
            employee_id, name, birthdate, gender, phone, email, join_date, status
        ) VALUES (
            employee_seq.NEXTVAL, :1, :2, :3, :4, :5, :6, :7
        )
    """
    cursor.execute(query, (name, birthdate, gender, phone, email, join_date, status))
    conn.commit()
    print(f"✅ 사원 '{name}' 등록 완료")

    cursor.close()
    conn.close()

def get_all_employees():
    """
    전체 사원 목록을 조회
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT employee_id, name, birthdate, gender, phone, email, join_date, status
        FROM employees
        ORDER BY employee_id
    """
    cursor.execute(query)
    employees = cursor.fetchall()

    cursor.close()
    conn.close()
    return employees