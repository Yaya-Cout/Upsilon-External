# test pyb module on F411 MCUs

import os, pyb

if 'STM32F411' not in os.uname().machine:
    print('SKIP')
    raise SystemExit

print(pyb.freq())
