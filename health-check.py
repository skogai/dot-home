#!/usr/bin/env python3
"""Generated local health probe for the dot systemd user service."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone


def check_service_status(service_name: str) -> dict[str, str]:
    """Return a JSON-serializable summary of a systemd user service."""
    try:
        result = subprocess.run(
            [
                "systemctl",
                "--user",
                "show",
                service_name,
                "--property=LoadState",
                "--property=ActiveState",
            ],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {
            "service": service_name,
            "load_state": "unknown",
            "active_state": "unknown",
            "status": "error",
            "error": str(exc),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    properties = dict(
        line.split("=", 1) for line in result.stdout.splitlines() if "=" in line
    )
    load_state = properties.get("LoadState", "unknown")
    active_state = properties.get("ActiveState", "unknown")
    status = (
        "healthy"
        if result.returncode == 0 and active_state == "active"
        else "unhealthy"
    )
    return {
        "service": service_name,
        "load_state": load_state,
        "active_state": active_state,
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main() -> int:
    health = check_service_status("dot.service")
    print(json.dumps(health, indent=2))
    return 0 if health["status"] == "healthy" else 1


if __name__ == "__main__":
    raise SystemExit(main())
