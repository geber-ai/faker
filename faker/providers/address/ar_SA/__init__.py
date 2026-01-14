from .. import Provider as AddressProvider


class Provider(AddressProvider):
    building_number_formats = ("####",)
    secondary_number_formats= ("####",)
    postcode_formats=("#####",)
    city_formats = ("{{city_name}}",)
    street_name_formats = ("{{street}}",)

    address_formats = (
        "{{building_number}}, {{street_name}}, {{secondary_number}}, {{district}}, {{postcode}}, {{city_name}}",
        #"{{building_number}}, {{street_name}}"
        #"{{secondary_number}}, {{district}}"
        #"{{postal_code}} "
        #"{{city}}",
    )
    