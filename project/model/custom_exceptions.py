# class ErrorMessages(Exception):

#     NO_VOYAGES_FOUND = "No voyages found!"
#     CREW_MEMBER_NOT_FOUND = "No crew members found!"
#     DESTINATION_NOT_FOUND = "Destination not found!"
#     NO_PILOTS_FOUND = "No pilots found!"
#     NO_FLIGHT_ATTENDANTS_FOUND = "No flight attendants found!"
#     CREW_MEMBER_ALREADY_IN_SYSTEM = "Crew member is already in the system!"
#     VOYAGE_ALREADY_IN_SYSTEM = "Voyage is already in the system!"
#     DESTINATION_ALREADY_IN_SYSTEM = "Destination is already in the system!"

#     def __init__(self):
#         pass

class CrewMemberNotFound(Exception):
    """Raised when crew member isn't in the data files"""
    pass

class NoCrewMembersRegistered(Exception):
    """Raised when crew member data files are empty"""
    pass

class CrewMemberAlreadyInSystem(Exception):
    """Raised when crew member is already in the files"""
    pass

class PilotsNotFound(Exception):
    """Raised when no pilots were found in the files"""
    pass

class FlightAttendantsNotFound(Exception):
    """Raised when no flight attendants were found in the files"""
    pass

class DestinationNotFound(Exception):
    """Raised when destination isn't found in the data files"""
    pass

class NoDestinationsRegistered(Exception):
    """Raised when the destinations data file is empty"""
    pass

class DestinationAlreadyInSystem(Exception):
    """Raised when destination is already in the system"""
    pass

class MissingEmergencyContactInfo(Exception):
    """Raised when emergency contact information isn't provided in a destination"""
    pass