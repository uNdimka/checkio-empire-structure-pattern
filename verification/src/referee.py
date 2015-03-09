from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(f, data):
    if len(data) <= 2:
        return f(d[0], str(d[1]))
    else:
        return f(d[0], str(d[1]), d[2])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "check_structure"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
