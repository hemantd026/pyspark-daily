"""Shared test harness: loads a challenge's data/solution modules by file path.

Each challenge directory contains modules with identical names (data.py,
solution.py), so they are loaded with importlib under a unique module name
derived from the challenge folder — no cross-challenge import collisions.
"""
import importlib.util
import os


def _load_module(day_dir: str, name: str):
    slug = os.path.basename(day_dir).replace("-", "_")
    path = os.path.join(day_dir, f"{name}.py")
    spec = importlib.util.spec_from_file_location(f"{slug}_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_day(day_dir: str):
    """Return (data_module, solution_module) for a challenge directory."""
    return _load_module(day_dir, "data"), _load_module(day_dir, "solution")
