all: sgt_smoother_module

sgt_smoother_module: sgt_smoother.i sgt_smoother.cpp
	python setup.py build
	cp $$(find -name _sgt_smoother.so) .

clean:
	rm -f  sgt_smoother_wrap.cpp sgt_smoother.py* _sgt_smoother.so
	rm -rf build

.PHONY: clean
