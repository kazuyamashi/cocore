# -*- coding: utf-8 -*-

import os
import sys

XILLYBUS_READ_32 = "/dev/xillybus_read_32"

def main():
	dev = os.open(XILLYBUS_READ_32, os.O_RDONLY)
	while True:
		string_data = os.read(dev, 1)
		sys.stdout.write(string_data)
		sys.stdout.flush()

if __name__ == '__main__':
	main()
