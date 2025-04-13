def calculate_statistics(values):
    count = len(values)
    if count == 0:
        return {"min": None, "max": None, "count": 0, "sum": None, "median": None}

    sorted_values = sorted(values)
    sum_val = sum(sorted_values)
    return {
        "min": sorted_values[0],
        "max": sorted_values[-1],
        "count": count,
        "sum": sum_val,
        "median": sorted_values[count // 2] if count % 2 else (sorted_values[count // 2 - 1] + sorted_values[
            count // 2]) / 2
    }
