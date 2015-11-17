from dbconnection import getconnection


cursor = conn.cursor()

archivo = open('rrhh.csv', 'r')
lista_funcionarios = []

for row in archivo:
    data = row.split(',')
    funcionario = []
    funcionario.append(data[0])
    funcionario.append(data[1])
    funcionario.append(data[6])
    funcionario.append(data[7])
    funcionario.append(data[8])
    funcionario.append(data[11])
    funcionario.append(data[14])
    # if data[11].strip() != '':
    try:
        cursor.execute("""
        INSERT INTO RecursosHumanos.dbo.Personal
        (PER_Dependencia, PER_Unidad_Organizacional, PER_CI_Empleado, PER_Apellido_Paterno, PER_Apellido_Materno,
        PER_Nombres)
        VALUES(%s, %s, '%s', '%s', '%s', '%s')

        """ % (data[0], data[1], data[11], data[6], data[7], data[8]))
        conn.commit()
        print funcionario
    except Exception, e:
        if 'PRIMARY KEY' in e[1]:
            pass
        else:
            print e
