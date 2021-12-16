#include "inc/peripherals.h"
#include "extapp_api.h"
#include <string.h>


/**
 * Mapping Keyboard Keys
 *
 * A new layout is being used, not the original one:
 *
 * 7 8 9 (
 * 4 5 6 x
 * 1 2 3 +
 * 0 . e Ans
 */
long long unsigned int keymappings[16] = {
    SCANCODE_Seven, SCANCODE_Eight, SCANCODE_Nine, SCANCODE_LeftParenthesis,
    SCANCODE_Four, SCANCODE_Five, SCANCODE_Six, SCANCODE_Multiplication,
    SCANCODE_One, SCANCODE_Two, SCANCODE_Three, SCANCODE_Plus,
    SCANCODE_Zero, SCANCODE_Dot, SCANCODE_EE, SCANCODE_Ans
};

int keymappings_await[16] = {
    KEY_CHAR_7, KEY_CHAR_8, KEY_CHAR_9, KEY_CHAR_LPAR,
    KEY_CHAR_4, KEY_CHAR_5, KEY_CHAR_6, KEY_CHAR_MULT,
    KEY_CHAR_1, KEY_CHAR_2, KEY_CHAR_3, KEY_CHAR_PLUS,
    KEY_CHAR_0, KEY_CHAR_DP, KEY_CHAR_EXP, KEY_SHIFT_ANS
};

int QUIT = 0;

/**
 * init_display: initialize SDL display
 * @param void
 * @return void
 */
void init_display(void) {
    extapp_pushRectUniform(0, 18, 320, 222, 0xFFFF);
}

void draw(unsigned char* display, char * rom_filename) {
    extapp_drawTextLarge("                                ", 0, 0, 0xFFFF, 0x0000, false);
    extapp_drawTextLarge(rom_filename, 0, 0, 0xFFFF, 0x0000, false);

    // iterating thru the display (64*32)
    for (int y = 0; y < 32; y++) {
        for (int x = 0; x < 64; x++) {
            if (display[x + (y * 64)]) {
                extapp_pushRectUniform(x * 3 + 125, y * 3 + 130, 3, 3, 0xFFFF);
            } else {
                extapp_pushRectUniform(x * 3 + 125, y * 3 + 130, 3, 3, 0x0000);
            }
        }
    }
}

uint64_t kbd_handler(void) {
    uint64_t kb = extapp_scanKeyboard();
    if (kb & SCANCODE_Back || kb & SCANCODE_OnOff || kb & SCANCODE_Home) {
        QUIT = 1;
    }
    return kb;
}

void waitForKeyPressed(void) {
  while(!extapp_scanKeyboard()) {
    extapp_msleep(10);
  }
}

void waitForKeyReleased(void) {
  while(extapp_scanKeyboard()) {
    extapp_msleep(10);
  }
}

void waitForKeyReleasedTimeout(int timeout) {
  while(extapp_scanKeyboard() && timeout > 0) {
    extapp_msleep(10);
    timeout -= 10;
  }
}

/**
 * should_quit: return QUIT status
 * @param void
 * @return QUIT flag
 */
int should_quit(void) { return QUIT; }
