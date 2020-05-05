import pandas as pd
from get_volumes import core_functions


def test_get_volumes():
    expected = pd.DataFrame({"SampleConcentrions":[1,4,2],'volumes':[20,1,2]})
    filename = 'data/data.csv'
    input = pd.DataFrame.read_csv(filename).head(3)
    result = core_functions.get_volumes(input)
    assert result == expected
