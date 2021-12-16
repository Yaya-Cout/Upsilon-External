#define _XOPEN_SOURCE 500

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "extapp_api.h"

#include "inc/peripherals.h"
#include "inc/selector.h"
#include <stdlib.h>

void extapp_main(void) {
    const char * filename = select_rom();
    init_display();
    extapp_drawTextSmall("[PENDING] Loading file...", 0, 20*1, 0x0000, 0xFFFF, false);

    size_t file_len = 0;
    if (extapp_fileExists(filename, EXTAPP_FLASH_FILE_SYSTEM)) {
        uint8_t* filecontent = (uint8_t*) extapp_fileRead(filename, &file_len, EXTAPP_FLASH_FILE_SYSTEM);
        extapp_drawTextSmall("[PENDING] File loaded, copying...", 0, 20*2, 0x0000, 0xFFFF, false);
        // For some reason, we have to add a dummy character at the beginning of the buffer otherwise the first character will be removed
        uint8_t* filecontenttowrite = (uint8_t*)malloc(file_len+1);
        filecontenttowrite[0] = ' ';
        // filecontenttowrite = " ";
        // filecontenttowrite = (uint8_t)filecontenttowrite + (uint8_t)filecontent;
        // strncpy(filecontenttowrite, " ", sizeof(filecontenttowrite));
        strncat(filecontenttowrite+1, filecontent, file_len);
        extapp_fileWrite(filename, filecontenttowrite, strlen(filecontenttowrite)+1, EXTAPP_RAM_FILE_SYSTEM);
        extapp_drawTextSmall("[OK] File copied successfully!", 0, 20*3, 0x0000, 0xFFFF, false);
        free(filecontenttowrite);
    }
    else {
        extapp_drawTextSmall("[FAILED] Error while loading file", 0, 20*2, 0x0000, 0xFFFF, false);
        waitForKeyPressed();
        return;
    }

    extapp_drawTextSmall("[OK] Done!", 0, 20*4, 0x0000, 0xFFFF, false);
    extapp_drawTextSmall("[OK] Press any key to continue", 0, 20*5, 0x0000, 0xFFFF, false);
    waitForKeyPressed();
    return;
}
