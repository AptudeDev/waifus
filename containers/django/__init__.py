from ..base import Centos_7


class Django( Centos_7 ):
    scripts = (
        'ssh/provision.py',
        "mariadb/install_client.py",
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/sigrha_users.git',
            'cls.branch', 'master' ),
        (
            "django/provision.py",
            'cls.project_folder', '' ),

        ( "systemd/cp.py", "cls.service_path" ),
        (
            'django/migrate.sh',
            '/home/chibi/projects/sigrha_users__master/',
            '/etc/systemd/system/sigrha_users.env',
        ),
        (
            "systemd/systemd.py", 'enable',
            "cls.service_name" ),
        (
            "systemd/systemd.py", 'restart',
            "cls.service_name" ),
    )


class Shiro( Django ):
    service_name = 'sigrha_users.service'
    service_path = 'django/sigrha_users.service'
    branch = 'master'
    project_folder = '/home/chibi/projects/sigrha_users__master'


class Shionji( Django ):
    pass


class Victorique( Django ):
    pass
