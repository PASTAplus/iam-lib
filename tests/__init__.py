"""
:Mod: __init__

:Synopsis:

:Author:
    servilla

:Created:
    5/4/2025
"""
import logging
from pathlib import Path

import daiquiri


cwd = Path("../tests").resolve().as_posix()
logfile = cwd + "/tests.log"
daiquiri.setup(
    level=logging.DEBUG,
    outputs=(daiquiri.output.File(logfile), "stdout",)
)
logger = daiquiri.getLogger(__name__)

test_data_path = cwd + "/data"