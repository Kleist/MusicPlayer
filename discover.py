#!/usr/bin/env python3

from soco import discover

for zone in discover():
    print(zone.player_name)
