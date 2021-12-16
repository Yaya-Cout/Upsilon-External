#ifndef CHIPEE_PERIPHERALS_H_
#define CHIPEE_PERIPHERALS_H_

#include <stdint.h>

extern long long unsigned int keymappings[16];
extern int keymappings_await[16];

void init_display();
void draw(unsigned char* display, char * rom_filename);
uint64_t kbd_handler();
void waitForKeyPressed();
void waitForKeyReleased();
void waitForKeyReleasedTimeout(int timeout);
int should_quit();

#endif
