from unittest import mock
import pytest

@pytest.fixture
def website():
    post1 = mock.Mock()
    post1.title = "First Post"

    post2 = mock.Mock()
    post2.title = "Benchmarking Python Code with Pytest"

    site = mock.Mock()
    site.title = "My little blog"
    site.posts = [post1, post2]
    return site

def test_site_title(website):
    assert website.title == "My little blog"

def test_posts(website):
    assert len(website.posts) == 2
