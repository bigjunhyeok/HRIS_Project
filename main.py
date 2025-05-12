from models.employee import insert_employee, get_all_employees
from datetime import datetime

if __name__ == "__main__":
    # ✅ 샘플 사원 등록
    insert_employee(
        name="김철수",
        birthdate=datetime(1988, 3, 25),
        gender='M',
        phone="010-2345-6789",
        email="kim@example.com",
        join_date=datetime(2022, 7, 1)
    )

    # ✅ 전체 사원 목록 출력
    employees = get_all_employees()
    print("\n📋 전체 사원 목록")
    for emp in employees:
        print(f"- ID: {emp[0]}, 이름: {emp[1]}, 입사일: {emp[6]}, 상태: {emp[7]}")