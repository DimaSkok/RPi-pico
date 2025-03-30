#include <stdio.h>
#include "pico/stdlib.h"
#include <string.h>

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

uint32_t read_memory(uint32_t address) {
    volatile uint32_t *ptr = (volatile uint32_t *)address;
    return *ptr;
}

int main() {
    stdio_init_all();
    if (pico_led_init() != PICO_OK) {
        printf("LED init failed\n");
        return 1;
    }
    printf("Ready\n"); 

    while (true) {
        char command[20];
        char* line = fgets(command, sizeof(command), stdin);

        if (!line) {
            printf("Ошибка чтения ввода.\n");
            continue;
        }

        command[strcspn(command, "\n")] = 0;

        if (strcmp(command, "led_on") == 0) {
            pico_set_led(true);
            printf("OK\n"); 
        } else if (strcmp(command, "led_off") == 0) {
            pico_set_led(false);
            printf("OK\n");  
        } else if (strncmp(command, "read_mem ", 9) == 0) {
            char *address_str = command + 9;
            char *endptr;
            uint32_t address = strtol(address_str, &endptr, 16);

            if (*endptr != '\0' && *endptr != ' ') {
                printf("Неверный формат адреса.\n");
            } else {
                uint32_t value = read_memory(address);
                printf("Память по адресу 0x%08X: 0x%08X\n", address, value);
                printf("OK\n");  
            }
        } else {
            printf("Неизвестная команда.\n");
        }
        sleep_ms(10);
    }
}