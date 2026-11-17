import pytest
from sovereign_platform.governance_breaker import SlidingWindowBreaker, GovernanceBlockedError
def test_breaker_trips():
    breaker = SlidingWindowBreaker(window_size=10, error_threshold=0.15)
    for _ in range(8): breaker.record_result(True)
    breaker.record_result(False)
    breaker.record_result(False)
    with pytest.raises(GovernanceBlockedError):
        breaker.check_state()
