#!/usr/bin/env python3
"""Run an interactive RBQL query, saving each result to a separate file."""
from pathlib import Path
import subprocess
import sys
import tempfile

profile = Path.home() / "Library/Application Support/ZedPixel"
results = profile / "query-results"
results.mkdir(parents=True, exist_ok=True)
with tempfile.NamedTemporaryFile(prefix="query-", suffix=".csv", dir=results, delete=False) as result:
    output = result.name
command = [str(profile / "tools/rbql/bin/rbql"), *sys.argv[1:], "--output", output]
try:
    raise SystemExit(subprocess.call(command))
finally:
    path = Path(output)
    if path.exists() and path.stat().st_size == 0:
        path.unlink()
