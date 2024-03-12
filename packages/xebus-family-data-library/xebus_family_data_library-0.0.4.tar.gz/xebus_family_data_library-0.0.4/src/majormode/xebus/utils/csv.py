# Copyright (C) 2021 Majormode.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Majormode or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Majormode.
#
# MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY
# OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE SHALL NOT BE LIABLE FOR ANY
# LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
# OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

import csv
import os
from typing import Any

from majormode.perseus.utils import cast

# The default character used to separate each CSV field.
DEFAULT_CSV_DELIMITER_CHARACTER = ','

# The default character used to escape the delimiter character, in case
# quotes aren't used.
DEFAULT_CSV_ESCAPE_CHARACTER = None

# The default character used to surround fields that contain the
# delimiter character.
DEFAULT_CSV_QUOTE_CHARACTER = '"'


def read_csv_file(
        file_path_name: os.PathLike,
        delimiter_character: str = None,
        escape_character: str = None,
        quote_character: str = None
) -> list[list[Any]]:
    """
    Return the rows in a CSV file.


    :param file_path_name: The absolute path and name of a CSV file.

    :param delimiter_character: The character used to separate each CSV
        field.

    :param escape_character: The character used to escape the delimiter
        character, in case quotes aren't used.

    :param quote_character: The character used to surround fields that
        contain the delimiter character.


    :return: The list of rows in the CSV file.
    """
    with open(file_path_name, 'rt') as fd:
        csv_reader = csv.reader(
            fd,
            delimiter=delimiter_character or DEFAULT_CSV_DELIMITER_CHARACTER,
            escapechar=escape_character or DEFAULT_CSV_ESCAPE_CHARACTER,
            quotechar=quote_character or DEFAULT_CSV_QUOTE_CHARACTER
        )

        rows = [
            row
            for row in csv_reader
        ]

        return rows
