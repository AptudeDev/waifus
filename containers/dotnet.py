from .base import Centos_7


class Dotnet( Centos_7 ):
    client_branch = 'main'
    client_service = 'sigrha_clients.service'
    client_service_path = 'dotnet/sigrha_clients.service'
    client_service_env = 'dotnet/sigrha_clients_test.env'

    gateway_branch = 'main'
    gateway_service = 'sigrha_gateway.service'
    gateway_service_path = 'dotnet/sigrha_gateway.service'
    gateway_service_env = 'dotnet/sigrha_gateway.env'

    opportunities_branch = 'main'
    opportunities_service_path = 'dotnet/sigrha_opportunities.service'
    opportunities_service = 'sigrha_opportunities.service'
    opportunities_env = 'sigrha_opportunities.env'

    migration_mode = 'dotnet/database_migration.sh'
    build_mode = 'dotnet/build_project.sh'

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
            'cls.migration_mode',
            '/home/chibi/projects/clients_service__main/API_Clients/',
            'cls.client_service_env',
        ),
        (
            'cls.migration_mode',
            '/home/chibi/projects/opportunities_service__main/Opportunities/',
            'cls.opportunities_env',
        ),
        (
            'cls.build_mode',
            '/home/chibi/projects/Gateway__main/Gateway/Gateway/',
            'cls.gateway_service_env',
        ),
        ( "systemd/systemd.py", 'enable', 'cls.client_service' ),
        ( "systemd/systemd.py", 'restart', 'cls.client_service' ),

        ( "systemd/systemd.py", 'enable', 'cls.opportunities_service' ),
        ( "systemd/systemd.py", 'restart', 'cls.opportunities_service' ),

        ( "systemd/systemd.py", 'enable', 'cls.gateway_service' ),
        ( "systemd/systemd.py", 'restart', 'cls.gateway_service' ),
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
    client_service_env = 'dotnet/sigrha_clients_test.env'

    gateway_service = 'sigrha_gateway.service_test'
    gateway_service_path = 'dotnet/sigrha_gateway_test.service'
    gateway_service_env = 'dotnet/sigrha_gateway_test.env'

    opportunities_service_path = 'dotnet/sigrha_opportunities_test.service'
    opportunities_service = 'sigrha_opportunities_test.service'
    opportunities_env = 'sigrha_opportunities_test.env'
    migration_mode = 'dotnet/database_migration_debug.sh'
    build_mode = 'dotnet/build_project_debug.sh'
