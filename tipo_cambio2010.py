from dbconnection import getconnection
import xlrd

conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()

w_tipos_cambio = xlrd.open_workbook('excels/tc2011_2015.xls')
tipos_cambios = w_tipos_cambio.sheet_by_index(2)

sql = """
    DELETE FROM t_tipocambio WHERE d_fecha = '%s';
    INSERT INTO t_tipocambio(c_moneda, d_fecha, n_tipocambio, c_usuariocreacion, d_fechacreacion)
    VALUES ('UFV', '%s', %s, 'daquispes', '%s');
    INSERT INTO t_tipocambio(c_moneda, d_fecha, n_tipocambio, c_usuariocreacion, d_fechacreacion)
    VALUES ('SUS', '%s', %s, 'daquispes', '%s');
"""

for i in range(1, tipos_cambios.nrows):
    fecha = xlrd.xldate.xldate_as_datetime(tipos_cambios.cell(i, 0).value, w_tipos_cambio.datemode)
    fecha = fecha.strftime('%Y-%m-%d') + 'T00:00:00'
    ufv = tipos_cambios.cell(i, 1).value
    dolar = tipos_cambios.cell(i, 2).value
    try:
        cursor.execute(sql % (fecha, fecha, str(ufv), fecha, fecha, str(dolar), fecha))
        conn.commit()
    except Exception, ex:
        conn.rollback()
        print ex
