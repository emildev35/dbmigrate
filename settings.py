DB_ORIGIN = {
    'HOST': '192.168.97.99',
    'USER': 'sa',
    'PASSWORD': 'ala_stg_2005',
    'DB_NAME': 'Activos',
    'TABLE': 'TAF_ACTIVO',
    'COLUMNS': [
        'cod_act',
        'cod_grupo',
        'cod_aux',
        'descripcion',
        'vida_util',
        'fecha_inc',
        'fecha_compra',
        'valor',
        'cod_fuente',
        'cod_organismo',
        'cod_prov',
        'regional'
    ]
}


DB_DESTINT = {
    'HOST': '192.168.97.99',
    'USER': 'sa',
    'PASSWORD': 'sa',
    'DB_NAME': 'Activos',
    'TABLE': 'Activos',
    'COLUMNS': {
        'ACT_Codigo_Activo': 'cod_act',
        'ACT_Grupo_Contable': 'cod_grupo',
        'ACT_Auxiliar_Contable': 'cod_aux',
        'ACT_Nombre_Activo': 'descripcion',
        'ACT_Vida_Util': 'vida_util',
        'ACT_Fecha_Incorporacion': 'fecha_inc',
        'ACT_Fecha_Compra': 'fecha_compra',
        'ACT_Valor_Compra': 'valor',
        'ACT_Fuente_Financiamiento': 'cod_fuente',
        'ACT_Organismo_Financiador': 'cod_organismo',
        'ACT_NIT_Proveedor': 'cod_prov',
        'ACT_Dependencia': 'regional',
        'ACT_Tipo_Cambio_Dolar': 'tipo_cambio_dolar',
        'ACT_Tipo_Cambio_UFV': 'tipo_cambio_ufv'
    }
}
