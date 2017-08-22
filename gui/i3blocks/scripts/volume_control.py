#!/usr/bin/env python3
import subprocess
import sys

from executor import execute

def get_active_sink():
  return execute('pacmd list-sinks | grep "* index" | awk \'{print $3}\'', capture=True)

def get_volume():
  # return execute('amixer -D pulse get Master | grep -o "\[.*%\]" | grep -o "[0-9]*" | head -n1')[0]
  return execute('pactl list sinks | grep "^[[:space:]]Volume:" | head -n $((' + get_active_sink() + ' + 1)) | tail -n 1 | sed -e "s,.* \\([0-9][0-9]*\\)%.*,\\1,"', capture=True)

def set_volume(percentage):
  execute('pactl set-sink-volume ' + get_active_sink() + ' ' + str(percentage) + '%')
  emit_signal()

def toggle_volume():
  execute('pactl set-sink-mute ' + get_active_sink() + ' toggle')
  emit_signal()

def is_muted():
  if execute("pactl list sinks | grep '^[[:space:]]Mute:' | head -n $((" + get_active_sink() + " + 1)) | tail -n 1 | awk '{print $2}'", capture=True) == "yes":
    return True
  else: return False

def write(message):
  sys.stdout.write(message)
  sys.stdout.flush()

def trim_to_range(volume):
  volume = int(volume)
  if volume < 0:
    volume = 0
  elif volume > 200:
    volume = 200
  return volume

def status():
  if int(get_volume()) == 0 or is_muted():
    return 'muted'
  else:
    return 'on'

def emit_signal():
  execute('pkill -RTMIN+1 i3blocks')

if __name__ == '__main__':
  command = sys.argv[1]

  if command == 'set':
    set_volume(trim_to_range(sys.argv[2]))
  elif command == 'up':
    new_volume = trim_to_range(int(get_volume()) + int(sys.argv[2]))
    set_volume(new_volume)
  elif command == 'down':
    new_volume = trim_to_range(int(get_volume()) - int(sys.argv[2]))
    set_volume(new_volume)
  elif command == 'toggle':
    toggle_volume()
  elif command == 'read':
    write(get_volume())
  elif command == 'status':
    write(status())
  elif command == 'i3blocks':
    output = get_volume() + ' '
    if is_muted():
      output += '\n\n#cc241d'
    write(output)
  elif command == 'signal':
    emit_signal()
  else:
    write('Usage: ' + sys.argv[0] + ' [set|up|down|toggle|read|status] [value]\n')
