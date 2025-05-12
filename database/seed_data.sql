-- 부서 더미 데이터
INSERT INTO departments (dept_id, dept_name, location)
VALUES (101, '인사팀', '서울 본사');

INSERT INTO departments (dept_id, dept_name, location)
VALUES (102, '개발팀', '판교 RandD 센터');

-- 직급 더미 데이터
INSERT INTO positions (position_id, position_name, rank_level)
VALUES (201, '사원', 1);

INSERT INTO positions (position_id, position_name, rank_level)
VALUES (202, '대리', 2);

INSERT INTO positions (position_id, position_name, rank_level)
VALUES (203, '과장', 3);

COMMIT;