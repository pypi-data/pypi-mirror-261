from _typeshed import Incomplete
from amsdal.cloud.services.actions.signup_action import FreeSignupAction as FreeSignupAction
from amsdal.configs.main import settings as settings

LICENCE_PATH: Incomplete
LICENCE_MESSAGE: Incomplete

def _input(msg: str) -> str: ...
def _print(msg: str) -> None: ...
def want_signup_input() -> str: ...
def licence_input() -> str: ...
def organization_name_input() -> str: ...
def email_input() -> str: ...

class SignupService:
    @classmethod
    def signup_prompt(cls) -> bool: ...
