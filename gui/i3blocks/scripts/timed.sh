#!/usr/bin/env bash
out=""
ac=$(/home/pascalr/.bin/timedctl --no-renew-token ac s)
if [[ $? -eq 0 ]]
then
  out=$(echo $ac | cut -d ":" -f 2- | cut -d ">" -f 1,2)
  echo " $out"
else
  out=$(echo $ac | cut -d ":" -f 2-)
  echo "<span background='red' foreground='white'> $out </span>"
fi
