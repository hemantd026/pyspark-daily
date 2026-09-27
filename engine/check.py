"""Verify a day's solution and update PROGRESS.md.

Usage: python engine/check.py day-001
"""
import datetime
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_day(arg: str) -> str:
    cdir = os.path.join(ROOT, "challenges")
    for d in sorted(os.listdir(cdir)):
        if d == arg or d.startswith(arg + "-") or d.startswith(arg):
            return os.path.join(cdir, d)
    raise SystemExit(f"No challenge matching {arg!r}")


def update_progress(slug: str, passed: bool):
    path = os.path.join(ROOT, "PROGRESS.md")
    with open(path) as f:
        text = f.read()
    today = datetime.date.today().isoformat()
    mark = "✅" if passed else "❌"
    date = today if passed else "-"
    new_row = f"| {slug} |"
    pattern = re.compile(rf"^\| {re.escape(slug)} \|.*\|$", re.M)
    if pattern.search(text):
        # replace status + date columns, keep the title column as-is
        def _repl(m):
            cols = [c.strip() for c in m.group(0).strip("|").split("|")]
            return f"| {cols[0]} | {cols[1]} | {mark} | {date} |"
        text = pattern.sub(_repl, text, count=1)
    else:
        text = text.rstrip("\n") + f"\n| {slug} | ? | {mark} | {date} |\n"
    # streak: count consecutive ✅ days from day-000
    streak = 0
    for line in text.splitlines():
        if re.match(r"^\| day-\d+", line) and "✅" in line:
            streak += 1
        elif re.match(r"^\| day-\d+", line):
            break
    text = re.sub(r"^Streak:.*$", f"Streak: {streak} day{'s' if streak != 1 else ''} 🔥",
                  text, flags=re.M)
    with open(path, "w") as f:
        f.write(text)


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "day-000"
    day_dir = find_day(arg)
    slug = os.path.basename(day_dir)
    print(f"--- verifying {slug} ---")
    r = subprocess.run(
        [sys.executable, "-m", "pytest", day_dir, "-q", "-p", "no:cacheprovider",
         "--import-mode=importlib"],
        cwd=ROOT,
    )
    if r.returncode == 0:
        update_progress(slug, True)
        print(f"\n✅ {slug} passed — PROGRESS.md updated. Commit it!")
        print(f'   git add challenges/{slug} PROGRESS.md && git commit -m "Solve {slug}"')
    else:
        print(f"\n❌ {slug} not passing yet — keep going.")


if __name__ == "__main__":
    main()
