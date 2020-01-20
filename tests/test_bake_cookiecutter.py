import subprocess
import pytest  # type: ignore


@pytest.mark.parametrize(
    "cmd,extra_context",
    [
        (
            ["nox", "-s", "lint", "--", "--skip_manifest_check"],
            {"project_name": "helloworld"},
        ),
        (["nox", "-s", "tests"], {"project_name": "my-project"}),
        (["nox", "-s", "build"], {}),
    ],
)
def test_bake_project(cookies, cmd, extra_context):
    # cookies is a pytest plugin
    # https://pytest-cookies.readthedocs.io/en/latest/
    result = cookies.bake(extra_context=extra_context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()
    subprocess.run(cmd, cwd=result.project, check=True)
