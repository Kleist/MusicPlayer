#!/usr/bin/env python3

import logging
import sys

import soco
from soco.music_services import MusicService
from soco.music_services.accounts import Account
from soco.music_library import MusicLibrary

def stop():
    device = soco.discovery.by_name("Stue")
    device.stop()

def play(title):
    device = soco.discovery.by_name("Stue")
    if not device.is_coordinator:
        print("Not coordinator")
        device = device.group.coordinator
        print("Using {}".format(device.player_name))
    library = device.music_library
    
    favs = library.get_sonos_favorites()
    for fav in favs:
        if fav.title.lower().startswith(title.lower()):
            print("Playing {}".format(fav.title))
            device.clear_queue()
            device.add_to_queue(fav.reference)
            device.play()
            return
    print("{} not found in {}".format(title, list(fav.title for fav in favs)))

def main(title, verbose):
    if verbose:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)

    play(title)
    
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('title')
    parser.add_argument('-v', '--verbose', action="store_true")
    args = parser.parse_args()
    main(args.title, args.verbose)
