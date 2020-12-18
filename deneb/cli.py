from pathlib import Path
import time

import click
import logme
from watchdog.observers import Observer

from .handler import Handler

path_type = click.Path(exists=True)

@click.command()
@click.argument('directory', default='/watch', type=path_type)
@click.argument('regex', default=r'.+json', type=str)
@logme.log()
def main(directory: str, regex: str, logger=None) -> None:
    logger.info(f"Watching '{directory}' for files matching '{regex}'.")

    path = Path(directory)
    regexes = [regex]

    event_handler = Handler(regexes=regexes)

    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
