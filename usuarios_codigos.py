# -*- coding: utf-8 -*-
from dbconnection import getconnection
import xlrd
import xlsxwriter


wb_usuarios = xlrd.open_workbook('excels/lista_usuarios.xls')
usuarios = wb_usuarios.sheet_by_index(0)

conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Seguridad')
cursor = conn.cursor()

sql = """ SELECT USU_Id_Usuario,USU_CI_Empleado FROM Usuarios """
sql_act_usuarios = """

ALTER TABLE Seguridad.dbo.Permisos
NOCHECK CONSTRAINT FK_Permisos_Usuarios;
UPDATE Seguridad.dbo.Usuarios SET USU_Id_Usuario='%s' WHERE USU_Id_Usuario='%s';
UPDATE Seguridad.dbo.Permisos SET PRM_Id_Usuario='%s' WHERE PRM_Id_Usuario='%s';
UPDATE Activos.dbo.Autorizaciones SET AUT_Id_Usuario='%s' WHERE AUT_Id_Usuario='%s';
UPDATE Activos.dbo.Tipos_Autorizacion SET TAU_Id_Usuario='%s' WHERE TAU_Id_Usuario='%s';
UPDATE Activos.dbo.Tipos_Autorizacion SET TAU_Id_Usuario='%s' WHERE TAU_Id_Usuario='%s';
UPDATE RecursosHumanos.dbo.PIN SET PIN_Id_Usuario='%s' WHERE PIN_Id_Usuario='%s';
ALTER TABLE Seguridad.dbo.Permisos
CHECK CONSTRAINT FK_Permisos_Usuarios;
"""
cursor.execute(sql)
usuarios_activos = cursor.fetchall()


codigo_usuarios = {}
for i in range(usuarios.nrows):
    codigo = unicode(usuarios.cell(i, 9).value.split("@")[0])
    ci = usuarios.cell(i, 16).value
    try:
        codigo_usuarios[str(int(ci))] = codigo
    except Exception as e:
        pass

numero_usuarios = 0
for usuario in usuarios_activos:
    codigo = usuario[0]
    ci = usuario[1].encode('utf8')
    if codigo_usuarios.has_key(ci):
        numero_usuarios += 1
        try:
            cursor.execute(sql_act_usuarios % (
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'),
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'),
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'),
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'),
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'),
                codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8')
                ))

            conn.commit()
        except Exception as e:
            conn.rollback()
            print e

        print 'CI: %s CODIGO: %s ANTIGUO: %s' % \
            (ci, codigo_usuarios[ci].encode('utf8'), codigo.encode('utf8'))

print 'El numero de Usuarios es : %d' % numero_usuarios

