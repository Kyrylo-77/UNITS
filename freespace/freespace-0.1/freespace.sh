#!/bin/bash

str=$(df -h | grep -v "loop" | grep "^/dev/" | sed -e's/  */ /g' | cut -f1,5,6 -d" ")

while read col1 col2 col3 ; do
  col2=$(echo $col2 | sed "s/%//")
  if [ $col2 -eq 100 ]; then
    echo "100%  "$col1"  "$col3 | logger -p local2.info -t freespace
  else
    echo $((100 - $col2))"%  "$col1"  "$col3 | logger -p local2.info -t freespace
  fi
done <<< "$str"
logger -p local2.notice -t freespace "Has been created free space report."
