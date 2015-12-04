import pymssql
from settings import DB_DESTINT
import datetime


def getconnection(host, user, password, db_name, instaneName=None):
    if instaneName is None:
        conn = pymssql.connect(host, user, password, db_name)
        return conn
    else:
        conn = pymssql.connect(host + '\\' + instaneName, user, password, db_name)
        return conn


def getTipoCambioDolar(conn, fecha):
    cur = conn.cursor()
    cur.execute(""" select n_tipocambio
                    from t_tipocambio where d_fecha=\'%s\'
                    and c_moneda = 'SUS'""" % fecha)
    return cur.fetchone()


def getTipoCambioUfv(conn, fecha):
    cur = conn.cursor()
    cur.execute(""" select n_tipocambio
                    from t_tipocambio where d_fecha=\'%s\'
                    and c_moneda = 'UFV'""" % fecha)
    return cur.fetchone()


def getDependencia(dependencia):
    dependencia = dependencia.replace(' ', '').strip()
    if dependencia == 'STSCZ':
        return 3
    if dependencia == 'STG':
        return 1
    if dependencia == 'STCBA':
        return 4
    if dependencia == 'STLP':
        return 2
    if dependencia == 'STCH':
        return 5


def getIdProveedor(conn, cod_proveedor):
    cur = conn.cursor()
    cur.execute(
        'SELECT nit_prov FROM TAF_PROVEEDOR WHERE cod_prov=%s' % cod_proveedor)
    return cur.fetchone()


def formatutf8(data):
    if data is None:
        return None
    return unicode(str(data.encode('utf8')), 'utf-8')


def insertData(conn, sql_fragment, data):
    sql_fragment += 'VALUES ('
    for col in DB_DESTINT['COLUMNS']:
        item_data = data[DB_DESTINT['COLUMNS'][col]]
        if col == 'ACT_Codigo_Activo':
            item_data = item_data[len(item_data) - 4:len(item_data)]

        if type(item_data) is datetime.datetime:
            item_data = item_data.strftime('%Y-%m-%d') + 'T00:00:00'
        if type(item_data) is int:
            item_data = str(item_data)
        if type(item_data) is str:
            if item_data.isdigit():
                item_data = str(item_data)
            else:
                item_data = '\'' + item_data.replace('\n', '') + '\''
        if type(item_data) is long:
            item_data = str(item_data)
        if type(item_data) is float:
            item_data = str(item_data)
        if type(item_data) is unicode:
            item_data = item_data.encode('ascii', 'ignore')
            item_data =  \
                '\'' + item_data.replace('\\n', '').replace('\'', '"') + '\''
        if col == 'ACT_Vida_Util':
            sql_fragment += item_data
        else:
            sql_fragment += item_data + ','

    sql_fragment += ')'
    sql_fragment = sql_fragment.replace('\n', '').replace('\r', '')
    try:
        cursor = conn.cursor()
        cursor.execute(sql_fragment)
        conn.commit()
        print "OK"
    except Exception:
        conn.rollback()
        print "FALLO"
