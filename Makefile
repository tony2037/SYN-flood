PY = python3

all: SYN
SYN: SYN_flood.py
	$(PY) $< --target 104.24.97.185
