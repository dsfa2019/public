SHELL=/bin/bash

# The basename of this assignment, e.g., lab01, hw01.
NAME=lab01

# The other files in this directory that the notebook references.
SUPPORTFILES={*.png,*.jpg,$(NAME)_tests}

# The command to run that releases notebooks (i.e., vocReleaseNotebook)
# (This shouldn't need to be changed.)
VOCRELEASE=php $(VLIB)/php/nb_release.php

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  zip       to create a zip of the assignment for upload to Vocareum."
	@echo "  voc       to release the assignment within the Vocareum platform."

zip:
	zip -r $(NAME).zip Makefile $(NAME).ipynb $(SUPPORTFILES) -x "*/__pycache__/*"
	
voc:
	cp -r $(SUPPORTFILES) ../resource/startercode
	$(VOCRELEASE) $(NAME).ipynb
