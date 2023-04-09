# Blink-STM32
A simple LED blink STM32 (blue pill) application using libopencm3

# Instructions
 1. git clone --recurse-submodules https://github.com/lucatonini/blink-STM32.git blink-STM32
 2. cd blink-STM32
 3. make -C libopencm3 # (Only needed once)
 4. make -C src
 5. Once STM32 and ST-Link are connected to your computer, run the follwing to flash the application: st-flash write build/blink-STM32.bin 0x8000000

# Dependencies
 * st-link
 * make
 * gcc

# Hardware
 * STM32 (Blue Pill)
 * ST-LINK V2
 * Jumper Cables x4

# Directories
 * Source contains application code
 * Library contains other repo code.
