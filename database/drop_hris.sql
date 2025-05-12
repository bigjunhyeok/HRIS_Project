-- ===============================
-- HRIS 시스템 객체 삭제 스크립트
-- ===============================

-- 테이블 삭제
DROP TABLE employee_jobs CASCADE CONSTRAINTS;
DROP TABLE positions CASCADE CONSTRAINTS;
DROP TABLE departments CASCADE CONSTRAINTS;
DROP TABLE employees CASCADE CONSTRAINTS;

-- 시퀀스 삭제
DROP SEQUENCE job_seq;
DROP SEQUENCE position_seq;
DROP SEQUENCE dept_seq;
DROP SEQUENCE employee_seq;

PROMPT 모든 DROP 명령 실행 완료

EXIT;