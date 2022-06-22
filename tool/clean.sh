#!/usr/bin/env sh
# Clean the given application.
# $1: application name (can contain _clean suffix)

# Get the application name
application="$1"
# Remove the suffix from $1
application="$(echo "${application}" | sed -e 's/_clean//')"
echo "Cleaning ${application}"
# If directory doesn't exist, interpret it as a application name
if [ ! -d "${application}" ]; then
    application="apps/${application}"
fi
# Clean the application
make -C "${application}" clean