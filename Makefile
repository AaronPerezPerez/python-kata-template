test:
	pytest
test-watch:
	ptw --beforerun clear
install:
	python3 -m venv kataEnv && source kataEnv/bin/activate && pip3 install -r requirements.txt && source kataEnv/bin/activates

