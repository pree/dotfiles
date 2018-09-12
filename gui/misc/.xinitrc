source /etc/X11/xinit/xinitrc.d/50-systemd-user.sh
xset s off
xset -dpms
xset s noblank
exec spotifyd --no-daemon &
exec spotify &
exec i3
