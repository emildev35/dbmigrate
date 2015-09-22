from .dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
curr = conn.cursor(as_dict=True)
curr.execute("SELECT COUNT(*) AS col,cod_act FROM TAF_ACTIVO GROUP BY cod_act")
data = curr.fetchall()

print len(data)
