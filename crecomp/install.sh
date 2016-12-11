case $1 in
	install)
		echo "password" | sudo -S apt-get install iverilog
		sudo apt-get install python-jinja2
		sudo apt-get install python-pip

		git clone https://github.com/PyHDI/pyverilog.git
		cd pyverilog
		sudo python setup.py install
		cd ..

		git clone https://github.com/PyHDI/veriloggen.git
		cd veriloggen/
		sudo python setup.py install
		cd ..

		git clone https://github.com/kazuyamashi/cReComp.git
		cd cReComp/
		sudo python setup.py install
		cd ..
		;;
	uninstall)
		echo "password" | sudo -S apt-get remove iverilog
		sudo apt-get install python-jinja2
		sudo pip uninstall pyverilog
		sudo pip uninstall veriloggen
		sudo pip uninstall cReComp/
		;;
	*)
		echo "option list"
		echo "=========="
		echo "install"
		echo "uninstall"
		;;
esac

