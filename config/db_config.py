import cx_Oracle
import configparser
import os

def get_connection():
    """
    .ini 파일로부터 Oracle DB 접속 정보를 읽고 DB 연결 객체를 반환
    """
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'db.ini')
    config.read(config_path)

    db = config['oracle']
    dsn = cx_Oracle.makedsn(db['host'], db.getint('port'), service_name=db['service_name'])

    conn = cx_Oracle.connect(
        user=db['username'],
        password=db['password'],
        dsn=dsn
    )
    return conn