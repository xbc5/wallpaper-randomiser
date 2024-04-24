#!/bin/env python3

import os
import time
import subprocess
import yaml
import random
from glob import glob

DEFAULT_CFG = {
  "interval_mins": 30,
  "wallpaper_dir": "~/.wallpapers"
}

def load_config():
  try:
    with open("/etc/wallpaper-ranomiser.yaml", "r") as f:
      y = yaml.safe_load(f)
      return {**DEFAULT_CFG, **y}
  except FileNotFoundError:
    return DEFAULT_CFG

CFG = load_config()
WP_DIR = os.path.expanduser(CFG["wallpaper_dir"])
os.makedirs(WP_DIR, exist_ok=True)
INTERVAL = CFG["interval_mins"]

def send_err():
  subprocess.call(["notify-send", "--urgency=critical", "--expire-time=10000",
                   "No wallpapers to randomise\nin {}".format(WP_DIR)])

def find_images():
  file_extensions = [".jpg", ".png"]
  patterns = [os.path.join(WP_DIR, "*" + ext) for ext in file_extensions]
  files = [file for pattern in patterns for file in glob(pattern)]
  random.shuffle(files)
  return files

def swap(arr):
  if len(arr) > 1:
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
  return arr

ERR_SENT = False
IMAGES = []
RANDOM_IMAGE=""

while True:
  if not IMAGES:
    IMAGES = find_images()

  if not IMAGES:
    if not ERR_SENT:
      send_err()
      ERR_SENT = True
    time.sleep(30)
    continue

  # sometimes the first queued image is the sames as the previous image
  if RANDOM_IMAGE == IMAGES[-1]:
    swap(IMAGES)

  RANDOM_IMAGE = IMAGES.pop()
  subprocess.call(["feh", "--bg-scale", RANDOM_IMAGE])
  interval_seconds = INTERVAL * 60
  time.sleep(interval_seconds)
