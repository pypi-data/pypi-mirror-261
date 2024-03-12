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

import datetime

from majormode.perseus.model.contact import Contact
from majormode.perseus.model.country import Country
from majormode.perseus.model.enum import Enum
from majormode.perseus.model.locale import Locale


# List of the property names that identify the information of children
# and their guardians, and their respective Python type.
FamilyPropertyName = Enum(
    'child_sis_id',
    'child_first_name',
    'child_last_name',
    'child_full_name',
    'child_languages',
    'child_nationalities',
    'child_date_of_birth',
    'child_grade_level',
    'child_class_name',
    'child_use_transport',
    'primary_guardian_sis_id',
    'primary_guardian_first_name',
    'primary_guardian_last_name',
    'primary_guardian_full_name',
    'primary_guardian_languages',
    'primary_guardian_nationalities',
    'primary_guardian_email_address',
    'primary_guardian_phone_number',
    'primary_guardian_home_address',
    'secondary_guardian_sis_id',
    'secondary_guardian_first_name',
    'secondary_guardian_last_name',
    'secondary_guardian_full_name',
    'secondary_guardian_languages',
    'secondary_guardian_nationalities',
    'secondary_guardian_email_address',
    'secondary_guardian_phone_number',
    'secondary_guardian_home_address',
)

FAMILY_PROPERTY_TYPES = {
    FamilyPropertyName.child_sis_id: str,
    FamilyPropertyName.child_first_name: str,
    FamilyPropertyName.child_last_name: str,
    FamilyPropertyName.child_full_name: str,
    FamilyPropertyName.child_languages: list[Locale],
    FamilyPropertyName.child_nationalities: list[Country],
    FamilyPropertyName.child_date_of_birth: datetime.datetime,
    FamilyPropertyName.child_grade_level: int,
    FamilyPropertyName.child_class_name: str,
    FamilyPropertyName.child_use_transport: bool,
    FamilyPropertyName.primary_guardian_sis_id: str,
    FamilyPropertyName.primary_guardian_first_name: str,
    FamilyPropertyName.primary_guardian_last_name: str,
    FamilyPropertyName.primary_guardian_full_name: str,
    FamilyPropertyName.primary_guardian_languages: list[Locale],
    FamilyPropertyName.primary_guardian_nationalities: list[Country],
    FamilyPropertyName.primary_guardian_email_address: Contact,
    FamilyPropertyName.primary_guardian_phone_number: Contact,
    FamilyPropertyName.primary_guardian_home_address: str,
    FamilyPropertyName.secondary_guardian_sis_id: str,
    FamilyPropertyName.secondary_guardian_first_name: str,
    FamilyPropertyName.secondary_guardian_last_name: str,
    FamilyPropertyName.secondary_guardian_full_name: str,
    FamilyPropertyName.secondary_guardian_languages: list[Locale],
    FamilyPropertyName.secondary_guardian_nationalities: list[Country],
    FamilyPropertyName.secondary_guardian_email_address: Contact,
    FamilyPropertyName.secondary_guardian_phone_number: Contact,
    FamilyPropertyName.secondary_guardian_home_address: str,
}

# Declare the list of property names for a child.
CHILD_PROPERTY_NAMES = [
    FamilyPropertyName.child_sis_id,
    FamilyPropertyName.child_first_name,
    FamilyPropertyName.child_last_name,
    FamilyPropertyName.child_full_name,
    FamilyPropertyName.child_languages,
    FamilyPropertyName.child_nationalities,
    FamilyPropertyName.child_date_of_birth,
    FamilyPropertyName.child_grade_level,
    FamilyPropertyName.child_class_name,
    FamilyPropertyName.child_use_transport,
]

# Declare the list of the property names for a primary guardian.
PRIMARY_GUARDIAN_PROPERTY_NAMES = [
    FamilyPropertyName.primary_guardian_sis_id,
    FamilyPropertyName.primary_guardian_first_name,
    FamilyPropertyName.primary_guardian_last_name,
    FamilyPropertyName.primary_guardian_full_name,
    FamilyPropertyName.primary_guardian_languages,
    FamilyPropertyName.primary_guardian_nationalities,
    FamilyPropertyName.primary_guardian_email_address,
    FamilyPropertyName.primary_guardian_phone_number,
    FamilyPropertyName.primary_guardian_home_address,
]

# Declare the list of the property names for a secondary guardian.
#
# :note: The secondary guardian's property names MUST be declared in
#     exactly the same order as those of the primary guardian.
SECONDARY_GUARDIAN_PROPERTY_NAMES = [
    FamilyPropertyName.secondary_guardian_sis_id,
    FamilyPropertyName.secondary_guardian_first_name,
    FamilyPropertyName.secondary_guardian_last_name,
    FamilyPropertyName.secondary_guardian_full_name,
    FamilyPropertyName.secondary_guardian_languages,
    FamilyPropertyName.secondary_guardian_nationalities,
    FamilyPropertyName.secondary_guardian_email_address,
    FamilyPropertyName.secondary_guardian_phone_number,
    FamilyPropertyName.secondary_guardian_home_address,
]