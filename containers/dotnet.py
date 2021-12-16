from .base import Centos_7


class Dotnet( Centos_7 ):
    scripts = (
        'ssh/provision.py',
        ( "systemd/cp.py", 'dotnet/sigrha_clients.service' ),
        ( "systemd/cp.py", 'dotnet/sigrha_opportunities.service' ),
        ( "systemd/cp.py", 'dotnet/sigrha_gateway.service' ),

        'dotnet/install.py',
        'dotnet/post_install.sh',
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/clients_service.git',
            'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/opportunities_service.git',
            'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/ADLoginService.git',
            'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/Gateway.git',
            'main' ),
        (
            'dotnet/database_migration.sh',
            '/home/chibi/projects/clients_service__main/API_Clients/',
            '/etc/systemd/system/sigrha_clients.env',
        ),
        (
            'dotnet/database_migration.sh',
            '/home/chibi/projects/opportunities_service__main/Opportunities/',
            '/etc/systemd/system/sigrha_opportunities.env',
        ),
        (
            'provision/dotnet/build_project.sh',
            '/home/chibi/projects/Gateway__main/Gateway/Gateway/',
        ),
        ( "systemd/systemd.py", 'enable', 'sigrha_clients.service' ),
        ( "systemd/systemd.py",'start', 'sigrha_clients.service' ),

        ( "systemd/systemd.py", 'enable', 'sigrha_opportunities.service' ),
        ( "systemd/systemd.py",'start', 'sigrha_opportunities.service' ),

        ( "systemd/systemd.py", 'enable', 'sigrha_gateway.service' ),
        ( "systemd/systemd.py",'start', 'sigrha_gateway.service' ),
    )
    env_vars = {
        'HOME': '/root/'
    }


class Mitsuha( Dotnet ):
    pass
