db = {'user'     : 'test',
      'password' : 'Insight!346',
      'host'     : 'localhost',
      'port'     : 3306,
      'database' : 'miniter'}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

JWT_SECRET_KEY = 'secrete'
JWT_EXP_DELTA_SECONDS = 7 * 24 * 60 * 60

S3_BUCKET     = "tantanhan1"
S3_ACCESS_KEY = "AKIA5LALLGPQHTDUVM6D"
S3_SECRET_KEY = "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"
S3_BUCKET_URL = f"https://{S3_BUCKET}.s3.ap-northeast-2.amazonaws.com/"

test_db = {'user'     : 'test',
           'password' : 'Insight!346',
           'host'     : 'localhost',
           'port'     : 3306,
           'database' : 'test_db'}

test_config = {
        'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
        'JWT_SECRET_KEY' : 'secrete',
        'JWT_EXP_DELTA_SECONDS' : 7 * 24 * 60 * 60,
        'S3_BUCKET'      : 'test',
        'S3_ACCESS_KEY'  : 'test_access_key',
        'S3_SECRET_KEY'  : 'test_secret_key',
        'S3_BUCKET_URL'  : f'https://s3.ap-northeast-2.amazonaws.com/test/'
}

UPLOAD_DIRECTORY = './profile_pictures'


