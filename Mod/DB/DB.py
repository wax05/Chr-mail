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

