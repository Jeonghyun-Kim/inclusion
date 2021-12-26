MEMO ?= "No memo."

install:
	pip3 install -r ./requirements.txt

start:
	python3 ./main.py --save --memo ${MEMO}

iterate-10:
	python3 ./main.py --save --iterate 10 --memo ${MEMO}

iterate-100:
	python3 ./main.py --save --iterate 100 --memo ${MEMO}

dev:
	python3 ./main.py -v 100000 --save
