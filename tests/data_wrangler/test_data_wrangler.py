import pytest
from argparse import ArgumentTypeError

from py_tricks_and_tips.data_wrangler.convert_extruder_data import valid_file


@pytest.mark.parametrize(
    "filename",
    [
        "file.csv",
        "file.CSV",
        "file.xls",
        "file.xlsx",
        pytest.param("file.not", marks=pytest.mark.raises(exception=ArgumentTypeError)),
    ],
)
def test_valid_file(mocker, filename):
    # mock out pathlib test so we don't need real files
    mocker.patch("pathlib.Path.is_file", return_value=True)
    assert filename == valid_file(filename)
