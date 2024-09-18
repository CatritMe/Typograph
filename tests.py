import pytest

from typograph import typo

articles = {
    "only dash": "<h1>30-40% рознице - сказал</h1>",
    "one quote": "<a>”Стоимость рознице”, - сказал Шестаков.</a>",
    "two quotes": "<div>”Стоимость рознице”, - сказал Шестаков. Шестаков сказал: ”Стоимость рознице”.</div>",
    "nested quotes": "<p>”Стоимость ”Стоимость рознице” рознице”, - сказал Шестаков.</p>",
    "nested two quotes": "<li>”Стоимость ”Стоимость”, ”рознице” рознице”, - сказал Шестаков.</li>",
}


def test_typo_only_dash():
    assert typo(articles["only dash"]) == "<h1>30-40% рознице — сказал</h1>"


def test_typo_one_quote():
    assert (
        typo(articles["one quote"]) == "<a>«Стоимость рознице», — сказал Шестаков.</a>"
    )


def test_typo_two_quotes():
    assert (
        typo(articles["two quotes"])
        == "<div>«Стоимость рознице», — сказал Шестаков. Шестаков сказал: «Стоимость рознице».</div>"
    )


def test_typo_nested_quotes():
    assert (
        typo(articles["nested quotes"])
        == "<p>«Стоимость „Стоимость рознице“ рознице», — сказал Шестаков.</p>"
    )


def test_typo_nested_two_quotes():
    assert (
        typo(articles["nested two quotes"])
        == "<li>«Стоимость „Стоимость“, „рознице“ рознице», — сказал Шестаков.</li>"
    )
