from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import sentry_sdk

from randovania import monitoring

if TYPE_CHECKING:
    from pathlib import Path

    from randovania.lib import status_update_lib


@dataclasses.dataclass(frozen=True)
class GameExportParams:
    spoiler_output: Path | None


class GameExporter:
    @property
    def is_busy(self) -> bool:
        """
        Checks if the exporter is busy right now
        """
        raise NotImplementedError

    @property
    def export_can_be_aborted(self) -> bool:
        """
        Checks if export_game can be aborted
        """
        raise NotImplementedError

    def _before_export(self):
        pass

    def _do_export_game(
        self,
        patch_data: dict,
        export_params: GameExportParams,
        progress_update: status_update_lib.ProgressUpdateCallable,
    ) -> None:
        raise NotImplementedError

    def _after_export(self):
        pass

    def export_game(
        self,
        patch_data: dict,
        export_params: GameExportParams,
        progress_update: status_update_lib.ProgressUpdateCallable,
    ):
        self._before_export()
        try:
            with monitoring.attach_patcher_data(patch_data):
                with sentry_sdk.start_transaction(op="task", name="export_game") as span:
                    span.set_tag("exporter", type(self).__name__)
                    self._do_export_game(patch_data, export_params, progress_update)
        finally:
            self._after_export()
