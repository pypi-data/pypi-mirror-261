# Copyright (C) 2024 Majormode.  All rights reserved.
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

from __future__ import annotations

import os
from typing import Any

from majormode.perseus.utils import module_utils, cast

from majormode.xebus.constant.family_sheet import DEFAULT_FIELD_NAME_IS_CHILD_REMOVED
from majormode.xebus.constant.family_sheet import DEFAULT_SECTION_NAME_CHILD
from majormode.xebus.constant.family_sheet import DEFAULT_SHEET_FIELD_NAMES_FAMILY_PROPERTY_NAMES_MAPPING
from majormode.xebus.constant.family_sheet import FamilyPropertyName
from majormode.xebus.model.sectioned_sheet import SectionedSheet
from majormode.xebus.utils.csv import read_csv_file


# Define the absolute path to the data of this Python library.
#
# The data of this Python library are located in a folder ``data`` located
# at the root path of this Python library.
#
# We have organized our Python modules in a source folder ``src`` located
# at the root path of this Python library, therefore the source depth is
# ``1`` (not ``0``).
LIBRARY_DATA_PATH = os.path.join(
    module_utils.get_project_root_path(__file__, __name__, 1),
    'data'
)


class FamilyDataSectionedSheet(SectionedSheet):
    """
    A sectioned sheet containing family data of an organization.
    """
    def __export_to_family_data_rows(self) -> list[dict[FamilyPropertyName, str]]:
        """
        Exports the rows from the sectioned sheet to a list of key/value rows
        with keys that have been normalized.

        The two-row header of sectioned sheet is not returned.

        :note: The value of fields is not converted to their respective
            appropriate Python type.


        :return: An array of where each entry corresponds to the information
            of a child and their guardianships.
        """
        rows = []
        for row_index in range(self.data_row_count):
            # Check whether the current row is empty, meaning that we have reached
            # the end of the family data list.
            if self.__is_row_empty(row_index):
                break

            # Check whether the child has been marked as no longer with the school
            # and should be removed from the list.
            is_child_removed = cast.string_to_boolean(
                self.get_field_value(
                    row_index,
                    DEFAULT_SECTION_NAME_CHILD,
                    DEFAULT_FIELD_NAME_IS_CHILD_REMOVED,
                    is_required=True
                )
            )

            if is_child_removed:
                continue

            # Convert the sheet fields names and their values.
            fields = {}
            for sheet_section_name, sheet_fields_names in DEFAULT_SHEET_FIELD_NAMES_FAMILY_PROPERTY_NAMES_MAPPING.items():
                for sheet_field_name, field_name in sheet_fields_names.items():
                    fields[field_name] = self.get_field_value(
                        row_index,
                        sheet_section_name,
                        sheet_field_name,
                        is_required=False
                    )

            rows.append(fields)

        return rows

    def __init__(self, rows: list[list[str]]):
        """
        Build a family sheet from rows read from a sectioned sheet (e.g.,
        Google Sheets, CSV file).


        :param rows: The rows of the family data sheet of an organization,
            including a two-row header declaring the sections and subsections
            of the family data sheet.
        """
        super().__init__(rows)
        self.__family_data_rows: list[dict[FamilyPropertyName, Any]] | None = None

    def __is_row_empty(
            self,
            row_index: int
    ) -> bool:
        """
        Indicate if the specified row is empty.


        :param row_index: The index of the row in the sheet.


        :return: ``True`` if the row is empty; ``False`` otherwise.
        """
        # Check whether some fields contain a value.
        #
        # :note: The commented code below is a shorter version, but it requires
        #     checking each field, which is slower.
        #
        # ```python
        # non_empty_fields = [
        #     field_name
        #     for sheet_section_name, sheet_fields_names in self.DEFAULT_SHEET_FIELD_NAMES_FAMILY_PROPERTY_NAMES_MAPPING.items()
        #     for sheet_field_name, field_name in sheet_fields_names.items()
        #     if field_name != FamilyPropertyName.child_use_transport
        #        and self.get_field_value(
        #            row_index,
        #            sheet_section_name,
        #            sheet_field_name,
        #            is_required=False
        #        ) is not None
        # ]
        #
        # return not non_empty_fields
        # ```
        for sheet_section_name, sheet_fields_names in DEFAULT_SHEET_FIELD_NAMES_FAMILY_PROPERTY_NAMES_MAPPING.items():
            for sheet_field_name, field_name in sheet_fields_names.items():
                # The field `FamilyPropertyName.child_use_transport` is never empty
                # because it contains either the value `TRUE` or `FALSE`.
                if field_name != FamilyPropertyName.child_use_transport:
                    sheet_field_value = self.get_field_value(
                        row_index,
                        sheet_section_name,
                        sheet_field_name,
                        is_required=False
                    )

                    # Check the value of this field is defined.
                    #
                    # :note: ``False`` value is treated as ``None`` (cf. ``DEFAULT_FIELD_NAME_IS_CHILD_REMOVED``)
                    if sheet_field_value:
                        return False

        return True

    @staticmethod
    def from_csv_file(
            file_path_name: os.PathLike,
            delimiter_character: str = None,
            escape_character: str = None,
            quote_character: str = None
    ):
        """
        Build a Family Sheet from a CSV file.


        :param file_path_name: The absolute path and name of a CSV file.

        :param delimiter_character: The character used to separate each CSV
            field.

        :param escape_character: The character used to escape the delimiter
            character, in case quotes aren't used.

        :param quote_character: The character used to surround fields that
            contain the delimiter character.


        :return:
        """
        rows = read_csv_file(
            file_path_name,
            delimiter_character=delimiter_character,
            escape_character=escape_character,
            quote_character=quote_character
        )

        return FamilyDataSectionedSheet(rows)

    @property
    def rows(self) -> list[dict[FamilyPropertyName, str]]:
        """
        Return the family data rows of this sheet.


        :note: The value of fields is not converted to their respective
            appropriate Python type.


        :return: A list of rows each corresponding to a dictionary whose key
            identifies the normalized name of the family data field.
        """
        if self.__family_data_rows is None:
            self.__family_data_rows = self.__export_to_family_data_rows()

        return self.__family_data_rows
