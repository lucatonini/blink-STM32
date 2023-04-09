PROJECT = ../build/blink-STM32
BUILD_DIR = ../build/source/

CFILES = main.c

# This is the tyupe of board I am using (You may need to change these 2 lines)
DEVICE=stm32f103c8
OOCD_FILE = board/stm32f4discovery.cfg

# You shouldn't have to edit anything below here.
VPATH += $(SHARED_DIR)
INCLUDES += $(patsubst %,-I%, . $(SHARED_DIR))
OPENCM3_DIR=../lib/libopencm3

include $(OPENCM3_DIR)/mk/genlink-config.mk
include ../rules.mk
include $(OPENCM3_DIR)/mk/genlink-rules.mk
