DEPENDENCIES=flet sys abc dataclasses
all:
	@which pip > /dev/null || (echo "pip not found, installing...Ho" && sudo apt-get update && sudo apt-get install -y python3-pip)
	@for dependency in $(DEPENDENCIES); do \
        if ! python -c "import $$dependency" 2>/dev/null; then \
            echo "$$dependency not found, installing..."; \
            pip install $$dependency; \
        fi; \
    done
pack: 

doc:
	doxygen Doxyfile

test:
	python3 -m unittest mathlib_suite 

run:
	python3 -m Calculator

profile:
	@python -c 'import sys' || (echo "sys module not found, installing..." && pip install sys)

clean: 
	rm -rf ./doxy_documentation

.PHONY: clean
