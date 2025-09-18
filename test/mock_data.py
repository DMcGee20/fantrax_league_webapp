import pandas as pd
import numpy as np

def get_mock_rosters():
    """Generate fake fantasy rosters"""
    teams = ["Dylan’s Destroyers", "Pitcher Perfect", "Homerun Hunters", "Steal City"]
    players = ["Player " + str(i) for i in range(1, 41)]
    positions = ["C", "1B", "2B", "SS", "3B", "OF", "SP", "RP"]

    data = []
    np.random.seed(42)
    for i, player in enumerate(players):
        data.append({
            "team": np.random.choice(teams),
            "player": player,
            "position": np.random.choice(positions),
            "HR": np.random.randint(0, 25),
            "RBI": np.random.randint(10, 80),
            "AVG": round(np.random.uniform(0.200, 0.330), 3),
            "SB": np.random.randint(0, 20),
            "ERA": round(np.random.uniform(2.00, 5.00), 2),
            "K": np.random.randint(10, 150),
        })
    return pd.DataFrame(data)

def get_mock_free_agents():
    """Generate fake free agent pool"""
    players = ["FA " + str(i) for i in range(1, 16)]
    positions = ["OF", "SP", "RP", "1B", "2B"]

    data = []
    np.random.seed(7)
    for player in players:
        data.append({
            "player": player,
            "position": np.random.choice(positions),
            "HR": np.random.randint(0, 20),
            "RBI": np.random.randint(5, 70),
            "AVG": round(np.random.uniform(0.210, 0.300), 3),
            "SB": np.random.randint(0, 15),
            "ERA": round(np.random.uniform(2.50, 5.50), 2),
            "K": np.random.randint(5, 120),
        })
    return pd.DataFrame(data)