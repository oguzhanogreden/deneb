import json
from pathlib import Path

import altair as alt
from altair_saver import save
import logme
from watchdog.events import FileSystemEventHandler
from watchdog.events import RegexMatchingEventHandler


@logme.log()
class Handler(RegexMatchingEventHandler):
    def __init__(self, regexes=[r".*"]):
        super().__init__(regexes)

    def make_path(self, path) -> Path:
        return Path(path)

    def make_plot_path(self, path):
        return path.name 

    def make_save_path(self, json_path: Path, name) -> Path:
        path = Path(json_path.parent, name)

        return path.with_suffix('.png')
        

    def read_chart(self, path: Path):
        with path.open('r') as f:
            spec = json.load(f)

        chart = alt.Chart.from_dict(spec)

        return chart

    def save_altair(self, chart, name):
        save(chart, name) 

    def _handle_event(self, event):
        try:
            if not event.is_directory:
                path = self.make_path(self.make_path(event.src_path))
                print(path)
                chart = self.read_chart(path)

                filename = self.make_plot_path(path)
                save_path = self.make_save_path(path, filename) 

                self.logger.info(f"Saving chart at {path} to {save_path}...")
                self.save_altair(chart, str(save_path))
                self.logger.info(f"Saving chart at {path} to {save_path}... DONE!")
        except:
            pass


    def on_created(self, event):
        self.logger.debug(f"Handling `on_created` event for {event.src_path}.")

        super().on_created(event)
        self._handle_event(event)

    def on_modified(self, event):
        self.logger.debug(f"Handling `on_modified` event for {event.src_path}.")

        super().on_modified(event)
        self._handle_event(event)

