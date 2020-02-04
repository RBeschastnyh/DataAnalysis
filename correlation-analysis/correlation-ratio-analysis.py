import numpy
import pandas
from constants import CORRELATION_RATIO_FILE_NAME
from constants import TABLE_COLUMNS_FOR_TWO_INPUT_VARIABLES


inputData = pandas.read_csv(CORRELATION_RATIO_FILE_NAME, header=None)
inputData.columns = TABLE_COLUMNS_FOR_TWO_INPUT_VARIABLES

x_values = inputData['x']
y_values = inputData['y']

print(x_values)
