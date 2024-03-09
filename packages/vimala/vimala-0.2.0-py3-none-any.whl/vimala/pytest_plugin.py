"""A pytest plugin for testing the vimala package.

This plugin can be enabled via the `pytest_plugins` conftest.py variable. This
allows us to use this plugin in external packages' tests instead of just for
this package's tests.

Examples:
    The following line should be found in the "tests/conftest.py" file:

    >>> pytest_plugins = ["vimala.pytest_plugin"]
"""

from typing import Generator
from unittest.mock import MagicMock, Mock, patch

import pytest


@pytest.fixture
def vim_proc_mock() -> Generator[Mock, None, None]:
    """Returns a mocked version of proctor.safe_popen().

    This mocked version will be used to run the 'vim' system command if
    `vimala.vim()` is called.
    """
    with patch("vimala._vim.proctor.safe_popen") as mock_safe_popen:
        mock_proc = MagicMock()
        mock_safe_popen.return_value = (
            mock_proc  # Simulate return value as needed
        )
        yield mock_safe_popen
