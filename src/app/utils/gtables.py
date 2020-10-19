from dataclasses import dataclass

import pandas as pd
import pygsheets

from app.settings import CONFIG


@dataclass
class GTable:
    table_key: str
    service_file_path: str

    def __post_init__(self):
        gtable = pygsheets.authorize(service_file=self.service_file_path)
        self.sh = gtable.open_by_key(self.table_key)

    def _gtable_wks(self, df, wks_name):
        try:
            wks = self.sh.worksheet_by_title(wks_name)
        except pygsheets.exceptions.WorksheetNotFound:
            wks = self.sh.add_worksheet(wks_name)
        wks.set_dataframe(df, (1, 1), fit=True)
        to_letter = chr(ord("A") + df.shape[1] - 1)
        for cell in wks.range(f"A1:{to_letter}1")[0]:
            cell: pygsheets.Cell = cell
            cell.set_text_format("bold", True)
            cell.set_text_format("fontSize", 12)

    def to_gsheet(self, df: pd.DataFrame, wks_name=None):
        if df.empty:
            return

        if wks_name is not None:
            self._gtable_wks(df, wks_name)
            return

    def from_gsheet(self, group_name: str) -> pd.DataFrame:
        wks = self.sh.worksheet_by_title(group_name)
        return wks.get_as_df()


def parse_gtable(group_name: str):
    gtable = GTable(CONFIG['gtable_key'], CONFIG['gtable_credentials_path'])
    return gtable.from_gsheet(group_name)
