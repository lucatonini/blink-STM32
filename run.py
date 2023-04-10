#!/usr/bin/env python
# encoding: utf-8
"""
Python run script

optional arguments:
  -h, --help            show this help message and exit
  --build               Build the binaries of the application
  --flash               Flash the binaries to hardware using the ST-Link V2
  --clean

"""

import glob
import sys
import argparse
import os
from os import path
import shutil
from shutil import copytree, ignore_patterns
import logging
import colorlog
from colorlog import ColoredFormatter
from alive_progress import alive_bar

def main():

    # Setup arguments
    parser = argparse.ArgumentParser(description=
    '''STM32 blink application master script, to build and flash compiled binaries''')
    parser.add_argument("--build",
                        help="Build the binaries of the application",
                        action='count', default=0)
    parser.add_argument("--flash",
                        help="Flash the binaries to hardware using the ST-Link V2",
                        action='count', default=0)
    parser.add_argument("--clean",
                        help="Clean up the build directories",
                        action='count', default=0)
    parser.add_argument("--debug",
                        help="Set logging level to debug",
                        action='count', default=0)

    args = parser.parse_args()

    # Setup logging system
    LOG_LEVEL = logging.INFO
    LOGFORMAT = " %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"

    # Change logging level if flag was passed
    if args.debug >= 1:
      LOG_LEVEL = logging.DEBUG

    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(LOGFORMAT)

    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)

    log = logging.getLogger('alive_progress')
    log.setLevel(LOG_LEVEL)
    log.addHandler(stream)

    log.debug("Arguments passed:")
    log.debug("args.build = " + str(args.build))
    log.debug("args.flash = " + str(args.flash))
    log.debug("args.clean = " + str(args.clean))
    log.debug("args.debug = " + str(args.debug))

    # Set up commands to be executed
    commands = []

    if args.clean > 0:
      commands.append("rm -rf build/")

    if args.build > 0:
      commands.append("make -C lib/libopencm3/")
      commands.append("make -C src")

    if args.flash > 0:
      commands.append("st-flash write build/blink-STM32.bin 0x8000000")

    log.debug(str(commands))

    with alive_bar(len(commands),title='Processing', length=40, bar='blocks', spinner='waves2') as bar:
      for command in commands:
        log.info("Running command: " + command)
        commandStream = os.popen(command)
        output = commandStream.read()
        log.debug(output)
        bar()


if __name__ == '__main__':

    sys.exit(main())
