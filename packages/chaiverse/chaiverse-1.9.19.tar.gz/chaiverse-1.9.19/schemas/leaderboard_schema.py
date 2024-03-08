from datetime import datetime
from typing import List

import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
from tabulate import tabulate

from chaiverse.lib import dataframe_tools
from chaiverse.schemas.leaderboard_row_schema import LeaderboardRow


DEFAULT_LEADERBOARD_HEADER_MAPPING = {
    'double_thumbs_up_ratio': '👍👍_ratio',
    'thumbs_up_ratio': '👍👍+👍_ratio',
    'single_thumbs_up_ratio': '👍_ratio',
    'thumbs_down_ratio': '👎_ratio',
}

DEFAULT_LEADERBOARD_INCLUDES = [
    'developer_uid',
    'submission_id',
    'elo_rating',
    'win_ratio',
    'num_battles',
    'double_thumbs_up_ratio',
    'thumbs_down_ratio',
    'feedback_count',
    'model_score',
    'safety_score',
    'best_of',
    'max_input_tokens',
    'status',
    'model_repo',
    'reward_repo',
    'model_name', 
    'timestamp',
]

DEFAULT_LEADERBOARD_EXCLUDES = []

DEFAULT_LEADERBOARD_SORT_PARAMS = {
    'by': 'elo_rating',
    'ascending': False
}

DEFAULT_TABULATE_OPTIIONS = {
    'numalign': 'decimal',
}


class Leaderboard(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    leaderboard_rows: List[LeaderboardRow]
    
    @property
    def df(self) -> pd.DataFrame:
        leaderboard_rows = [row.all_fields_dict() for row in self.leaderboard_rows]
        df = pd.DataFrame.from_records(leaderboard_rows)
        df = _sort_by_values(df, **DEFAULT_LEADERBOARD_SORT_PARAMS)
        return df

    def to_display_df(self, includes=None, excludes=None, sort_params=None, header_mapping=None) -> pd.DataFrame:
        includes = includes or DEFAULT_LEADERBOARD_INCLUDES
        excludes = excludes or DEFAULT_LEADERBOARD_EXCLUDES
        sort_params = sort_params or DEFAULT_LEADERBOARD_SORT_PARAMS
        header_mapping = header_mapping or DEFAULT_LEADERBOARD_HEADER_MAPPING
        df = self.df
        df = _include_listed_columns(df, includes)
        df = _exclude_listed_columns(df, excludes)
        df = _sort_by_values(df, **sort_params)
        df = df.rename(columns=header_mapping)
        df['elo_rating']=df.elo_rating.astype(int)
        df = df.round(2)
        return df


def _include_listed_columns(df, includes):
    df = df[[column for column in includes if column in df.columns]]
    return df

def _exclude_listed_columns(df, excludes):
    df = df[[column for column in df.columns if column not in excludes]]
    return df

def _sort_by_values(df, by: List[str], ascending: bool):
    df = df.sort_values(by=by, ascending=ascending, na_position='last', ignore_index=True)
    df.index = np.arange(1, len(df)+1)
    return df
