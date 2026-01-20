from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):

    cellphone_formats = (
        "{{area_code}} {{cellphone_provider_code}} ### ####",
        "{{area_code}}{{cellphone_provider_code}}#######",
        "0{{cellphone_provider_code}} ### ####",
        "0{{cellphone_provider_code}}#######",
    )

    telephone_formats = (
        "{{area_code}} {{telephone_provider_code}} ### ####",
        "{{area_code}}{{telephone_provider_code}}#######",
        "0{{telephone_provider_code}} ### ####",
        "0{{telephone_provider_code}}#######",
    )

    toll_formats = (
        "9200 #####",
        "800### ####",
    )

    formats = cellphone_formats + telephone_formats + toll_formats

    def cellphone_provider_code(self) -> str:
        return self.random_element(
            [
                "50",
                "53",
                "54",
                "55",
                "56",
                "58",
                "59",
            ]
        )

    def telephone_provider_code(self) -> str:
        return self.random_element(
            [
                "11",
                "12",
                "13",
                "14",
                "16",
                "17",
            ]
        )

    def area_code(self) -> str:
        return self.random_element(
            [
                "00966",
                "+966",
            ]
        )

    def cellphone_number(self) -> str:
        pattern: str = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))

    def telephone_number(self) -> str:
        pattern: str = self.random_element(self.telephone_formats)
        return self.numerify(self.generator.parse(pattern))

    def toll_number(self) -> str:
        pattern: str = self.random_element(self.toll_formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number(self) -> str:
        pattern: str = self.random_element(self.formats)
        return self.numerify(self.generator.parse(pattern))
