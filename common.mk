SHELL=/bin/bash

ifeq ($(shell echo ${GOLLY_DATA_HOME}),)
$(error Environment variable GOLLY_DATA_HOME not defined. Please run "source environment" in the golly-data repo root directory before running make commands)
endif

