DEPENDENCIES=flet sys abc dataclasses
TARGET_FOLDER=xragan00_xtabac12_236811_xfiedl05
all:
	@which pip > /dev/null || (echo "pip not found, installing...Ho" && sudo apt-get update && sudo apt-get install -y python3-pip)
	@for dependency in $(DEPENDENCIES); do \
        if ! python -c "import $$dependency" 2>/dev/null; then \
            echo "$$dependency not found, installing..."; \
            pip install $$dependency; \
        fi; \
    done

doc_dependencies:
	@if ! which dot > /dev/null; then \
        echo "Graphviz is not installed"; \
        echo "Installing Graphviz..."; \
        sudo apt-get install graphviz; \
    	elif ! which doxygen > /dev/null; then \
        echo "Doxygen is not installed"; \
        echo "Installing Doxygen..."; \
        sudo apt-get install doxygen; \
	fi

pack: doc_dependencies
	mkdir $(TARGET_FOLDER)
	@python -c 'import doxypy' || (echo "doxypy module not found, installing..." && pip install doxypy)
	doxygen Doxyfile
	mv doc $(TARGET_FOLDER)/
	cd ../ && mkdir install && cp -r calculator-1.0 install/ && cp -r profiler-1.0 install/ && mv install src/$(TARGET_FOLDER)/
	cd $(TARGET_FOLDER)/ && mkdir repo
	rsync -av --exclude='$(TARGET_FOLDER)' ./ $(TARGET_FOLDER)/repo/src/
	cd ../ && rsync -av --exclude='src' ./ src/$(TARGET_FOLDER)/repo/
	tar cvzf $(TARGET_FOLDER).tar.gz $(TARGET_FOLDER)
	rm -rf $(TARGET_FOLDER)

doc:	doc_dependencies
	@python -c 'import doxypy' || (echo "doxypy module not found, installing..." && pip install doxypy)
	doxygen Doxyfile
test:
	python3 -m unittest mathlib_suite 

run:
	python3 -m Calculator

profile:
	@python -c 'import sys' || (echo "sys module not found, installing..." && pip install sys)

clean: 
	rm -rf $(TARGET_FOLDER).tar.gz
	rm -f __pychache__
	rm -rf doc

.PHONY: clean
