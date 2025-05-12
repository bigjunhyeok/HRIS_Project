import os
import subprocess
import tempfile
import configparser

def get_sqlplus_conn_str():
    """
    config/db.ini 파일에서 Oracle 접속 문자열 생성
    """
    config = configparser.ConfigParser()
    config.read(os.path.join("config", "db.ini"))

    db = config["oracle"]
    user = db["username"]
    password = db["password"]
    host = db["host"]
    port = db["port"]
    service = db["service_name"]

    return f"{user}/{password}@{host}:{port}/{service}"

def execute_sql_file_with_sqlplus(file_path, label=None):
    """
    sqlplus를 이용해 SQL 파일 실행
    """
    conn_str = get_sqlplus_conn_str()

    if not os.path.isfile(file_path):
        print(f"❌ 파일 없음: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'exit;' not in content.lower():
        content += "\nEXIT;\n"

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.sql', encoding='utf-8') as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    env = os.environ.copy()
    env["NLS_LANG"] = ".AL32UTF8"

    result = subprocess.run(
        ["sqlplus", "-s", conn_str, f"@{tmp_path}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env
    )

    tag = f"[{label}]" if label else ""
    if result.returncode == 0:
        print(f"✅ {tag} 실행 완료")
    else:
        print(f"❌ {tag} 실패\n{result.stderr.strip() or result.stdout.strip()}")

if __name__ == "__main__":
    execute_sql_file_with_sqlplus("database/drop_hris.sql", label="DROP")
    execute_sql_file_with_sqlplus("database/init_hris.sql", label="INIT")
    #execute_sql_file_with_sqlplus("database/seed_data.sql", label="SEED")