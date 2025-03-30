/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

#define OUTPUT_PIN 9

int my_gpio_init(void) {
    gpio_init(OUTPUT_PIN);
    gpio_set_dir(OUTPUT_PIN, GPIO_OUT);
}

void my_gpio_set(bool on) {
    gpio_put(OUTPUT_PIN, on);
}


int main() {
    stdio_init_all();
    my_gpio_init();
    printf("ADC Example, measuring GPIO26\n");
    
    adc_init();

    // Make sure GPIO is high-impedance, no pullups etc
    adc_gpio_init(26);
    // Select ADC input 0 (GPIO26)
    adc_select_input(0);

    while (1) {

        char s = getchar();

        if (s == 'e'){
            // 12-bit conversion, assume max value == ADC_VREF == 3.3 V
            my_gpio_set(true);
            const float conversion_factor = 3.3f / (1 << 12);
            uint16_t result = adc_read();
            printf("%f", result * conversion_factor);
            
        }
        
        if (s == 'd'){
            my_gpio_set(false);
            const float conversion_factor = 3.3f / (1 << 12);
            uint16_t result = adc_read();
            printf("%f", result * conversion_factor);
        }
        

    }
}
