#!/usr/bin/env python3
import os
from chibi_lxc.config import configuration
from chibi.config import basic_config, load as load_config
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi_command import Command
from chibi_command.centos import Iptables
from chibi_command.sysctl import Sysctl
from chibi_command.lxc import lxc
from chibi.file.snippets import ln
from chibi.file.snippets import cd


basic_config( 'DEBUG' )
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()

provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'lxc/provision' )
provision_ssh = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'ssh/provision/' )


if __name__ == "__main__":
    if provision_ssh.exists:
        ssh_provision = Chibi_path(
            '/home/chibi/projects/waifus__master/provision/ssh/provision' )
        provision_ssh.copy( ssh_provision, verbose=True )
        for ssh_key in ssh_provision.ls():
            ssh_key.chmod( 0o0777 )
            ssh_key.chown( user_name='chibi', group_name='chibi', )

    Chibi_path( '/etc/security/limits.conf' ).open().write(
        """
*    soft    nofile 65536
*    hard    nofile 65536
        """ )

    Chibi_path( '/etc/sysctl.d/99-sysctl.conf' ).open().write(
        """
vm.max_map_count=262144
fs.file-max = 2097152
"""
    )
    first_machine = lxc.Destroy( '-n', 'test_machine' ).run()
    first_machine = lxc.Create( '-n', 'test_machine' )
    first_machine.template( 'download' )
    first_machine.parameters(
        '-d', 'centos', '-r', '7', '--arch', 'amd64', '--keyserver',
        'hkp://keyserver.ubuntu.com' )
    first_machine.run()

    cd( '/home/chibi/projects/waifus__master' )
    Command(
        'chibi_lxc', 'up',
        'Chii',
        #'Chii', 'Chino',
        'Asuka', 'Mitsuha', 'Kurumi', 'Kaoru'
        'Ikaros',
        'Misuzu', 'Pochi', 'Tohru' ).run()
    #Command(
    #    'chibi_lxc', 'provision',
    #    'Ikaros', 'Chii', 'Asuka', 'Mitsuha' ).run()

    hosts = Chibi_path( 'hosts' )
    print( hosts.open().read() )
    hosts.copy( '/etc/hosts', verbose=True )
    load_config( './config.py' )
    configuration.chibi_lxc.containers
    ikaros = configuration.chibi_lxc.containers.Ikaros

    iptable = Iptables.table( 'nat' ).append( "PREROUTING" ).protocol( 'tcp' )
    iptable.in_interface( 'eth1' ).destination_port( 80 ).jump( 'DNAT' )
    iptable.to_destination( ikaros.info.ip, 80 )
    iptable.run()
    Iptables.delete( "FORWARD", '4' ).run()
    Iptables.delete( "FORWARD", '4' ).run()
    """
    ikaros = Command(
        'chibi_lxc', 'up', 'Ikaros', 'Misuzu', 'Pitou', 'Rei', 'Chii' )
    """
    #Chibi_path( 'hosts' ).copy( '/etc/hosts' )
