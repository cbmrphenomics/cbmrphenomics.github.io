.PHONY: autobuild

# Runs sphinx-autobuild in a temporary directory, allowing real-time
# monitoring of changes to the documentation. Options -aE is needed since
# changes to certain files (css, js) may not not picked up otherwise.
# https://github.com/executablebooks/sphinx-autobuild#relevant-sphinx-bugs
autobuild:
	sphinx-autobuild -qnaE esrum/source $(shell mktemp --directory)
