from chibi_requests import Chibi_url
import requests


hosts = [
    'kibana', 'waifus', 'sigrha.com.mx',
    'api.sigrha.client.aptude.com',
    'api.sigrha.opportunities.aptude.com',
    'api.sandbox.client.sigrha.com',
    'api.sandbox.opportunities.sigrha.com',
    'api.sandbox.sigrha.com',
    'sandbox.sigrha.com',
]


for host in hosts:
    try:
        response = Chibi_url( f'http://{host}' ).get()
        if response.ok:
            print( host, 'OK', response.status_code )
        else:
            print( host, 'no work', response.status_code )
    except requests.ConnectionError as e:
        print( host, 'no work', e )
