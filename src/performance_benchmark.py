"""Performance pass: frame rendering pipeline and asset encoding latency.

Profiles video timeline assembly overhead and asset encoding pipeline latency,
adding benchmark tests for processing bottlenecks.
"""
from __future__ import annotations

import argparse
import time
from contextlib import contextmanager
from typing import Any
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Add project root to path if needed for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import src.composition_runtime as cr

@contextmanager
def profile_latency(name: str):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"[{name}] latency: {end - start:.4f}s")

def get_sample_composition() -> dict[str, Any]:
    """Provide a complex composition schema to test timeline assembly overhead."""
    return {
        "schema": cr.SCHEMA, "id": "benchmark_comp", "width": 1080, "height": 1920,
        "fps": 30, "duration_frames": 3600, # 2 minutes
        "variables": {"title": "Performance Pass Benchmark"},
        "tracks": [
            {"id": "bg", "component": "solid", "start_frame": 0, "duration_frames": 3600,
             "z": 0, "props": {"color": "#111"}},
            {"id": "layer1", "component": "solid", "start_frame": 100, "duration_frames": 1000,
             "z": 1, "props": {"color": "#222"}},
            {"id": "text_overlay", "component": "text", "start_frame": 300, "duration_frames": 500,
             "z": 10, "props": {"text": "{{title}}"}},
            # add more layers to simulate complexity
            *[{"id": f"layer_{i}", "component": "solid", "start_frame": i * 10, "duration_frames": 100,
               "z": i, "props": {"color": "#333"}} for i in range(2, 50)]
        ],
    }

def benchmark_timeline_assembly():
    print("--- Profiling Timeline Assembly Overhead ---")
    spec = get_sample_composition()

    with profile_latency("Expand Composition"):
        expanded = cr.expand_composition(spec)

    with profile_latency("Validate Composition"):
        cr.validate(expanded)

    with profile_latency("Compile Render Graph"):
        cr.compile_graph(expanded)

    with profile_latency("Total Timeline Assembly"):
        e = cr.expand_composition(spec)
        cr.validate(e)
        cr.compile_graph(e)

def benchmark_asset_encoding():
    print("\n--- Profiling Asset Encoding Pipeline Latency ---")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print("[Asset Encoding] skipped: ffmpeg not available")
        return

    with tempfile.TemporaryDirectory() as td:
        out_path = Path(td) / "test_out.mp4"
        # use a 1 second test render
        cmd = [ffmpeg, "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=black:s=1280x720:r=30:d=1", "-c:v", "libx264", str(out_path)]

        with profile_latency("Asset Encoding Pipeline (FFMpeg lavfi 1s)"):
            subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(description="Performance benchmarks for rendering and encoding.")
    args = parser.parse_args()

    benchmark_timeline_assembly()
    benchmark_asset_encoding()

    print("\nBenchmarks completed successfully.")

if __name__ == "__main__":
    main()
