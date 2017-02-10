#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import py_bootgen.bootgen

RESOURCE = "resource/"

def bootgen(binary, output_name="BOOT.bin"):

	print "Target binary : %s"%binary
	print "Output product : %s"%output_name

	fsbl = "FSBL.elf"
	u_boot = "u-boot.elf"

	py_bootgen.bootgen.main(fsbl, binary, u_boot, output_name)


if __name__ == '__main__':
	args = sys.argv
	argc = len(args)

	if argc < 2:
		print "USAGE: python bootgen.py xillydemo.bit"
		quit()

	elif argc < 3:
		binary = args[1]
		bootgen(binary)

	elif argc < 4:
		binary = args[1]
		output_name = args[2]
		bootgen(binary, output_name)