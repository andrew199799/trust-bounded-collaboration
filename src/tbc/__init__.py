"""Trust-Bounded Collaboration: exact-action, non-executing evaluation."""
from ._core import action_digest, dumps_receipt, evaluate, load_request
from ._json import InputError

__all__ = ["load_request", "action_digest", "evaluate", "dumps_receipt", "InputError"]
__version__ = "1.0.0"
