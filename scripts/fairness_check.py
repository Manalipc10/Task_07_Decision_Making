def check_representation(df):
    report = []
    if df["Syracuse Goals"].sum() < df["Opponent Goals"].sum():
        report.append("Overall scoring disparity detected.")
    if df["Goal Diff"].min() < 0:
        report.append("At least one period has negative differential.")
    return report

if __name__ == "__main__":
    import pandas as pd
    from clean_stats_text import parse_goals

    data = parse_goals("outputs/2024SUStats_raw.txt")
    df = pd.DataFrame(data, columns=["Period", "Syracuse Goals", "Opponent Goals"])
    df["Goal Diff"] = df["Syracuse Goals"] - df["Opponent Goals"]

    findings = check_representation(df)
    with open("outputs/fairness_report.txt", "w") as f:
        for line in findings:
            f.write(line + "\n")

    print("[INFO] Fairness report saved to outputs/fairness_report.txt")
