import pandas as pd
from get_volumes import core_function


def test_get_volumes():
    expected = pd.DataFrame({"Conc.":[10.0,10.1,12.2],'Volume':[70,69.3,57.38]})
    filename = 'Data.csv'
    result = core_function.get_volumes(filename)
    assert (result.head(3)["Conc."].round(1) == expected["Conc."].round(1)).all
    assert (result.head(3)["Volume"].round(0) == expected["Volume"].round(0)).all
