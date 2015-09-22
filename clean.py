from .dbconnection import getconnection

conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

cursor = conn.cursor(as_dict=True)

cursor.execute("""
SELECT ACT_Nombre_Activo, ACT_Codigo_Activo
FROM Activos
 """)

data = cursor.fetchall()

def formatutf8(cadena):
    if cadena is None:
        return None
    return unicode(str(cadena.encode('utf8')), 'utf-8')

import unicodedata


def elimina_tildes(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


cursor_dos = conn.cursor()

for r in data:
    new_name = r["ACT_Nombre_Activo"]
    # print r

    new_name = elimina_tildes(new_name)
    new_name = new_name.replace('\r', '')
    new_name = new_name.encode('ascii', 'ignore')
    print str(new_name)
    cursor_dos.execute("""
            UPDATE Activos SET ACT_Nombre_Activo = '%s' WHERE ACT_Codigo_Activo=%d
            """ % (new_name, r['ACT_Codigo_Activo']))
    conn.commit()
