#!/usr/bin/env python3

import logging
import sys
import config

import soco
from soco.music_services import MusicService
from soco.music_services.accounts import Account
from soco.music_library import MusicLibrary

def open_device(name):
    device = soco.discovery.by_name(name)
    if not device:
        raise RuntimeError(f'Device "{name}" not found')
    if not device.is_coordinator:
        logging.info("Not coordinator")
        device = device.group.coordinator
        logging.info("Using {}".format(device.player_name))
    return device

def find(device, title):
    library = device.music_library
    result = library.browse()
    favs = library.get_sonos_favorites()
    for fav in favs:
        if fav.title.lower().startswith(title.lower()):
            print(fav.title)
            return
    print("{} not found in {}".format(title, list(fav.title for fav in favs)))

def main(title, verbose):
    device = open_device(config.DEVICE_NAME)
    if verbose:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
    find(device, title)
    
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('title')
    parser.add_argument('-v', '--verbose', action="store_true")
    args = parser.parse_args()
    main(args.title, args.verbose)
