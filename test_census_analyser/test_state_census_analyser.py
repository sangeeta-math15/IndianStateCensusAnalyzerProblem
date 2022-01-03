import pytest

from main_census_analyser.state_census_analyser import StateCensusAnalyser
from main_census_analyser.census_analyser_exception import WrongFilePathError, WrongExtensionCSVFile

INDIA_STATE_CENSUS_PATH = 'census_analyzer.csv'
WRONG_CSV_PATH = '\census_analyzer.csv'
WRONG_FILE_EXTENSION = 'census_analyzer.json'


@pytest.fixture
def instance_of_main_class():
    state_census = StateCensusAnalyser()
    return state_census


def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 29



