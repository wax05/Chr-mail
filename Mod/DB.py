import json
import pymysql

def SqlInit(FilePath="./Config/SqlSettings.json"):
    """Parsing Json Configuration File -> Return SqlObject 

   `Args`:
        `FilePath`=(str, optional): Defaults to "./Config/SqlSettings.json".
    `Returns`:
        {Conn:PymysqlConn,CommonCurs:PymysqlCommonCurs,DictCurs:PymysqlDictCurs}
    """
    with open(FilePath,"r") as f:
        SqlSettings = json.load(f)
        host=SqlSettings['host']
        user=SqlSettings['user']
        pw=SqlSettings['password']
        db_name=SqlSettings['db_name']
        charset=SqlSettings['charset']
        Conn = pymysql.connect(host = host, user = user, password = pw ,db = db_name,charset = charset)#DbConfig
        CommonCurs = Conn.cursor()
        DictCurs = Conn.cursor(pymysql.cursors.DictCursor)
        return {"Conn":Conn,"CommonCurs":CommonCurs,"DictCurs":DictCurs}

def Db_Export_Data(TableName:str)->tuple:
    """`TableName`에 있는 정보 다 빼옴"""
    try:
        sql = f"select * from {TableName}"
        curs.execute(sql)
        rows = curs.fetchall()
        return rows
    except:
        return 'error'

def Db_Export_Data_YouWant(TableName:str,Column:str,Value:str)->tuple:
    """`TableName`테이블내 `Column`에서 `Value`와 맞는것을 모두 가져옴"""
    try:
        sql = f"select * from {TableName} where {Column}='{Value}'"
        curs.execute(sql)
        rows = curs.fetchall()
        return rows
    except:
        return 'error'