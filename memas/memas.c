#include <stdio.h>
#include "pico/stdlib.h"

int pico_led_init(void) {
#if defined(PICO_DEFAULT_LED_PIN)
    // A device like Pico that uses a GPIO for the LED will define PICO_DEFAULT_LED_PIN
    // so we can use normal GPIO functionality to turn the led on and off
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
    return PICO_OK;
#elif defined(CYW43_WL_GPIO_LED_PIN)
    // For Pico W devices we need to initialise the driver etc
    return cyw43_arch_init();
#endif
}

// Turn the led on or off
void pico_set_led(bool led_on) {
#if defined(PICO_DEFAULT_LED_PIN)
    // Just set the GPIO on or off
    gpio_put(PICO_DEFAULT_LED_PIN, led_on);
#elif defined(CYW43_WL_GPIO_LED_PIN)
    // Ask the wifi "driver" to set the GPIO on or off
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, led_on);
#endif

}

int main()
{
    stdio_init_all();
    if (pico_led_init() != PICO_OK) {
        printf("LED init failed\n");
        return 1;
    }

    while (true) {
        char st = getchar();

        if (st == 'e'){
            pico_set_led(true);
        }

        if (st == 'd'){
            pico_set_led(false);
        }
        if (st == 'm'){
            st = getchar();
            if (st == 'e'){
                st = getchar();
                if (st == 'm'){
                    pico_set_led(true);
                    sleep_ms(1000);     // тута нужно принять 8 символов и выплюнуть нужные 8 символов
                    char* s = readline();
                    pico_set_led(false);
                }
            }
        }
    }

    sleep_ms(10);
}
