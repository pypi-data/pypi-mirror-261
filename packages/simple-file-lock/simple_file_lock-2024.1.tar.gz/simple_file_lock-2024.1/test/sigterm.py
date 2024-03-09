#!/usr/bin/env python3
'''
Manual test for lockfile removal on SIGINT.
'''

import logging
import os
import pathlib
import shutil
import signal
import sys
import tempfile
import time

from simple_file_lock import FileLock


LOGGER = logging.getLogger(__name__)


def test():
    '''
    Test lockfile removal on keyboard interrupt.
    '''
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = pathlib.Path(tmp_dir)
        path = tmp_dir / 'test.txt'

        def sigterm_handler(_sig, _frame):
            '''
            Check if the temporary directory is empty and remove it.
            '''
            is_empty = not list(tmp_dir.iterdir())
            shutil.rmtree(tmp_dir)
            if is_empty:
                LOGGER.info('The lock file was removed.')
                sys.exit(os.EX_OK)
            else:
                LOGGER.error('The lock file was not removed.')
                sys.exit(os.EX_SOFTWARE)

        signal.signal(signal.SIGINT, sigterm_handler)
        signal.signal(signal.SIGTERM, sigterm_handler)

        with FileLock(path):
            print(
                f'Kill process {os.getpid():d} to test SIGTERM handling.'
            )
            while True:
                time.sleep(500)
    return os.EX_OK


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        sys.exit(test())
    except KeyboardInterrupt:
        pass
