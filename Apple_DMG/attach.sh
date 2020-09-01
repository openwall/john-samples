#!/bin/sh

. vars.sh

for img in testimage.*.{dmg,sparse{image,bundle}}; do
	echo "generating log files for $img"
	suffix=`echo $img|sed 's/testimage\.//;'`
	hdiutil attach -debug -passphrase $passphrase $img > attach.$suffix.stdout.log 2> attach.$suffix.stderr.log 
done

exit 0
