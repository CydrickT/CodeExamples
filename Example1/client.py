from address import Address


class Client:
    def __init__(self, first_name: str, last_name: str, phone_number: str, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number

    def printLabel(self) -> str:
        return (self.first_name + " " + self.last_name + "\n" + 
                self.address.number + " " + self.address.street + "\n" +
                self.address.city + " " + self.address.province + " " + self.address.zip_code)