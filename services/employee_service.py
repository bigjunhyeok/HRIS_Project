from models.employee import insert_employee
from models.job_history import assign_job

def onboard_employee(employee_data, dept_id, position_id):
    """
    새로운 사원 등록 후 지정된 부서와 직급으로 직무 배정

    Args:
        employee_data (dict): 사원 기본 정보
        dept_id (int): 부서 ID
        position_id (int): 직급 ID
    """
    insert_employee(
        name=employee_data["name"],
        birthdate=employee_data["birthdate"],
        gender=employee_data["gender"],
        phone=employee_data["phone"],
        email=employee_data["email"],
        join_date=employee_data["join_date"],
        status="재직"
    )

    # employee_id는 시퀀스를 사용했기 때문에 가장 큰 ID를 조회하는 방식 사용
    from config.db_config import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(employee_id) FROM employees")
    employee_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    assign_job(employee_id, dept_id, position_id, start_date=employee_data["join_date"])
    print(f"🎉 사원 {employee_data['name']} 등록 및 직무 배정 완료")