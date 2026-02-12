import json
from pathlib import Path
from analytics import spots_last_minutes, spots_by_band

FRONTEND_DATA = Path(__file__).parents[1] / "frontend" / "data"


def export_metrics():
    FRONTEND_DATA.mkdir(parents=True, exist_ok=True)

    metrics = {
        "active_last_15_min": spots_last_minutes(15),
        "spots_by_band": spots_by_band()
    }

    with open(FRONTEND_DATA / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)


def run():
    export_metrics()
