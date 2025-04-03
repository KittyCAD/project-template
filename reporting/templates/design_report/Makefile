COMMON_MK := $(shell find ../../.. -name common.mk -type f 2>/dev/null)
ifeq ($(COMMON_MK),)
$(error Could not find common.mk in parent directories)
endif
include $(COMMON_MK)