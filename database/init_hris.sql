-- ===============================
-- HRIS 시스템 초기 테이블 생성
-- ===============================

-- 사원 테이블
CREATE TABLE employees (
    employee_id   NUMBER PRIMARY KEY,
    name          VARCHAR2(100),
    birthdate     DATE,
    gender        CHAR(1),
    phone         VARCHAR2(20),
    email         VARCHAR2(100),
    join_date     DATE,
    status        VARCHAR2(20) -- 재직, 휴직, 퇴사
);

-- 부서 테이블
CREATE TABLE departments (
    dept_id     NUMBER PRIMARY KEY,
    dept_name   VARCHAR2(100),
    location    VARCHAR2(100)
);

-- 직급 테이블
CREATE TABLE positions (
    position_id    NUMBER PRIMARY KEY,
    position_name  VARCHAR2(100),
    rank_level     NUMBER
);

-- 사원 직무 이력 테이블
CREATE TABLE employee_jobs (
    job_id        NUMBER PRIMARY KEY,
    employee_id   NUMBER REFERENCES employees(employee_id),
    dept_id       NUMBER REFERENCES departments(dept_id),
    position_id   NUMBER REFERENCES positions(position_id),
    start_date    DATE,
    end_date      DATE
);

-- ===============================
-- 시퀀스 생성
-- ===============================
CREATE SEQUENCE employee_seq START WITH 1001 INCREMENT BY 1;
CREATE SEQUENCE dept_seq     START WITH 101  INCREMENT BY 1;
CREATE SEQUENCE position_seq START WITH 201  INCREMENT BY 1;
CREATE SEQUENCE job_seq      START WITH 10001 INCREMENT BY 1;

EXIT;