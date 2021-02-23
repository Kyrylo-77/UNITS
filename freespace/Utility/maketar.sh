#/bin/bash

tar czf freespace-0.1.tar.gz ../freespace-0.1/
ssh -p2300 -lroot 127.1 'cat >/root/rpmbuild/SOURCES/freespace-0.1.tar.gz' < freespace-0.1.tar.gz