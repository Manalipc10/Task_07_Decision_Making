import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from clean_stats_text import parse_goals

# Load parsed goals
data = parse_goals("outputs/2024SUStats_raw.txt")
df = pd.DataFrame(data, columns=["Period", "Syracuse Goals", "Opponent Goals"])
df["Goal Diff"] = df["Syracuse Goals"] - df["Opponent Goals"]

print("Goals per period:\n", df)

# Bar chart
df.plot(x="Period", y=["Syracuse Goals", "Opponent Goals"], kind="bar")
plt.title("Goals by Period - Syracuse vs Opponents (2024 Season)")
plt.ylabel("Goals")
plt.savefig("outputs/goals_by_period.png")

# Bootstrapped CI for avg goals/game
np.random.seed(42)
goals_per_game = [15.23] * 22   # from stats PDF
samples = np.random.choice(goals_per_game, (1000, len(goals_per_game)), replace=True).mean(axis=1)
ci_low, ci_high = np.percentile(samples, [2.5, 97.5])
print(f"Bootstrap 95% CI for average goals: {ci_low:.2f}, {ci_high:.2f}")
