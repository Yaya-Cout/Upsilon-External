# KhiCAS

KhiCAS is a swiss knife for the mathematics. It's a port of xCAS for the calculator.

It's a bit complex to use, but when you know how to use it, you can do a lot of things. The interface is a shell, with some menus.

## Updating KhiCAS

To update KhiCAS, you have some things to do:

1. Download the latest version of KhiCAS from Parisse's website using `wget https://www-fourier.univ-grenoble-alpes.fr/~parisse/numworks/khiext.tgz`
2. Extract the archive using `tar xvfz khiext.tgz`
3. Copy the contents of the folder `khiext/apps/KhiCAS` to the folder `apps/KhiCAS`
4. Now, you have the new version of KhiCAS, but you have to apply some changes to the code.
5. Replace `inline bool iskeydown(int key){ return getkey(key | 0x80000000); }` by `inline bool iskeydown(int key);`
6. Add this code in the file `apps/KhiCAS/main.cpp`:

```cpp
bool iskeydown(int key) {
  return extapp_isKeydown(key);
}
```

7. If you have an error like `arm-none-eabi-ar: add.o: No such file or directory`, try to execute `make distclean` in the `apps/KhiCAS/src/gmp-6.2.1` folder. Try to rebuild KhiCAS after that. If it works, check if the `make distclean` command exists in the GMP section of `apps/KhiCAS/buildDeps`.
