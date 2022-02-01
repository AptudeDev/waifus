Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Dot_net < Base_centos
	def initialize( params={} )
		super()
		@abstract = true
		@name = 'Dot Net'
		@box = "base_centos_7"
		@ram = 1000
		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),

			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Python.new( "provision/dotnet/install.py" ),
			Script.new( "provision/dotnet/post_install.sh" ),
			Python.new( "provision/ssh/provision.py" ),

			Python.new( "provision/systemd/cp.py",
				args: [ "dotnet/#{params.fetch( :service_client )}.service" ] ),
			Python.new( "provision/systemd/cp.py",
				args: [ "dotnet/#{params.fetch( :service_oportunities )}.service" ] ),
			Python.new( "provision/systemd/cp.py",
				args: [ "dotnet/#{params.fetch( :service_gateway )}.service" ] ),

			Python.new( "provision/git_clone.py",
				args: [
					params.fetch(
						:client_repo,
						'git@github.com:AptudeSiGRHA/clients_service.git', ),
					params.fetch( :client_branch, 'main', ),
					params.fetch( :client_repo_name, 'main', ),
				] ),
			Python.new( "provision/git_clone.py",
				args: [
					params.fetch(
						:opportunities_repo,
						'git@github.com:AptudeSiGRHA/opportunities_service.git', ),
					params.fetch( :opportunities_branch, 'main', ),
					params.fetch( :opportunities_repo_name, 'main', ),
				] ),
			Python.new( "provision/git_clone.py",
				args: [
					params.fetch(
						:login_repo,
						'git@github.com:AptudeSiGRHA/ADLoginService.git', ),
					params.fetch( :login_branch, 'main', ),
					params.fetch( :login_repo_name, 'main', ),
				] ),
			Python.new( "provision/git_clone.py",
				args: [
					params.fetch(
						:gateway_repo,
						'git@github.com:AptudeSiGRHA/Gateway.git', ),
					params.fetch( :gateway_branch, 'main', ),
					params.fetch( :gateway_repo_name, 'main', ),
				] ),

			Script.new( "provision/dotnet/database_migration.sh",
				args: [
					'/home/chibi/projects/clients_service__main/API_Clients/',
					"/etc/systemd/system/#{params.fetch( :service_client )}.env",
				] ),
			Script.new( "provision/dotnet/database_migration.sh",
				args: [
					'/home/chibi/projects/opportunities_service__main/Opportunities/',
					"/etc/systemd/system/#{params.fetch( :service_oportunities )}.env",
				] ),
			Script.new( "provision/dotnet/build_project.sh",
				args: [
					'/home/chibi/projects/Gateway__main/Gateway/Gateway/',
				] ),

			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', "#{params.fetch( :service_client )}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', "#{params.fetch( :service_client )}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', "#{params.fetch( :service_oportunities )}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', "#{params.fetch( :service_oportunities )}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', "#{params.fetch( :service_gateway )}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', "#{params.fetch( :service_gateway )}.service" ] ),
		]
	end
end

class Mitsuha < Dot_net
	def initialize()
		super(
			:service_gateway => 'sigrha_gateway',
			:service_client => 'sigrha_clients',
			:service_oportunities => 'sigrha_opportunities',
		)
		@abstract = false
		@name = 'Mitsuha'
	end
end

class Kaoru < Dot_net
	def initialize()
		super(
			:client_branch => 'development',
			:opportunities_branch => 'development',
			:gateway_branch => 'development',
			:login_branch => 'main',

			:service_gateway => 'sigrha_gateway_test',
			:service_client => 'sigrha_clients_test',
			:service_oportunities => 'sigrha_opportunities_test',
		)
		@abstract = false
		@name = 'Kaoru'
	end
end
