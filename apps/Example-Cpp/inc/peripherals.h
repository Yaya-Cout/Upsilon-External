#ifndef EXAMPLE_CPP_PERIPHERALS_H_
#define EXAMPLE_CPP_PERIPHERALS_H_

#include <stdint.h>

namespace Peripherals {

extern long long unsigned int keymappings[16];
extern int keymappings_await[16];

void init_display();
void waitForKeyPressed();
void waitForKeyReleased();
void waitForKeyReleasedTimeout(int timeout);

} // namespace Peripherals

#endif // EXAMPLE_CPP_PERIPHERALS_H_
