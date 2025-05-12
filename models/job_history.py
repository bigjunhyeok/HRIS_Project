from config.db_config import get_connection

def assign_job(employee_id, dept_id, position_id, start_date):
    """
    사원에게 부서/직급을 배정 (직무 이력 추가)
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO employee_jobs (
            job_id, employee_id, dept_id, position_id, start_date, end_date
        ) VALUES (
            job_seq.NEXTVAL, :1, :2, :3, :4, NULL
        )
    """
    cursor.execute(query, (employee_id, dept_id, position_id, start_date))
    conn.commit()
    print(f"✅ 사원 ID {employee_id}의 직무 배정 완료")

    cursor.close()
    conn.close()

def end_job(job_id, end_date):
    """
    기존 직무 이력을 종료 처리 (퇴직, 부서 이동 등)
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE employee_jobs
        SET end_date = :1
        WHERE job_id = :2
    """
    cursor.execute(query, (end_date, job_id))
    conn.commit()
    print(f"✅ 직무 ID {job_id} 종료일 업데이트 완료")

    cursor.close()
    conn.close()

def get_employee_jobs(employee_id):
    """
    특정 사원의 전체 직무 이력을 조회
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT job_id, dept_id, position_id, start_date, end_date
        FROM employee_jobs
        WHERE employee_id = :1
        ORDER BY start_date DESC
    """
    cursor.execute(query, (employee_id,))
    jobs = cursor.fetchall()

    cursor.close()
    conn.close()
    return jobs