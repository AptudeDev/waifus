from ..base import Centos_7


class Django( Centos_7 ):
    scripts = (
        "mariadb/install_client.py",
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/sigrha_users.git',
            'cls.branch', 'master' ),
        (
            "provision/django/provision.py",
            'cls.project_folder', '' ),

        ( "systemd/cp.py", "django/#{service_name}.service" ),
        (
            "systemd/systemd.py", 'enable',
            "django/#{service_name}.service" ),
        (
            "systemd/systemd.py", 'start',
            "django/#{service_name}.service" ),
    )


class Shiro( Django ):
    service_name = 'sigrha_users',
    branch = 'master',
    project_folder = '/home/chibi/projects/sigrha_users__master',


class Shionji( Django ):
    pass


class Victorique( Django ):
    pass
