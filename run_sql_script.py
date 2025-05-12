def run_sql_file_full_statements(cursor, path):
    """
    SQL 파일 전체를 읽어서 세미콜론 단위로 문장을 실행
    (CREATE TABLE, INSERT 등 멀티라인 포함)
    """
    print(f"\n📄 실행 시작: {path}")
    with open(path, 'r', encoding='utf-8') as file:
        sql = file.read()

    # 주석 제거 & 세미콜론 단위 분리
    statements = []
    buffer = ""
    for line in sql.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('--'):
            continue
        buffer += line + "\n"
        if ';' in line:
            statements.append(buffer.strip())
            buffer = ""

    for stmt in statements:
        try:
            print(f"▶ 실행 중: {stmt.splitlines()[0][:60]}...")
            cursor.execute(stmt)
        except Exception as e:
            print(f"⚠️ 실행 실패: {stmt.splitlines()[0][:100]}...\n에러: {e}")