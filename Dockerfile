# Define base image
FROM ubuntu:latest
# Setup commands
RUN apt-get update
RUN apt-get install wget gdb gcc g++ libgmp-dev libmpfr-dev libmpfi-dev libpari-dev libgsl0-dev libxext-dev libpng-dev libjpeg-dev libreadline-dev libncurses5-dev mesa-common-dev libx11-dev libxt-dev libxft-dev libntl-dev libgl1-mesa-dev libgl-dev libao-dev hevea debhelper libfltk1.3-dev build-essential git imagemagick libx11-dev libxext-dev libfreetype6-dev libpng-dev libjpeg-dev pkg-config gcc-arm-none-eabi binutils-arm-none-eabi dfu-util texinfo autoconf-archive -y
# We won't use add or copy, because we want to use the Dockerfile only to build the app, while editing the app from the host
# Define the working directory
WORKDIR /External
# Open a shell, to let the user execute commands
CMD ["/bin/bash"]