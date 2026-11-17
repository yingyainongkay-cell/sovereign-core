.PHONY: install test verify

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest tests/ -v

verify: test
	@echo "========================================="
	@echo " All Sovereign Core Verifications Passed!"
	@echo "========================================="
