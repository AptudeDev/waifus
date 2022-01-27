import sys
from chibi.config import configuration
from chibi.file import Chibi_path
from chibi.module import import_

sys.path.append( Chibi_path( '.' ).inflate )

from containers.base import Centos_7
from containers.elasticsearch import Misuzu, Pitou, Rei, Rem, Sakura
from containers.nginx import Ikaros, Astraea, Caos, Nymph
from containers.mariadb import Chii, Freya, Sumomo
from containers.rabbitmq import Chino, Cocoa, Rize
from containers.nodejs import Asuka, Kurumi
from containers.dotnet import Mitsuha, Kaoru
from containers.others.owncloud import Owncloud
from containers.logstash import Tohru, Kanna, Elma
from containers.kibana import Pochi, Tama
from containers.django import Shiro, Shionji, Victorique


configuration.chibi_lxc.containers.add( Centos_7 )
configuration.chibi_lxc.containers.add( Misuzu )
configuration.chibi_lxc.containers.add( Pitou )
configuration.chibi_lxc.containers.add( Rei )
configuration.chibi_lxc.containers.add( Rem )
configuration.chibi_lxc.containers.add( Sakura )

configuration.chibi_lxc.containers.add( Ikaros )
configuration.chibi_lxc.containers.add( Astraea )
configuration.chibi_lxc.containers.add( Caos )
configuration.chibi_lxc.containers.add( Nymph )

configuration.chibi_lxc.containers.add( Chii )
configuration.chibi_lxc.containers.add( Freya )
configuration.chibi_lxc.containers.add( Sumomo )

configuration.chibi_lxc.containers.add( Chino )
configuration.chibi_lxc.containers.add( Cocoa )
configuration.chibi_lxc.containers.add( Rize )

configuration.chibi_lxc.containers.add( Asuka )
configuration.chibi_lxc.containers.add( Mitsuha )
configuration.chibi_lxc.containers.add( Kurumi )
configuration.chibi_lxc.containers.add( Kaoru )

configuration.chibi_lxc.containers.add( Tohru )
configuration.chibi_lxc.containers.add( Kanna )
configuration.chibi_lxc.containers.add( Elma )

configuration.chibi_lxc.containers.add( Pochi )
configuration.chibi_lxc.containers.add( Tama )

configuration.chibi_lxc.containers.add( Shiro )
configuration.chibi_lxc.containers.add( Shionji )
configuration.chibi_lxc.containers.add( Victorique )

configuration.chibi_lxc.hosts = Chibi_path( 'hosts' )
