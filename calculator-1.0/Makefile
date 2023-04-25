all:
	@which pyinstaller > /dev/null || \
        (echo "PyInstaller not found. Installing..."; pip install pyinstaller)
	pyinstaller --onefile Calculator.py

clean:
	rm -rf ./dist
	rm -rf ./build
	rm -f Calculator.spec
	rm -f .Makefile.swp
	rm -rf ./math_parser/__pycache__

.PHONY: clean
