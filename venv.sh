#!/bin/bash -ue

virtualenv .venv
. .venv/bin/activate
pip install soco mfrc522
