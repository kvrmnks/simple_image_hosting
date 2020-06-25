import pymysql

'''
create table list(
    id varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    time timestamp DEFAULT CURRENT_TIMESTAMP,
    primary key (id)
)charset=utf8;

create table pics(
    id varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    data longblob NOT NULL,
    primary key (id)
)charset=utf8;
'''


class LDataBase:
    def __init__(self, host, port, user, password, db, charset='utf8'):
        self.mysql = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.cursor = self.mysql.cursor()

    def clearTables(self):
        self.dropTables()
        self.createTables()

    def dropTables(self):
        self.cursor.execute('drop table pics;')
        self.cursor.execute('drop table list;')

    def createTables(self):
        self.cursor.execute('create table list(\
            id varchar(255) NOT NULL,\
            name varchar(255) NOT NULL,\
            time timestamp DEFAULT CURRENT_TIMESTAMP,\
            primary key (id)\
        )charset=utf8;')
        self.cursor.execute('create table pics(\
            id varchar(255) NOT NULL,\
            name varchar(255) NOT NULL,\
            data longblob NOT NULL,\
            primary key (id)\
        )charset=utf8;')

    def getList(self):
        self.cursor.execute('select * from list')
        return self.cursor.fetchall()

    def getAllPics(self):
        self.cursor.execute('select * from pics')
        return self.cursor.fetchall()

    def insertPics(self, id, name, data):
        sql_list = 'insert into list (id, name) values (%s, %s)'
        sql_pics = 'insert into pics (id, name, data) values (%s, %s, %s)'
        self.cursor.execute(sql_list, (id, name))
        self.cursor.execute(sql_pics, (id, name, data))

    def getPicsById(self, id):
        sql = 'select * from pics where id = ' + id
        self.cursor.execute(sql)
        return self.cursor.fetchall()

