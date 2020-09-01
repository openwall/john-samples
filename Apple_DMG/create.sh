#!/bin/sh

. vars.sh

for type in $types; do
    for algo in $algos; do
	for version in $versions; do
	    hdiutil create -passphrase $passphrase -size $size -type $type \
	    -imagekey encrypted-encoding-version=$version -encryption $algo \
	    $prefix.$algo.$size.header_v$version
	done
    done
done
