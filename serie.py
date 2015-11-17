from dbconnection import getconnection, getIdProveedor, getDependencia
from dbconnection import getTipoCambioDolar, getTipoCambioUfv, insertData


conn = getconnection('192.168.97.97', 'sa', 'sa', 'Activos')

conn_source = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')

c_series = conn_source.cursor()
c_series.execute()
