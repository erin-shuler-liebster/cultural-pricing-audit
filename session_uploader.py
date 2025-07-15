import pandas as pd

def analyze_mouse_heatmap(file_path: str) -> dict:
    """
    Expects a CSV file with columns like: 'x', 'y', 'event_type', 'timestamp'
    """
    try:
        df = pd.read_csv(file_path)

        summary = {
            "Total Events": len(df),
            "Click Events": df[df['event_type'] == 'click'].shape[0],
            "Hover Events": df[df['event_type'] == 'hover'].shape[0],
            "Average X": round(df['x'].mean(), 2),
            "Average Y": round(df['y'].mean(), 2)
        }

        return summary
    except Exception as e:
        return {"error": str(e)}
