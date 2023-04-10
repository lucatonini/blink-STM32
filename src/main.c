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


/* Set STM32 to 72 MHz. */
static void clock_setup(void)
{
	rcc_clock_setup_pll(&rcc_hse_configs[RCC_CLOCK_HSE12_72MHZ]);

	/* Enable GPIOC clocks. */
	rcc_periph_clock_enable(RCC_GPIOC);
}

static void gpio_setup(void)
{
	/* LED */
	/* Set GPIO13 (in GPIO port C) to 'output push-pull'. */
	gpio_set_mode(GPIOC, GPIO_MODE_OUTPUT_50_MHZ,
		      GPIO_CNF_OUTPUT_PUSHPULL, GPIO13);

	// Set up GPIO pin
	// gpio_set_mode(GPIOC,
	// 	GPIO_MODE_OUTPUT_2_MHZ,
	// 	GPIO_CNF_OUTPUT_PUSHPULL,
	// 	GPIO13);

	/* Preconfigure the LEDs. */
	gpio_set(GPIOC, GPIO13);
}

int main(void) {

	clock_setup();
	gpio_setup();

	// Create infinte loop for blinking light
	while(1) {
		// Time out length. The higher the number the slower the blink
		for (int i = 0; i < 8000000; i++) {
			__asm__("nop");
		}

		// Toggle the light between on and off
		gpio_toggle(GPIOC, GPIO13);
	}
}
