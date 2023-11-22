# -- coding: utf-8 --
#************#
# Create
#************#

import xmlrpc.client
import csv

host = '127.0.0.1'
port = 9001
db = 'odoo_17'
user = 'villalon2511@gmail.com'
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
            vals['list_price'] = _list_price
            print(vals)

            # Validate the register does not exist
            _id = object_proxy.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', _name]]])
            if _id:
                _product = object_proxy.execute(db, uid, password, 'product.template' ,'write',_id , vals)
                if _product:
                    print("Se ha modificado el registro: ")
                else:
                    print("No se ha modificado el registro: ")
            else:
                print('= El registro no existe =')

        cont += 1
        print("Se han modificado: ", cont)


def main():
    print("Ha comenzado el proceso")
    _create(True)
    print('Ha finalizado la carga tabla')
main()