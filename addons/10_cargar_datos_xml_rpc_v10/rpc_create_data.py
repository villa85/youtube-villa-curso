# -- coding: utf-8 --
#************#
# Create
#************#

import xmlrpc.client
import csv

host = '127.0.0.1'
port = 9003
db = 'odoo_10'
user = 'admin'
password = 'admin'

url = 'http://%s:%d/xmlrpc/2/' % (host, port)

common_proxy = xmlrpc.client.ServerProxy(url + 'common')
object_proxy = xmlrpc.client.ServerProxy(url + 'object')
uid = common_proxy.login(db, user, password)
if uid:
    print('Conectado al servidor maestro')

def _create(state):
    print("=1=")
    print(state)
    if state is True:
        archive = csv.DictReader(open('data.csv'))
        cont = 0
        for field in archive:
            cont += 1
            _name = field['name'].strip()
            _detailed_type = field['detailed_type'].strip()
            _list_price = field['list_price'].strip()

            vals = {}
            vals['name'] = _name
            vals['detailed_type'] = _detailed_type
            vals['list_price'] = _list_price
            vals['active'] = True
            print(vals)

            # Validate the register does not exist
            _id = object_proxy.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', _name]]])
            if _id:
                print('= El registro ya existe =')
            else:
                new_product = object_proxy.execute(db, uid, password, 'product.template', 'create', vals)
                if new_product:
                    print("Se ha creado el registro: ")
                else:
                    print("No se ha creado el registro: ")

        cont += 1
        print("Se han creado: ", cont)


def main():
    print("Ha comenzado el proceso")
    _create(True)
    print('Ha finalizado la carga tabla')
main()