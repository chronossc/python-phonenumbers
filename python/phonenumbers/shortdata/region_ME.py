"""Auto-generated file, do not edit by hand. ME metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ME = PhoneMetadata(id='ME', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:16\\d{3}|2(?:[015-9]|\\d{2})|[0135]\\d{2}|4\\d{2,3}|9\\d{3})', possible_number_pattern='\\d{3,6}', example_number='1011'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
