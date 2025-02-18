#!/usr/bin/env python3
import logging
import os

from chibi_command import Command
from chibi.config import basic_config
from chibi.file import Chibi_path
from chibi.file.snippets import ln
from chibi.net.hostname import get_hostname
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl

basic_config()
logger = logging.getLogger( 'nginx.start' )


provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] )
    + 'nginx' + 'provision' )


cowsay( "inicia de inicio de nginx" )

Command( 'setsebool', '-P', 'httpd_can_network_connect', '1', ).run()

folders = ( 'conf.d', "sites_available" )

nginx_folder = Chibi_path( '/etc/nginx/' )

for folder in folders:
    dest = nginx_folder + folder
    folders_for_copy = provision_folder + folder
    folders_for_copy.copy( dest )

( provision_folder + 'nginx.conf' ).copy( nginx_folder + 'nginx.conf' )

sites_enabled = nginx_folder + 'sites_enabled'
sites_available = nginx_folder + 'sites_available'

configs = [
    'sigrha_react.conf', 'sigrha_client.conf',
    'sigrha_opportunities.conf', 'waifus.conf', 'sigrha_users.conf',
    'sigrha_gateway.conf',
    'sandbox_sigrha_react.conf',
    'sandbox_sigrha_client.conf',
    'sandbox_sigrha_opportunities.conf',
    #'sandbox_sigrha_users.conf',
    'sandbox_sigrha_gateway.conf',
]

for config in configs:
    if not ( sites_enabled + config ).exists:
        ln( sites_available + config, sites_enabled + config )
    else:
        logger.info( f'el archivo {config} existe' )


Chibi_path( '/var/www/default/' ).mkdir( is_ok_exists=True )
index = Chibi_path( "/var/www/default/index.html" ).open()
index.write( "<h1>{} - waifus lab</h1>".format( get_hostname() ) )
Command( 'chcon', '-Rt', 'httpd_sys_content_t', '/var/www/' ).run()

Systemctl.restart( "nginx" ).run()

cowsay( "fin de inicio de nginx" )
