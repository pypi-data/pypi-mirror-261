import pytest

from poaster.bulletin import components


@pytest.mark.parametrize(
    "text, max_word_count, want",
    [
        ("Hi this is my post", -1, "<p>…</p>"),
        ("Hi this is my post", 0, "<p>…</p>"),
        ("Hi this is my post", 1, "<p>Hi…</p>"),
        ("Hi this is my post", 2, "<p>Hi this…</p>"),
        ("Hi this is my post", 3, "<p>Hi this is…</p>"),
        ("Hi this is my post", 4, "<p>Hi this is my…</p>"),
        ("Hi this is my post", 5, "<p>Hi this is my post</p>"),
        ("Hi this is my post", 60, "<p>Hi this is my post</p>"),
    ],
)
def test_get_post_text_snippet(text: str, max_word_count: int, want: str):
    got = str(components.post_text_snippet(text, max_word_count=max_word_count))
    assert got == want
