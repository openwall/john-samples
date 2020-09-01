PHONY = clean sanitize all create attach

all:	create attach sanitize

clean:
	rm -f testimage.*.{dmg,sparseimage}
	rm -rf testimage.*.sparsebundle
	rm -f attach.*.log

create:
	sh create.sh

attach:
	sh attach.sh

sanitize:
	sh sanitize.sh
