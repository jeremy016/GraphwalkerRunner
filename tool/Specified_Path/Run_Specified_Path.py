# -*- coding: utf-8 -*-
import sys
import script as Script


def main():
	argv_1 = sys.argv[1]
	rundown = argv_1.split('->')

	for point in rundown:
		eval( "Script."+point + "()" )


if __name__ == "__main__":
    main()

 