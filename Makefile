MEMO ?= "No memo."

install:
	pip3 install -r ./requirements.txt

start:
	python3 ./main.py --save -m ${MEMO}

iterate-10:
	python3 ./main.py --save -i 10 -m ${MEMO}

dev:
	python3 ./main.py --verbose 10000
