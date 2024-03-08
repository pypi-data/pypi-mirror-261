from chaiverse.http_client import SubmitterClient
from chaiverse.lib import dataframe_tools
from chaiverse.schemas import Leaderboard
from chaiverse import config


def get_leaderboard() -> Leaderboard:
    submitter_client = SubmitterClient()
    leaderboard = submitter_client.get(config.LATEST_LEADERBOARD_ENDPOINT)
    leaderboard = Leaderboard(**leaderboard)
    return leaderboard


def display_leaderboard():
    leaderboard = get_leaderboard()
    display_df = leaderboard.to_display_df()
    formatted = dataframe_tools.format_dataframe(display_df)
    print(formatted)
