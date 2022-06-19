#!/usr/bin/env bash
docker run -itv "${PWD}:/External" ubuntu
apt update
apt install sudo
sudo apt-get install wget gdb gcc g++ libgmp-dev libmpfr-dev libmpfi-dev libpari-dev libgsl0-dev libxext-dev libpng-dev libjpeg-dev libreadline-dev libncurses5-dev mesa-common-dev libx11-dev libxt-dev libxft-dev libntl-dev libgl1-mesa-dev libgl-dev libao-dev hevea debhelper libfltk1.3-dev
sudo apt-get install build-essential git imagemagick libx11-dev libxext-dev libfreetype6-dev libpng-dev libjpeg-dev pkg-config gcc-arm-none-eabi binutils-arm-none-eabi dfu-util
cd External || exit 1
cd api || exit 1
make
cd ../ || exit 1
cd apps/KhiCAS || exit 1
chmod +x src/gmp-6.2.1/gen-fib
make