from __future__ import annotations

from pathlib import Path

import nox

PYTHON = ('3.7', '3.8', '3.9', '3.10')

LIB_ROOT = Path(__file__).parent
CORE_REQS = LIB_ROOT / 'requirements.txt'
DEV_REQS = LIB_ROOT / 'requirements-dev.txt'


def get_reqs(*paths: Path) -> list[str]:
    all_reqs: list[str] = []
    for path in paths:
        reqs = path.resolve().read_text(encoding='utf-8').replace('\r', '').split('\n')
        all_reqs.extend(reqs)
    return [req for req in all_reqs if req]


@nox.session(python=PYTHON, reuse_venv=True)
def tests(session: nox.Session) -> None:
    session.install(*get_reqs(CORE_REQS, DEV_REQS))
    session.run('make', 'test', external=True)
