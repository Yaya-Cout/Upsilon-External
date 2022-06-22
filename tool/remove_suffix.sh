#!/usr/bin/env sh
# Remove suffix given in $1 from the string $2
# $1: suffix to remove
# $2: string to remove suffix from

string="$1"
suffix="$2"


if [ -z "${suffix}" ]; then
    echo "Usage: $0 <string> <suffix>"
    exit 1
fi


# Get the length of the suffix
suffix_length="$(echo -n "${suffix}" | wc -c)"
# Get the length of the string
string_length="$(echo -n "${string}" | wc -c)"
# Get the length of the string minus the suffix
string_length_minus_suffix="$(expr "${string_length}" - "${suffix_length}")"
# If the suffix is longer than the string, exit
if [ "${suffix_length}" -gt "${string_length}" ]; then
    echo "Suffix is longer than the string"
    exit 1
fi
# Get if the string matches the suffix
string_matches_suffix="$(echo -n "${string}" | tail -c "${suffix_length}")"
# If the string doesn't match the suffix, exit
if [ "${string_matches_suffix}" != "${suffix}" ]; then
    echo "String doesn't match the suffix"
    exit 1
fi
# Get the string without the suffix
string="$(echo -n "${string}" | head -c "${string_length_minus_suffix}")"
# Print the string
echo "${string}"