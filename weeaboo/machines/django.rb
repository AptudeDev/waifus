Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Django < Base_centos
	def initialize( params={} )
		super()
		@abstract = true
		@name = 'Django'
		@box = "base_centos_7"
		@ram = 512
		service_name = params.fetch( :service_name, 'django' )
		repo = params.fetch(
			:repo, 'git@github.com:AptudeSiGRHA/sigrha_users.git' )
		branch = params.fetch( :branch, 'master' )
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/ssh/provision.py" ),
			Python.new( "provision/mariadb/install_client.py" ),

			Python.new( "provision/git_clone.py",
				args: [ repo, branch, 'master' ] ),

			Python.new( "provision/django/provision.py",
				args: [ params.fetch( :project_folder, '' ) ] ),
			Script.new( "provision/django/migrate.sh".
				args: [ 
					'/home/chibi/projects/sigrha_users__master/',
					'/etc/systemd/system/sigrha_users.env',
				] ),

			Python.new( "provision/systemd/cp.py",
				args: [ "django/#{service_name}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', "#{service_name}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'restart', "#{service_name}.service" ] ),
		]
	end
end

class Shiro < Django
	def initialize()
		super(
			:service_name => 'sigrha_users',
			:branch => 'master',
			:project_folder => '/home/chibi/projects/sigrha_users__master',
		)
		@name = 'Shiro'
		@abstract = false
	end
end

class Shionji < Django
	def initialize()
		super()
		@name = 'Shionji'
		@abstract = false
	end
end

class Victorique < Django
	def initialize()
		super()
		@name = 'Victorique'
		@abstract = false
	end
end
