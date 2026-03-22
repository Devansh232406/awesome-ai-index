#!/usr/bin/env python3
"""
generate_events_csv.py - Generate events.csv from data sources.
Exports a flat CSV of all indexed AI models, papers, and tools.
"""
import csv
import json
import os
from pathlib import Path
from datetime import datetime, timezone

def load_json_safe(filepath):
    """Safely load a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: skipping {filepath}: {e}")
        return None

def collect_entries():
    """Collect all entries from data directories."""
    entries = []

    # Models
    models_path = Path("data/models/models.json")
    if models_path.exists():
        data = load_json_safe(models_path)
        if data and isinstance(data, list):
            for m in data:
                entries.append({
                    "type": "model",
                    "name": m.get("name", ""),
                    "organization": m.get("organization", ""),
                    "url": m.get("url", ""),
                    "license": m.get("license", ""),
                    "category": m.get("category", "model"),
                    "date_added": m.get("date_added", ""),
                    "description": m.get("description", "")
                })

    # Vendors
    vendors_dir = Path("data/vendors")
    if vendors_dir.exists():
        for f in sorted(vendors_dir.glob("**/*.json")):
            if f.name == "dataset-metadata.json":
                continue
            data = load_json_safe(f)
            if data and isinstance(data, dict):
                entries.append({
                    "type": "vendor",
                    "name": data.get("name", f.stem),
                    "organization": data.get("name", ""),
                    "url": data.get("website", ""),
                    "license": "",
                    "category": "vendor",
                    "date_added": data.get("date_added", ""),
                    "description": data.get("description", "")
                })

    # Papers
    papers_dir = Path("data/papers")
    if papers_dir.exists():
        for f in sorted(papers_dir.glob("*.json")):
            data = load_json_safe(f)
            if data and isinstance(data, list):
                for p in data:
                    entries.append({
                        "type": "paper",
                        "name": p.get("title", ""),
                        "organization": ", ".join(p.get("authors", [])),
                        "url": p.get("url", ""),
                        "license": "",
                        "category": p.get("category", "paper"),
                        "date_added": p.get("published", ""),
                        "description": p.get("summary", "")[:200]
                    })

    # Benchmarks
    benchmarks_dir = Path("data/benchmarks")
    if benchmarks_dir.exists():
        for f in sorted(benchmarks_dir.glob("*.json")):
            data = load_json_safe(f)
            if data and isinstance(data, list):
                for b in data:
                    entries.append({
                        "type": "benchmark",
                        "name": b.get("name", ""),
                        "organization": b.get("organization", ""),
                        "url": b.get("url", ""),
                        "license": "",
                        "category": "benchmark",
                        "date_added": b.get("date_added", ""),
                        "description": b.get("description", "")
                    })

    return entries

def main():
    entries = collect_entries()
    output_path = Path("events.csv")
    fieldnames = ["type", "name", "organization", "url", "license", "category", "date_added", "description"]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    print(f"Generated events.csv with {len(entries)} entries")

if __name__ == "__main__":
    main()
