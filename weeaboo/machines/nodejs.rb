Dir[ File.dirname(__FILE__) + "/base.rb" ].each { |file| require file }

class Nodejs < Base_centos
	def initialize(
			repo='git@github.com:AptudeSiGRHA/sigrha-react.git',
			branch='main', repo_name='main', service_name='sigrha_react' )
		super()
		@abstract = true
		@name = 'Nodejs'
		@box = "base_centos_7"
		@ram = 3072
		@repo = repo
		@branch = branch
		@repo_name = repo_name
		@service_name = service_name

		@scripts = [
			Script.new( "provision/update_python_lib.sh" ),
			Python.new( "provision/add_user.py",
				args: [ 'chibi' ] ),
			Python.new( "provision/copy_host.py" ),
			Python.new( "provision/repos/cp_all_repos.py" ),
			Script.new( "provision/nodejs/install.sh" ),
			Python.new( "provision/ssh/provision.py" ),
			Python.new( "provision/git_clone.py",
				args: [ @repo, @branch, @repo_name ] ),
			Script.new( "provision/nodejs/provison_repo.sh",
				args: [ '/home/chibi/projects/sigrha-react__main' ] ),

			Python.new( "provision/systemd/cp.py",
				args: [ "nodejs/#{@service_name}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'enable', "#{@service_name}.service" ] ),
			Python.new( "provision/systemd/systemd.py",
				args: [ 'start', "#{@service_name}.service" ] ),
		]
	end
end

class Asuka < Nodejs
	attr_accessor :repo, :branch, :repo_name
	def initialize()
		super(
			repo='git@github.com:AptudeSiGRHA/sigrha-react.git',
			branch='main', repo_name='main', service_name="sigrha_react" )
		@abstract = false
		@name = 'Asuka'
	end
end

class Kurumi < Nodejs
	attr_accessor :repo, :branch, :repo_name
	def initialize()
		super(
			repo='git@github.com:AptudeSiGRHA/sigrha-react.git',
			branch='releasecandidate', repo_name='main',
			service_name="sigrha_react_test" )
		@abstract = false
		@name = 'Kurumi'
	end
end
