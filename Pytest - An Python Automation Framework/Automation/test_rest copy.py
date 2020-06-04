# coding=utf-8
"""DuckDuckGo Web Browsing feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_bdd.feature', 'Basic DuckDuckGo Search')
def test_basic_duckduckgo_search():
    """Basic DuckDuckGo Search."""


@given('the DuckDuckGo home page is displayed')
def the_duckduckgo_home_page_is_displayed():
    """the DuckDuckGo home page is displayed."""
    raise NotImplementedError


@when('the user searches for "panda"')
def the_user_searches_for_panda():
    """the user searches for "panda"."""
    raise NotImplementedError


@then('results are shown for "panda"')
def results_are_shown_for_panda():
    """results are shown for "panda"."""
    raise NotImplementedError