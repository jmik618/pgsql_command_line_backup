import pytest

from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_drivers():
    """
    The parser will exit if the drivers name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "destination"])

def test_parser_with_known_drivers():
    """
    The parser will not exit if the driver name is known.
    """
    for driver in ['local', 's3']:

def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver
    with a destination
    """
    args = parser.parse_args([url, "--driver", "local","/some/path"])

    assert args.url = url
    assert args.driver = "local"
    assert args.destination = "/some/path"

