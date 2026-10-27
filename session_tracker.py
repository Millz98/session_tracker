"""Gaming session tracker (work in progress).

Loads a JSON history of play sessions and prints a summary.
Each session: {"game": str, "minutes": int, "date": "YYYY-MM-DD"}
"""
import json
from collections import Counter


def load_history(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def summarize(history):
    total_minutes = sum(s["minutes"] for s in history)
    per_game = Counter()
    for s in history:
        per_game[s["game"]] += s["minutes"]
    return {
        "sessions": len(history),
        "total_minutes": total_minutes,
        "avg_minutes": round(total_minutes / len(history), 1),
        "longest_session": max(history, key=lambda s: s["minutes"]),
        "top_game": per_game.most_common(1)[0][0],
    }


def format_summary(summary):
    longest = summary["longest_session"]
    return (
        f"Sessions: {summary['sessions']}\n"
        f"Total time: {summary['total_minutes'] // 60}h {summary['total_minutes'] % 60}m\n"
        f"Average: {summary['avg_minutes']} min\n"
        f"Longest: {longest['game']} ({longest['minutes']} min on {longest['date']})\n"
        f"Most played: {summary['top_game']}"
    )


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "history_nonempty.json"
    print(format_summary(summarize(load_history(path))))
