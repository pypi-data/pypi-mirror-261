"""
Setup method for lbtguiders azcamconsole.
Usage example:
  python -i -m azcam_lbtguiders.console
"""

import os
import sys
import threading

import azcam
import azcam.utils
import azcam.console
import azcam.console.shortcuts
from azcam.server.tools.ds9display import Ds9Display


def setup():
    # command line args
    try:
        i = sys.argv.index("-datafolder")
        datafolder = sys.argv[i + 1]
    except ValueError:
        datafolder = None
    try:
        i = sys.argv.index("-lab")
        lab = 1
    except ValueError:
        lab = 0

    # files and folders
    azcam.db.systemname = "lbtguiders"

    azcam.db.systemfolder = f"{os.path.dirname(__file__)}"
    azcam.db.datafolder = azcam.utils.get_datafolder(datafolder)

    parfile = os.path.join(
        azcam.db.datafolder,
        "parameters",
        f"parameters_console_{azcam.db.systemname}.ini",
    )

    # start logging
    logfile = os.path.join(azcam.db.datafolder, "logs", "console.log")
    azcam.db.logger.start_logging(logfile=logfile)
    azcam.log(f"Configuring console for {azcam.db.systemname}")

    # display
    display = Ds9Display()
    dthread = threading.Thread(target=display.initialize, args=[])
    dthread.start()  # thread just for speed

    # console tools
    from azcam.console.tools import create_console_tools

    create_console_tools()

    # try to connect to azcamserver
    server = azcam.db.tools["server"]
    connected = server.connect()
    if connected:
        azcam.log("Connected to azcamserver")
    else:
        azcam.log("Not connected to azcamserver")

    # par file
    azcam.db.parameters.read_parfile(parfile)
    azcam.db.parameters.update_pars("azcamconsole")


# start
setup()
from azcam.cli import *
