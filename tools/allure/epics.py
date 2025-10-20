from enum import Enum

class AllureEpic(str, Enum):
    LMS = "LMS service"
    STUDENT = "STUDENT service"
    ADMIN = "ADMIN service"
