#!/usr/bin/sh
# Rebuild the given application with the _rebuild suffix
# $1: application to rebuild

# Get the application name
application="$1"
# Remove the suffix
application_without_suffix="$(echo "${application}" | sed -e 's/_rebuild//')"
echo "Rebuilding ${application_without_suffix}"
# Clean the application
./tool/clean.sh "${application_without_suffix}"
# Rebuild the application
make -C "apps/${application_without_suffix}"