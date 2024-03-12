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

from __future__ import annotations

import csv
from os import PathLike
from typing import Any

import unidecode
from majormode.perseus.model.country import Country
from majormode.perseus.model.locale import Locale

from majormode.xebus.utils.csv import DEFAULT_CSV_DELIMITER_CHARACTER
from majormode.xebus.utils.csv import DEFAULT_CSV_ESCAPE_CHARACTER
from majormode.xebus.utils.csv import DEFAULT_CSV_QUOTE_CHARACTER


# def convert_sectioned_sheet(
#         sectioned_sheet: SectionedSheet
# ) -> list[dict[FamilyPropertyName, Any]]:
#     """
#     Convert the rows containing family data into an array with normalized
#     fields and values.
#
#
#     :param sectioned_sheet: A sectioned sheet containing family data.
#
#
#     :return: An array of where each entry corresponds to the information
#         of a child and their guardianships.
#     """
#     rows = []
#     for row_index in range(sectioned_sheet.data_row_count):
#         # Check whether the current row is empty, meaning that we have reached
#         # the end of the family data list.
#         if self.__is_row_empty(sectioned_sheet, row_index):
#             break
#
#         # Check whether the child has been marked as no longer with the school
#         # and should be removed from the list.
#         is_child_removed = self._convert_field_boolean_value(
#             sectioned_sheet.get_field_value(
#                 row_index,
#                 DEFAULT_SECTION_NAME_CHILD,
#                 DEFAULT_FIELD_NAME_IS_CHILD_REMOVED,
#                 is_required=True
#             )
#         )
#
#         if is_child_removed:
#             continue
#
#         # Convert the sheet fields names and their values.
#         fields = {}
#         for sheet_section_name, sheet_fields_names in DEFAULT_SHEET_FIELD_NAMES_FAMILY_PROPERTY_NAMES_MAPPING.items():
#             for sheet_field_name, field_name in sheet_fields_names.items():
#                 sheet_field_value = sectioned_sheet.get_field_value(
#                     row_index,
#                     sheet_section_name,
#                     sheet_field_name,
#                     is_required=False
#                 )
#
#                 field_value_converter_function = self.FIELD_VALUE_CONVERTERS.get(field_name)
#                 field_value = sheet_field_value if field_value_converter_function is None \
#                     else field_value_converter_function(self, sheet_field_value)
#
#                 fields[field_name] = field_value
#
#         rows.append(fields)
#
#     return rows
#
# def __is_row_empty(
#         sectioned_sheet: SectionedSheet,
#         row_index: int
# ) -> bool:
#     """
#     Indicate if the specified row is empty.
#
#
#     :param sectioned_sheet: The sheet containing the row.
#
#     :param row_index: The index of the row in the sheet.
#
#
#     :return: ``True`` if the row is empty; ``False`` otherwise.
#     """
#     # Check whether some fields contain a value.
#     #
#     # :note: The commented code below is a shorter version, but it requires
#     #     checking each field, which is slower.
#     #
#     # ```python
#     # non_empty_fields = [
#     #     field_name
#     #     for sheet_section_name, sheet_fields_names in self.GOOGLE_SHEET_PROPERTIES_MAPPING.items()
#     #     for sheet_field_name, field_name in sheet_fields_names.items()
#     #     if field_name != FamilyPropertyName.child_use_transport
#     #        and sectioned_sheet.get_field_value(
#     #            row_index,
#     #            sheet_section_name,
#     #            sheet_field_name,
#     #            is_required=False
#     #        ) is not None
#     # ]
#     #
#     # return not non_empty_fields
#     # ```
#     for sheet_section_name, sheet_fields_names in self.GOOGLE_SHEET_PROPERTIES_MAPPING.items():
#         for sheet_field_name, field_name in sheet_fields_names.items():
#             # The field `FamilyPropertyName.child_use_transport` is never empty
#             # because it contains either the value `TRUE` or `FALSE`.
#             if field_name != FamilyPropertyName.child_use_transport:
#                 sheet_field_value = sectioned_sheet.get_field_value(
#                     row_index,
#                     sheet_section_name,
#                     sheet_field_name,
#                     is_required=False
#                 )
#
#                 if sheet_field_value:
#                     return False
#
#     return True


def load_languages_names_iso_codes_mapping_from_csv_file(file_path_name: PathLike) -> dict[str, Locale]:
    """
    Return the mapping between the names of languages and their respective
    ISO 639-3:2007 codes as identified in the specified file.


    :param file_path_name: The absolute path and name of a CSV file
        containing a list of names of languages and their corresponding
        ISO 639-3:2007 codes (the values).


    :return: A dictionary representing a mapping between the names of
        languages (the keys), localized in a particular language, and
        their corresponding ISO 639-3:2007 codes (the values).
    """
    names_values_mapping = load_codes_names_mapping_from_csv_file(file_path_name)

    languages_names_iso_codes_mapping = {
        name: Locale(iso_639_3_code)
        for name, iso_639_3_code in names_values_mapping.items()
    }

    return languages_names_iso_codes_mapping


def load_codes_names_mapping_from_csv_file(
        file_path_name: PathLike,
        delimiter_character: str = None,
        escape_character: str = None,
        quote_character: str = None
) -> dict[str, str]:
    """
    Return a dictionary of codes and their corresponding human-readable
    names.


    :param file_path_name: The absolute path and name of the file
        containing codes and their corresponding human-readable names.

    :param delimiter_character: The character used to separate each CSV
        field.

    :param escape_character: The character used to escape the delimiter
        character, in case quotes aren't used.

    :param quote_character: The character used to surround fields that
        contain the delimiter character.


    :return: A dictionary where the keys correspond to a human-readable
        names and the values correspond to their corresponding codes.
    """
    with open(file_path_name, 'rt') as fd:
        csv_reader = csv.reader(
            fd,
            delimiter=delimiter_character or DEFAULT_CSV_DELIMITER_CHARACTER,
            escapechar=escape_character or DEFAULT_CSV_ESCAPE_CHARACTER,
            quotechar=quote_character or DEFAULT_CSV_QUOTE_CHARACTER
        )

        names_values_mapping: dict[str, str] = {
            language_name: iso_code
            for iso_code, language_name in csv_reader
        }

    return names_values_mapping


def load_nationalities_names_iso_codes_mapping_from_csv_file(file_path_name: PathLike) -> dict[str, Country]:
    """
    Return the mapping between the names of languages and their respective
    ISO 639-3:2007 codes as identified in the specified file.


    :param file_path_name: The absolute path and name of a CSV file
        containing a list of ISO 3166-1 alpha-2 codes and the names of the
        corresponding languages.


    :return: A dictionary representing a mapping between the names of
        languages (the keys), localized in a particular language, and
        their corresponding ISO 3166-1 alpha-2 codes (the values).
    """
    names_values_mapping = load_codes_names_mapping_from_csv_file(file_path_name)

    nationalities_names_iso_codes_mapping = {
        nationality_name: Country(iso_3166_alpha2_code)
        for nationality_name, iso_3166_alpha2_code in names_values_mapping.items()
    }

    return normalize_names_codes_mapping(nationalities_names_iso_codes_mapping)


def normalize_names_codes_mapping(names_codes_mapping: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize the keys of a names codes mapping.

    Key normalization makes it possible to support minor differences
    (basically lowercase or uppercase letters, and accents) of names
    when searching for the corresponding code.


    :param names_codes_mapping: A mapping between names (the keys) and
        their respective codes (the values), such as, for example,
        language names and their ISO codes.


    :return: The names codes mapping where the names have been
        transliterated to ASCII lower cased strings.
    """
    normalized_names_codes_mapping = {
        normalize_key(key): value
        for key, value in names_codes_mapping.items()
    }

    return normalized_names_codes_mapping


def normalize_key(s: str) -> str:
    """
    Normalize the keys of a names codes mapping.


    :param s: A string to normalize.


    :return: The transliterated to ASCII lower cased string of the key
    """
    normalized_string = unidecode.unidecode(s.lower())
    return normalized_string
