{
    'name': 'Recalc Taxes with Fiscal Position',
    'version': '17.0',
    'category': 'Invoicing',
    'description': """
Fixes the need of taxes recalculation when fiscal position is changed.
Also, moves the fiscal position selector to main view of the invoice
    """,
    'author': 'Blanco Martín & Asociados',
    'website': 'http://blancomartin.cl',
    'license': 'LGPL-3',
    'depends': [
        'account',
        ],
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
