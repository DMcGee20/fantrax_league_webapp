import pandas as pd

def team_strengths(df: pd.DataFrame):
    """Aggregate stats by team"""
    numeric_cols = ["HR", "RBI", "AVG", "SB", "ERA", "K"]
    return df.groupby("team")[numeric_cols].mean().reset_index()

def free_agent_targets(fa_df: pd.DataFrame, stat: str = "HR", top_n: int = 5):
    """Return top free agents for a given stat"""
    return fa_df.sort_values(stat, ascending=False).head(top_n)