"""THE DATA CONTRACT - a written, checkable promise about what our files contain.

WHY THIS EXISTS (2026-07-25)
----------------------------
`universe-results-<date>.json` changed shape SEVEN TIMES IN SEVEN DAYS
(2026-07-18 through 07-24). Fields appeared, vanished and came back. About a
dozen scripts read that file and not one of them checked it was the shape it
expected - they just reached for a key and got `None` if it had moved.

That is exactly how `og_shadow.py` died. `all_names[].mode` was renamed to
`ce_mode`; the shadow grader looked for the old name, found nothing it
recognised, and exited quietly EVERY NIGHT FOR FOUR DAYS. No crash, no warning.
Nobody noticed until an audit.

The contract does not stop the shape changing - it should keep changing, adding
`gated_longs` was a genuine improvement. It makes changing it a DELIBERATE act:

  * the producer states which version it wrote, and must keep its promise
  * the consumer states which versions it understands, and refuses others LOUDLY

So a break becomes noisy on the night instead of invisible for four days.

Design rules, learned the hard way:
  * **Legacy files must keep working.** Every results file before 2026-07-25 has
    no version stamp. Those are accepted as LEGACY with a warning - breaking the
    ability to re-read history would be a worse bug than the one being fixed.
  * **Unknown FUTURE versions are fatal.** A v3 file handed to a v2 reader is the
    og_shadow scenario. That must raise, never shrug.
  * **A missing required field is fatal at WRITE time**, so a broken producer is
    caught before it can hand bad data to twelve consumers.
"""

KIND = "universe-results"
CURRENT_VERSION = 2

# What version 2 promises. Keep this list SHORT and load-bearing: these are the
# fields something downstream will break without, not everything that happens to
# be in the file. Optional-but-common fields are deliberately absent.
CONTRACTS = {
    KIND: {
        2: {
            "top_level": [
                "date",             # the session this describes
                "universe_size",    # names attempted
                "scanned",          # names read cleanly
                "fresh_count",      # fresh BUY signals before gating
                "hits",             # the fresh signals, each with a verdict
                "all_names",        # every scanned name (Sell Mode + shadow need this)
                "data_quality",     # blockers/warnings surfaced in the workbook
            ],
            # Per-row promises. Checked on a sample, not every row, so validation
            # stays cheap enough to run on every read.
            "rows": {
                "hits": ["sym", "verdict", "gates"],
                "all_names": ["sym", "ce_mode", "last"],
            },
        }
    }
}


class SchemaError(Exception):
    """The file is not the shape it promised, or is a version we cannot read."""


def stamp(obj, kind=KIND, version=CURRENT_VERSION):
    """Mark an object with the contract it claims to satisfy. Call before writing."""
    obj["schema_kind"] = kind
    obj["schema_version"] = version
    return obj


def _missing(obj, kind, version):
    spec = CONTRACTS[kind][version]
    missing = [f for f in spec["top_level"] if f not in obj]
    for field, required in spec.get("rows", {}).items():
        rows = obj.get(field)
        if not isinstance(rows, list) or not rows:
            continue                      # empty is legitimate (a day with no hits)
        row = rows[0]
        missing += [f"{field}[].{k}" for k in required if k not in row]
    return missing


def validate(obj, kind=KIND, version=CURRENT_VERSION, path=""):
    """Fail if `obj` does not keep the promise. Use at WRITE time."""
    if version not in CONTRACTS.get(kind, {}):
        raise SchemaError(f"no contract defined for {kind} v{version}")
    missing = _missing(obj, kind, version)
    if missing:
        where = f" in {path}" if path else ""
        raise SchemaError(
            f"{kind} v{version}{where} is missing required fields: {missing}. "
            f"The producer changed shape without updating the contract - either "
            f"restore the fields or bump CURRENT_VERSION in scripts/schema.py "
            f"and update every consumer that reads them.")
    return obj


def require(obj, understood=(2,), kind=KIND, path="", warn=print):
    """Check a file we are ABOUT TO READ. Returns the version in force.

    Legacy (unstamped, pre-2026-07-25) files are accepted with a warning so that
    historical runs stay readable. A stamped version we do not understand is
    FATAL - that is the og_shadow failure and it must never be silent again.
    """
    got = obj.get("schema_version")
    if got is None:
        warn(f"NOTE: {path or kind} has no schema stamp (pre-2026-07-25 file) - "
             f"reading as LEGACY. Field names may differ from the current contract.")
        return None
    if got not in understood:
        raise SchemaError(
            f"{path or kind} is schema v{got}, but this script only understands "
            f"v{sorted(understood)}. Refusing to read it rather than silently "
            f"producing nothing. Update this consumer for v{got}.")
    missing = _missing(obj, kind, got)
    if missing:
        raise SchemaError(
            f"{path or kind} claims v{got} but is missing {missing} - the file is "
            f"not what it says it is.")
    return got
