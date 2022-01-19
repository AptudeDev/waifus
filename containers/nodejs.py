from .base import Centos_7


class Nodejs( Centos_7 ):
    branch = 'main'
    service_path = 'nodejs/sigrha_react.service'
    service_name = 'sigrha_react.service'

    scripts = (
        'nodejs/install.sh',
        'ssh/provision.py',
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/sigrha-react.git',
            'cls.branch', 'main' ),
        'nodejs/install.sh',
        (
            "nodejs/provison_repo.sh",
            '/home/chibi/projects/sigrha-react__main/' ),
        ( "systemd/cp.py", 'cls.service_path' ),
        ( "systemd/systemd.py", 'enable', 'cls.service_name' ),
        ( "systemd/systemd.py", 'restart', 'cls.service_name' ),
    )


class Asuka( Nodejs ):
    branch = 'main'


class Kurumi( Nodejs ):
    branch = 'releasecandidate'
    service_path = 'nodejs/sigrha_react_test.service'
    service_name = 'sigrha_react_test.service'
