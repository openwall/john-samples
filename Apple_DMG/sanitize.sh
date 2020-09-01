#!/bin/sh
# sanitize some data we don't want to have in the public log files
# please be careful with this if you don't know what you're doing.

perl -i -pe 's|/Users/.*?/Coding|/Users/xxx|g' attach.*.log
perl -i -pe 's|/Users/.*? Apple_HFS|/Users/xxx/Coding|g' attach.*.log
perl -i -pe 's|got ........-....-....-....-............|got XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX|g' attach.*.log
perl -i -pe 's|/Volumes/.*? Apple_HFS|/Volumes/xxx|g' attach.*.log
perl -i -pe 's|........-....-....-....-............$|XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX|g' attach.*.log
