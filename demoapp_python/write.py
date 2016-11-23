# -*- coding: utf-8 -*-

import os
import sys
XILLYBUS_WRITE_32 = "/dev/xillybus_write_32"

def main():
	dev = os.open(XILLYBUS_WRITE_32, os.O_WRONLY)

	while True:
		string_data = sys.stdin.read(1)
		os.write(dev, string_data)

if __name__ == '__main__':
	main()
