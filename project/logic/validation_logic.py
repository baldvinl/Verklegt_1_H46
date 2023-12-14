class Validation_Logic:
    def __init__(self) -> None:
        pass

    def DestinationAlreadyRegistered(self, new_destination, all_destinations):
        """Raises error if new destinations airport is already registered"""
        if all_destinations:
            for destination in all_destinations:
                if destination.airport == new_destination.airport:
                    return True
        return False
