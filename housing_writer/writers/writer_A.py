"""
This is a writer for the A type tables in the state XLS format.

May try this with XLSX, because it does update things and more
modern converters may work on it better.
"""

import openpyxl
from housing_writer.writers.base import TableWriter

A3_COLUMNS = {
    1: 'Single Family',
    2: '2 - 4 Units',
    3: '5 + Units',
    4: 'Second Unit',
    5: 'Mobile Homes',
    6: 'Total',
    7: 'Number of infill units',
}


class TableAWriter(TableWriter):
    """
    Writer for the three "A-type" tables.
    """

    def write_A3(self, excess_units_for_moderate,
                 excess_units_above_moderate):
        """
        Write the A3 table. This method has to take in JSON structures,
        which may be how we store things.

        :param excess_units_for_moderate: Dictionary of values for moderate
         housing.
        :param excess_units_above_moderate: Dictionary
        :return:
        """

        # Write headers, starting at column 11:
        self.current_col = 11
        for key, value in A3_COLUMNS.items():
            key_text = '{}.\n {}'.format(key, value)
            print(key_text)



