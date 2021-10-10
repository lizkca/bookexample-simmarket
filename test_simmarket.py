from click.testing import CliRunner
from simmarket import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output



