# monitoring/utils.py

from ldap3 import Server, Connection, ALL
from django.conf import settings

def authenticate_ldap(username, password):
    try:
        server = Server(settings.LDAP_SERVER, get_info=ALL)
        conn = Connection(server, user='cn={},{}'.format(username, settings.LDAP_BASE_DN), password=password, auto_bind=True)
        return True
    except Exception as e:
        print(e)
        return False
