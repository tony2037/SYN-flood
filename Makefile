PY = python3

all: SYN
SYN: SYN_flood.py
	$(PY) $<
