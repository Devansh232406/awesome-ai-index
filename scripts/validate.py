#!/usr/bin/env python3
"""Validate all JSON datasets in the awesome-ai-index repo."""
import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

errors = []


def err(msg: str):
    errors.append(msg)
    print(f"  ERROR: {msg}", file=sys.stderr)


def load_json(path: Path) -> dict | None:
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        err(f"{path.name}: Invalid JSON - {e}")
        return None


def validate_date(val: str, ctx: str):
    try:
        datetime.strptime(val, "%Y-%m-%d")
    except ValueError:
        err(f"{ctx}: Invalid date '{val}', expected YYYY-MM-DD")


def validate_models(data: dict, vendor_ids: set):
    models = data.get("models", [])
    ids = set()
    required = ["id", "name", "vendor", "release_date", "license_spdx", "model_type"]
    for m in models:
        mid = m.get("id", "UNKNOWN")
        for field in required:
            if field not in m:
                err(f"Model '{mid}': missing required field '{field}'")
        if mid in ids:
            err(f"Model '{mid}': duplicate id")
        ids.add(mid)
        if "release_date" in m:
            validate_date(m["release_date"], f"Model '{mid}'")
        vendor = m.get("vendor")
        if vendor and vendor not in vendor_ids:
            err(f"Model '{mid}': vendor '{vendor}' not found in vendors.json")
    print(f"  Models: {len(models)} entries, {len(ids)} unique IDs")


def validate_vendors(data: dict) -> set:
    vendors = data.get("vendors", [])
    ids = set()
    required = ["id", "name", "hq_country", "website"]
    for v in vendors:
        vid = v.get("id", "UNKNOWN")
        for field in required:
            if field not in v:
                err(f"Vendor '{vid}': missing required field '{field}'")
        if vid in ids:
            err(f"Vendor '{vid}': duplicate id")
        ids.add(vid)
    print(f"  Vendors: {len(vendors)} entries, {len(ids)} unique IDs")
    return ids


def validate_benchmarks(data: dict):
    benchmarks = data.get("benchmarks", [])
    ids = set()
    for b in benchmarks:
        bid = b.get("id", "UNKNOWN")
        if bid in ids:
            err(f"Benchmark '{bid}': duplicate id")
        ids.add(bid)
    print(f"  Benchmarks: {len(benchmarks)} entries")


def validate_frameworks(data: dict):
    frameworks = data.get("frameworks", [])
    ids = set()
    for f in frameworks:
        fid = f.get("id", "UNKNOWN")
        if fid in ids:
            err(f"Framework '{fid}': duplicate id")
        ids.add(fid)
    print(f"  Frameworks: {len(frameworks)} entries")


def main():
    print("Validating awesome-ai-index datasets...\n")

    # Load vendors first for referential integrity
    vendor_ids = set()
    vp = DATA / "vendors" / "vendors.json"
    if vp.exists():
        print("[vendors.json]")
        vdata = load_json(vp)
        if vdata:
            vendor_ids = validate_vendors(vdata)

    # Models
    mp = DATA / "models" / "models.json"
    if mp.exists():
        print("[models.json]")
        mdata = load_json(mp)
        if mdata:
            validate_models(mdata, vendor_ids)

    # Benchmarks
    bp = DATA / "benchmarks" / "benchmarks.json"
    if bp.exists():
        print("[benchmarks.json]")
        bdata = load_json(bp)
        if bdata:
            validate_benchmarks(bdata)

    # Frameworks
    fp = DATA / "frameworks" / "frameworks.json"
    if fp.exists():
        print("[frameworks.json]")
        fdata = load_json(fp)
        if fdata:
            validate_frameworks(fdata)

    print(f"\nValidation complete: {len(errors)} error(s)")
    if errors:
        sys.exit(1)
    print("All checks passed!")


if __name__ == "__main__":
    main()
