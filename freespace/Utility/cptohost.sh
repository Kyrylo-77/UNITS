#/bin/bash

ssh -p2300 -lroot 127.1 'cat >/root/rpmbuild/SOURCES/freespace-0.1.tar.gz' < freespace-0.1.tar.gz
ssh -p2300 -lroot 127.1 'cat >/root/rpmbuild/SPECS/freespace.spec' < ../freespace.spec