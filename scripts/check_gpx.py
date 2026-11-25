#!/usr/bin/env python3
"""Zero-dependency GPX pre-check utility before converting GPX to FIT.

Usage:
    python3 scripts/check_gpx.py path/to/route.gpx

Online GPX to FIT converter & FIT validator:
    https://www.sasuke.top/fitdata/
"""

import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371000.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def check_gpx(file_path: Path) -> int:
    if not file_path.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        return 1

    tree = ET.parse(file_path)
    root = tree.getroot()

    points = []
    timestamps = 0
    for elem in root.iter():
        tag = elem.tag.split("}")[-1]
        if tag in ("trkpt", "rtept"):
            lat = float(elem.attrib["lat"])
            lon = float(elem.attrib["lon"])
            has_time = any(child.tag.split("}")[-1] == "time" for child in elem)
            if has_time:
                timestamps += 1
            points.append((lat, lon))

    if len(points) < 2:
        print(f"Warning: only {len(points)} point(s) found in {file_path.name}.")
        return 2

    total_m = 0.0
    spikes = 0
    max_jump = 0.0
    for (lat1, lon1), (lat2, lon2) in zip(points, points[1:]):
        dist = haversine_m(lat1, lon1, lat2, lon2)
        total_m += dist
        if dist > max_jump:
            max_jump = dist
        if dist > 150.0:
            spikes += 1

    print(f"File:        {file_path.name}")
    print(f"Points:      {len(points)}")
    print(f"Distance:    {total_m / 1000:.3f} km ({total_m:.1f} m)")
    print(f"Timestamps:  {timestamps}/{len(points)}")
    print(f"Max jump:    {max_jump:.1f} m (spikes >150m: {spikes})")

    if timestamps == 0:
        print("\n[Note] No timestamps found. Direct upload to Garmin/Strava may fail.")
        print("       Convert to FIT with pace & heart rate at: https://www.sasuke.top/fitdata/en/gpx-to-fit.html")
    if spikes > 0:
        print(f"\n[Warn] Detected {spikes} large GPS jump(s) (>150m). Inspect route before exporting FIT.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/check_gpx.py <file.gpx>")
        sys.exit(1)
    sys.exit(check_gpx(Path(sys.argv[1])))
