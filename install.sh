#!/bin/bash
function _install() {
  # Create directory if it doesn't exist and change ownership to root
  sudo mkdir -p /usr/local/lib/scripts
  sudo chown root:root /usr/local/lib/scripts

    # Move the wallpaper-randomiser.py to the directory and change permissions
  sudo cp ./wallpaper-randomiser.py /usr/local/lib/scripts
  sudo chown root:root /usr/local/lib/scripts/wallpaper-randomiser.py
  sudo chmod 755 /usr/local/lib/scripts/wallpaper-randomiser.py

    # Create ~/.config/systemd/user directory if it doesn't exist and copy the service file
  mkdir -p ~/.config/systemd/user
  cp ./wallpaper-randomiser.service ~/.config/systemd/user/wallpaper-randomiser.service

    # Reload the user daemon and enable/start the service
  systemctl --user daemon-reload
  systemctl --user enable wallpaper-randomiser.service
  systemctl --user start wallpaper-randomiser.service
}

function uninstall() {
  systemctl --user stop wallpaper-randomiser.service
  systemctl --user disable wallpaper-randomiser.service

  rm ~/.config/systemd/user/wallpaper-randomiser.service
  sudo rm /usr/local/lib/scripts/wallpaper-randomiser.py

  systemctl --user daemon-reload
}

function _help() {
  cat <<EOF
Usage: `basename $0` [install | uninstall]

COMMANDS:
   i,install     install the script and service, enable and run it
   u,uninstall   disable it, and remove all traces
   h,help        display this help menu

EOF
}

case "$1" in
  i|install) _install;;
  u|uninstall) _uninstall;;
  h|help) _help;;
  *) echo -e "Unknown command\n"; _help;;
esac
