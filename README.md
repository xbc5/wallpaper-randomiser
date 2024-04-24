# Wallpaper Randomiser

## Description

Select a random wallpaper, from the local file system, every N minutes.

It will cycle through all images randomly in sequence -- so no images are left unused for long periods.

## Native Dependencies

`feh`, `notify-send`.

## Install

```sh
./install.sh i
```

This will enable the `wallpaper-randomiser.service` too, as a user service.

## Usage

Simply place jpg or png files in the `wallpaper_dir`, which defaults to `~/.wallpapers`.

## Config

The config file lives at `/etc/wallpaper-randomiser.yaml`, and the (implicit) default values are:
```yaml
interval_mins: 30
wallpaper_dir: ~/.wallpapers
```

## Uninstall

```sh
./install.sh u
```
