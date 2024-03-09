"""The vimala package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from __future__ import annotations

from typing import Iterable

from eris import ErisError, Result, return_lazy_result
import proctor
from typist import PathLike


@return_lazy_result
def vim(
    *args: PathLike,
    lineno: int = None,
    commands: Iterable[str] = (),
    vim_exe: PathLike = "vim",
) -> Result[proctor.Process, ErisError]:
    """Execute `vim`."""
    extra_args: list[str] = []
    if lineno is not None:
        extra_args.append(f"+{lineno}")

    for cmd in commands:
        extra_args.extend(["-c", cmd])

    cmd_args = [str(x) for x in [vim_exe, *args, *extra_args]]
    proc = proctor.safe_popen(cmd_args, stdout=None, stderr=None, timeout=None)
    return proc
