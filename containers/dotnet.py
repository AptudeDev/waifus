from .base import Centos_7


class Dotnet( Centos_7 ):
    client_branch = 'main'
    client_service = 'sigrha_clients.service'
    client_service_path = 'dotnet/sigrha_clients.service'

    gateway_branch = 'main'
    gateway_service = 'sigrha_gateway.service'
    gateway_service_path = 'dotnet/sigrha_gateway.service'

    opportunities_branch = 'main'
    opportunities_service_path = 'dotnet/sigrha_opportunities.service'
    opportunities_service = 'sigrha_opportunities.service'

    scripts = (
        'ssh/provision.py',
        ( "systemd/cp.py", 'cls.client_service_path' ),
        ( "systemd/cp.py", 'cls.opportunities_service_path' ),
        ( "systemd/cp.py", 'cls.gateway_service_path' ),

        'dotnet/install.py',
        'dotnet/post_install.sh',
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/clients_service.git',
            'cls.client_branch', 'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/opportunities_service.git',
            'cls.opportunities_branch', 'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/Gateway.git',
            'cls.gateway_branch', 'main' ),
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
        ( "systemd/systemd.py", 'enable', 'cls.client_service' ),
        ( "systemd/systemd.py", 'start', 'cls.client_service' ),

        ( "systemd/systemd.py", 'enable', 'cls.opportunities_service' ),
        ( "systemd/systemd.py", 'start', 'cls.opportunities_service' ),

        ( "systemd/systemd.py", 'enable', 'cls.gateway_service' ),
        ( "systemd/systemd.py", 'start', 'cls.gateway_service' ),
    )
    env_vars = {
        'HOME': '/root/'
    }


class Mitsuha( Dotnet ):
    pass


class Kaoru( Dotnet ):
    client_branch = 'development'
    opportunities_branch = 'development'
    gateway_branch = 'development'

    client_service = 'sigrha_clients_test.service'
    client_service_path = 'dotnet/sigrha_clients_test.service'

    gateway_service = 'sigrha_gateway.service_test'
    gateway_service_path = 'dotnet/sigrha_gateway_test.service'

    opportunities_service_path = 'dotnet/sigrha_opportunities_test.service'
    opportunities_service = 'sigrha_opportunities_test.service'
