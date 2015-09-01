stock-quant: main.py
	python main.py

test:
	python tests/main.py

clean:
	@echo "start remove complied files"
	rm ./*.pyc
	rm ./test/*.pyc
	rm ./data/*.pyc
	rm ./analytics/*.pyc
	@echo "end remove complied files"

install:
	# TODO python setup.py
