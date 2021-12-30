#!/usr/bin/env python3
import sys
from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi_command.nix import Systemctl
from chibi.file import Chibi_path
from chibi_command import Command
import os



basic_config()
provision_folder = (
    Chibi_path( os.environ[ 'PROVISION_PATH' ] ) + 'django/provision' )

project_folder = Chibi_path( sys.argv[1] )
cowsay( f"provisionado django {project_folder}" )

pip = Command(
    'pip3', 'install', '-r', project_folder + 'requirements_dev.txt' )

pip.run()

cowsay( f"termino de provisionado django {project_folder}" )
