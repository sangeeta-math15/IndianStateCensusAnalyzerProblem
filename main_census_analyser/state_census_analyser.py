import csv
import logging
import re

from main_census_analyser.census_analyser_exception import WrongFilePathError, WrongExtensionCSVFile


class StateCensusAnalyser:
    state_census_list = []

    logging.basicConfig(filename='state_census_analyzer.log', level=logging.DEBUG,
                        format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')

    def extension_validator(self, csv_file_path):
        """
        :param csv_file_path: the path of the csv file given by user
        :if it is not a csv file, this will raise an error
        """
        FILE_PATTERN = '.*.csv$'
        pattern = re.compile(FILE_PATTERN)
        match = pattern.search(csv_file_path)
        try:
            if not match:
                logging.error(' Exception occurred due to wrong file extension')
                raise WrongExtensionCSVFile(' Please correct extension file')

        except WrongExtensionCSVFile as e:
            print(str(e))

    def load_census_data(self, file_name_path):
        """
        :param file_name_path: the state census data csv file path
        :return: count of entries inside it except heading
        """
        self.extension_validator(file_name_path)
        try:
            with open(file_name_path, 'r') as data:
                for line in csv.reader(data):
                    self.state_census_list.append(line)
                count = len(self.state_census_list)
                logging.debug('Number of entries {}'.format(count - 1))
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise WrongFilePathError('Please choose correct file path')
        except WrongFilePathError as e:
            logging.info(str(e))
        return count - 1


if __name__ == '__main__':
    state = StateCensusAnalyser()
    state.load_census_data('census_analyzer.csv')

