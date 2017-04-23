<img src="logo/cocore_logo_str.png" width="60%">

**CO**mponent oriented development & **CO**operation of software application and **RE**configurable device  

**Git**:         https://github.com/kazuyamashi/cocore.git  
**Maintainer**:  Kazushi Yamashina
**Copyright**:   2016, Kazushi Yamashina  
**License**:     GPL-2.0  
**Contact**: 	 kazuyamashi_at_gmail.com  or [Twitter](https://twitter.com/KazushihsuzaK) or [Facebook](https://www.facebook.com/kazushi.yamashina?fref=nf)

# What is COCORE
**COCORE is a Linux distribution for programmable SoC (FPGA+ARM). So, COCORE is an environment for following a system or an application.**

- Hardware and software co-system, co-application.
- Robotic system using FPGA
- Distributed system using FPGA

In COCORE, a file system is based on **Ubuntu 14.04 armhf**, and COCORE includes **Xillybus** and **ROS (Robot Operating System)**.

- [Xillybus](http://xillybus.com/)
- [ROS](http://www.ros.org/)

COCORE supports some FPGA boards.

- [Zybo](https://reference.digilentinc.com/reference/programmable-logic/zybo/start)
- [Zedboard](http://store.digilentinc.com/zedboard-zynq-7000-arm-fpga-soc-development-board/)

# What constitutes COCORE

### Zybo

- Hardware design
	- [Xillinux : xillinux-eval-zybo-1.3c](http://xillybus.com/downloads/xillinux-eval-zybo-1.3c.zip)
- Linux kernel
	- [https://github.com/DigilentInc/Linux-Digilent-Dev.git](https://github.com/DigilentInc/Linux-Digilent-Dev.git) (branch : master-next)
- u-boot
	- [https://github.com/DigilentInc/u-boot-Digilent-Dev.git](https://github.com/DigilentInc/Linux-Digilent-Dev.git) (branch : master-next)
- File system : [http://www.armhf.com](http://www.armhf.com/download/)
	- [ubuntu-trusty-14.04-armhf](http://s3.armhf.com/dist/basefs/ubuntu-trusty-14.04-armhf.com-20140603.tar.xz)

### Zedboard

- Hardware design
	- [Xillinux : xillinux-eval-zedboard-1.3c](http://xillybus.com/downloads/xillinux-eval-zedboard-1.3c.zip)
- Linux kernel
	- [https://github.com/DigilentInc/Linux-Digilent-Dev.git](https://github.com/DigilentInc/Linux-Digilent-Dev.git) (branch : master-next)
- u-boot
	- [https://github.com/Xilinx/u-boot-xlnx.git](https://github.com/Xilinx/u-boot-xlnx.git) (branch : xilinx-v14.4)
- File system : [http://www.armhf.com](http://www.armhf.com/download/)
	- [ubuntu-trusty-14.04-armhf](http://s3.armhf.com/dist/basefs/ubuntu-trusty-14.04-armhf.com-20140603.tar.xz)



# How to build this distribution for Zybo

[Xillybus and ROS on Ubuntu on Zybo : Japanese](zybo/build_instruction/xillybus_and_ros_on_ubuntu_on_zybo.md)  
[Xillybus and ROS on Ubuntu on Zybo : English](zybo/build_instruction/xillybus_and_ros_on_ubuntu_on_zybo_en.md)

# How to build this distribution for Zedboard

[Xillybus and ROS on Ubuntu on Zedboard : Japanese](zedboard/build_instruction/xillybus_and_ros_on_ubuntu_on_zedboard.md)  
[Xillybus and ROS on Ubuntu on Zedboard : English](zedboard/build_instruction/xillybus_and_ros_on_ubuntu_on_zedboard_en.md)


# Download SD image

It is preparing and it will be released soon.

# ROS-compliant FPGA component

It is preparing.