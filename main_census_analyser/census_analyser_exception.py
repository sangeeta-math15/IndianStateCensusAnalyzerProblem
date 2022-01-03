class CensusAnalyserException(Exception) :
    def __init__(self, str):
        super().__init__(str)


class WrongFilePathError(CensusAnalyserException):
    pass


class WrongExtensionCSVFile(CensusAnalyserException):
    pass

