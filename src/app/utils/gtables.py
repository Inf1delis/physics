from dataclasses import dataclass
from datetime import datetime

import pandas as pd
import pygsheets
from pygsheets import VerticalAlignment

from app.settings.consts import TOTAL_DF_COL


@dataclass
class GTable:
    table_key: str
    service_file_path: str
    df: pd.DataFrame = None

    def __post_init__(self):
        gtable = pygsheets.authorize(
            service_file=self.service_file_path,
        )
        self.sh = gtable.open_by_key(self.table_key)

    def _gtable_wks(self, df, wks_name):
        try:
            wks = self.sh.worksheet_by_title(wks_name)
        except pygsheets.exceptions.WorksheetNotFound:
            wks = self.sh.add_worksheet(wks_name)
        wks.set_dataframe(df, (1, 1))
        to_letter = chr(ord("A") + df.shape[1] - 1)
        for cell in wks.range(f"A1:{to_letter}1")[0]:
            cell: pygsheets.Cell = cell
            cell.set_text_format("bold", True)
            cell.set_text_format("fontSize", 12)
            cell.set_vertical_alignment(VerticalAlignment.MIDDLE)

    def to_gsheet(self, df: pd.DataFrame, wks_name=None):
        if df.empty:
            return
        self._gtable_wks(df, wks_name)

    def from_gsheet(self, group_name: str) -> pd.DataFrame:
        wks = self.sh.worksheet_by_title(group_name)
        self.df = wks.get_as_df()
        return self.df

    def score_student(self, group_name: str, student_name: str, score: float, lesson_date: datetime):
        df = self.df
        if df is None:
            return f'Ошибка. Поиск давно не производился, сначала сделайте поиск.'
        df = df.drop([TOTAL_DF_COL], axis=1, errors='ignore')
        df.fillna(0.)

        name_col = df.columns[0]
        lesson_date_str = str(lesson_date.date())
        if lesson_date_str not in df:
            df[lesson_date_str] = 0.
        df.loc[df[name_col] == student_name, lesson_date_str] += score
        df[TOTAL_DF_COL] = df[df.columns[1:]].sum(axis=1)
        df = df.round(2)
        self.to_gsheet(df, group_name)
        return f'Баллы в количестве {score} добавлены студенту "{student_name}"'
