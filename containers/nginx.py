from .base import Centos_7


sites_enable = [
    'default',
    'kibana',
    'sandbox_sigrha_client',
    'sandbox_sigrha_gateway',
    'sandbox_sigrha_opportunities',
    'sandbox_sigrha_react',
    'sigrha_client',
    'sigrha_gateway',
    'sigrha_opportunities',
    'sigrha_react',
    'sigrha_users',
    'waifus',
]

scripts_sites = ( "nginx/enable.py", 'enable', *sites_enable )


class Nginx( Centos_7 ):
    scripts = (
        "nginx/install.py",
        "nginx/provision.py",
        scripts_sites,

        ( "systemd/systemd.py", 'enable', 'nginx.service' ),
        ( "systemd/systemd.py", 'restart', 'nginx.service' ),

        "elasticsearch/beat/filebeat_install.py",
        "elasticsearch/beat/filebeat_nginx.py",
        ( "systemd/systemd.py", 'enable', 'filebeat.service' ),
        ( "systemd/systemd.py", 'start', 'filebeat.service' )
    )


class Ikaros( Nginx ):
    extra_hosts = (
        'waifus', 'sigrha.com',
        'api.client.sigrha.com',
        'api.opportunities.sigrha.com',
        'api.sandbox.client.sigrha.com',
        'api.sandbox.opportunities.sigrha.com',
        'api.sandbox.sigrha.com',
        'sandbox.sigrha.com',
        'kibana.sigrha.com',
    )


class Astraea( Nginx ):
    pass


class Caos( Nginx ):
    pass


class Nymph( Nginx ):
    pass
