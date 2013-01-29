INSTALL_DIR := install
MOD_NAME    := pysgt

BUILD_DIR   := build

all: smoother pysgt test install

build: smoother pysgt

smoother:
	cd src/sgt_smoother; make

pysgt:
	mkdir -p build
	cp src/sgt_smoother/sgt_smoother.py src/sgt_smoother/_sgt_smoother.so build
	cp src/core.py build
	touch build/__init__.py

test:
	python build/core.py > testrun.out

install:
	mkdir -p $(INSTALL_DIR)/$(MOD_NAME)
	cp $(BUILD_DIR)/* $(INSTALL_DIR)/$(MOD_NAME)


clean:
	rm -rf $(BUILD_DIR)
	rm -f testrun.out
	rm -rf install
	cd src/sgt_smoother; make clean

.PHONY: all smoother pysgt test install clean
