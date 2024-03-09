"""Test the pytest plugin provided by vimala."""

from __future__ import annotations

from unittest.mock import Mock

import vimala


def test_vim_proc_mock(vim_proc_mock: Mock) -> None:
    """Tests that the {vim_proc_mock} fixture WAI."""
    vimala.vim("foo", "bar").unwrap()
    vim_proc_mock.assert_called_once_with(
        ["vim", "foo", "bar"], stdout=None, stderr=None, timeout=None
    )
