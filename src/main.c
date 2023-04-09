/**
 * @{
 * @file      main.c
 * @brief     Main execution file
 *
 * @author    L. Tonini
 * @date      09/04/2023
 *
 * @copyright Copyright 2023 Luca Tonini
 */

#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

int main(void) {

	// Enable GPIO pin
	rcc_periph_clock_enable(RCC_GPIOC);

	// Set up GPIO pin
	gpio_set_mode(GPIOC,
		GPIO_MODE_OUTPUT_2_MHZ,
		GPIO_CNF_OUTPUT_PUSHPULL,
		GPIO13);

	// Create infinte loop for blinking light
	while(1) {
		// Time out length. The higher the number the slower the blink
		for (int i = 0; i < 1000000; i++) {
			__asm__("nop");
		}

		// Toggle the light between on and off
		gpio_toggle(GPIOC, GPIO13);
	}
}
