"""Auto-generated file, do not edit by hand. MD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MD = PhoneMetadata(id='MD', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:[79]|6(?:000|1(?:11|23))|8\\d)|4\\d{3}|5[0-3]\\d|6[0-389]\\d|8\\d{2}|9(?:0[04-9]|[1-4]\\d))', possible_number_pattern='\\d{3,6}', example_number='116000'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
