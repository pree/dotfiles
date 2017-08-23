#!/bin/sh
scrot /tmp/lock.png
convert /tmp/lock.png -scale 5% -scale 2000% /tmp/lock.png
convert /tmp/lock.png $HOME/.config/i3/img/lock.png -gravity center -composite -matte /tmp/lock.png
i3lock -i /tmp/lock.png
rm /tmp/lock.png
