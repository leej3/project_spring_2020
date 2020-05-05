import pandas as pd
from get_volumes import core_function


def test_get_volumes():
    expected = pd.DataFrame({"Conc.":[10,10.1,12,2],'volumes':[70,69.3,57.38]})
    filename = 'data/data.csv'
    input = pd.DataFrame.read_csv(filename).head(3)
    result = core_functions.get_volumes(input)
    assert result == expected
