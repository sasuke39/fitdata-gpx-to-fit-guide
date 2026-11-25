# FitData — Online FIT File Generator, GPX to FIT Converter & GPX Pre-Check Toolkit

[![Live Tool](https://img.shields.io/badge/Live%20Tool-FitData%20Online-15803d?style=flat-square)](https://www.sasuke.top/fitdata/)
[![GPX to FIT](https://img.shields.io/badge/Guide-GPX%20to%20FIT-2563eb?style=flat-square)](https://www.sasuke.top/fitdata/en/gpx-to-fit.html)
[![FIT Validator](https://img.shields.io/badge/Tool-FIT%20Validator-0f766e?style=flat-square)](https://www.sasuke.top/fitdata/en/fit-file-validator.html)

**Online App:** [https://www.sasuke.top/fitdata/](https://www.sasuke.top/fitdata/)

A practical toolkit and guide for runners, cyclists, and fitness developers working with `.gpx` and binary `.fit` (Flexible and Interoperable Data Transfer) activity files.

Includes:
- A zero-dependency Python CLI (`scripts/check_gpx.py`) to inspect `.gpx` tracks for missing timestamps, GPS spikes, and total distance before converting to `.fit`.
- A valid 400m athletics track sample (`examples/sample-track.gpx`) for testing.
- Direct links to **FitData**, a browser-based tool to draw running routes, convert GPX to FIT with customizable pace/heart rate/multi-lap offsets, and validate `.fit` files online.

---

## Why GPX Uploads Often Fail (and Why FIT Works Better)

| Dimension | Binary FIT (`.fit`) | XML GPX (`.gpx`) |
|---|---|---|
| File Size (10 km run) | ~30–80 KB | ~300 KB – 2 MB |
| Timestamps & Pace | Native per-second records + Session summary | Often missing in planned routes |
| Heart Rate & Laps | Native `Record` / `Lap` / `Session` fields | Vendor-specific XML extensions |
| Platform Compatibility | Garmin Connect, Strava, COROS, Wahoo, Keep | Best for route navigation only |

---

## Quick Start: Pre-Check Your GPX Before Converting to FIT

Run the included Python 3 script (standard library only, no `pip install` needed):

```bash
python3 scripts/check_gpx.py examples/sample-track.gpx
```

What it checks:
- Trackpoint count and total Haversine distance (km)
- Whether `<time>` timestamps exist (missing timestamps cause most Strava/Garmin import rejections)
- Sudden GPS teleport/spike detection (> 150m jump between adjacent points)

Once your GPX looks clean, upload it to **[FitData GPX to FIT Online](https://www.sasuke.top/fitdata/en/gpx-to-fit.html)** to generate a standard binary `.fit` activity file with realistic pace, heart rate, and lap data, then verify it with the built-in **[FIT Validator](https://www.sasuke.top/fitdata/en/fit-file-validator.html)**.

---

## Documentation & Online Tools

### English Guides
- [FitData Online App (Draw Route / GPX to FIT / Validate FIT)](https://www.sasuke.top/fitdata/)
- [Online GPX to FIT Converter Guide](https://www.sasuke.top/fitdata/en/gpx-to-fit.html)
- [Online Running FIT File Generator (400m Track Multi-Lap & GPS Noise)](https://www.sasuke.top/fitdata/en/running-fit-generator.html)
- [Free Online FIT File Validator & Import Troubleshooting](https://www.sasuke.top/fitdata/en/fit-file-validator.html)

### 中文使用教程
- [FitData 在线 FIT 文件生成与 GPX 转 FIT 工具](https://www.sasuke.top/fitdata/)
- [如何在线绘制跑步轨迹并导出 FIT 文件（完整教程）](https://www.sasuke.top/fitdata/fit-file-guide.html)
- [GPX 转 FIT 在线转换教程（保留路线・自定义配速与心率）](https://www.sasuke.top/fitdata/gpx-to-fit.html)
- [操场多圈跑步轨迹与 GPS 噪声模拟设置指南](https://www.sasuke.top/fitdata/running-track-generator.html)
- [FIT 文件在线校验与 Keep / 佳明 / Strava 导入失败排查](https://www.sasuke.top/fitdata/fit-file-validator.html)
- [FIT 与 GPX 文件格式区别及主流运动平台导入说明](https://www.sasuke.top/fitdata/fit-vs-gpx.html)

---

## License

MIT License.
