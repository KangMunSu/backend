db = {
    'user' : 'admin',
    'password' : 'insight1346',
    'host' : 'database-1.cd6uiz9xmlvp.ap-northeast-2.rds.amazonaws.com',
    'port' : 3306,
    'database' : 'miniter'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

JWT_SECRET_KEY = 'secrete'

test_db = {
        'user' : 'test',
        'password' : 'Insight!346',
        'host' : 'database-1.cd6uiz9xmlvp.ap-northeast-2.rds.amazonaws.com',
        'port' : 3306,
        'database' : 'test_db'
}

test_config = {
        'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
        'JWT_SECRET_KEY' : 'secrete'
}
