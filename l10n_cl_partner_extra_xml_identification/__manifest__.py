{
    "name": """Chile - Partner XML Identification""",
    'version': '17.0.',
    'category': 'Localization/Chile',
    'license': 'LGPL-3',
    'sequence': 12,
    'author':  'Blanco Martín & Asociados',
    'description': """
Agrega Campos Especiales a los XML
==================================
//Emisor/CdgVendedor
//Receptor/CdgIntRecep
    """,
    'website': 'http://blancomartin.cl',
    'depends': [
        'l10n_cl_edi',
    ],
    'data': [
        'views/partner_view.xml',
        'template/dte_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
