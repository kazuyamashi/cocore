printf "password: "
read password
echo "$password" | sudo -S apt-get install && sudo -S pip install jinja2

git clone https://github.com/PyHDI/pyverilog.git
cd pyverilog
python setup.py install
cd ..

git clone https://github.com/PyHDI/veriloggen.git
cd veriloggen/
python setup.py install
cd ..

git clone https://github.com/kazuyamashi/cReComp.git
cd cReComp/
python setup.py install
cd ..