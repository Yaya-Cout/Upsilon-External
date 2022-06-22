# Installing SDK

Currently, only Debian-based Linux distributions are supported natively. You can try to install the Upsilon's SDK on your system and then flash your project, but it's not guaranteed to work.

## Debian-based distributions

The following commands should work on Debian-based Linux distributions. It will install all the dependencies to build KhiCAS and all others applications. Some of them are required only for KhiCAS.

```shell
sudo apt-get install wget gdb gcc g++ libgmp-dev libmpfr-dev libmpfi-dev libpari-dev libgsl0-dev libxext-dev libpng-dev libjpeg-dev libreadline-dev libncurses5-dev mesa-common-dev libx11-dev libxt-dev libxft-dev libntl-dev libgl1-mesa-dev libgl-dev libao-dev hevea debhelper libfltk1.3-dev build-essential git imagemagick libx11-dev libxext-dev libfreetype6-dev libpng-dev libjpeg-dev pkg-config gcc-arm-none-eabi binutils-arm-none-eabi dfu-util texinfo autoconf-archive
```

## Other distributions

There is a Dockerfile to build the SDK for other distributions, but it's not available on DockerHub. To build the SDK, you need to install docker and to run the following command:

```shell
docker build -t external .
```

Once the image is built, you can run it using the following command to build your project:

```shell
docker run -itv $PWD:/External external make KhiCAS_rebuild
```

Replace `KhiCAS` with the name of your project.
You can remove the `make KhiCAS_rebuild` command if you want a shell.

Once the project is built, you have to flash it, but the `make KhiCAS_flash` command is not available on Docker and it execute `make KhiCAS_rebuild`. So to flash your project, you need to edit the Makefile to remove the `%_rebuild` dependency for the `%_flash` command.

Don't forget to restore the Makefile before you commit your changes.

---

Once the SDK is installed, you follow the steps in [the external applications creation guide](/docs/new-app.md)]