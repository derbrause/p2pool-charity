linux:
install:
	python setup.py install --record files.txt
uninstall:
	cat files.txt | xargs rm -rf

windows:
edit indlude_dirs and library_dirs in setup-win.py to point to the corresponding folders on your system. after that build with:
	python setup-win.py install
