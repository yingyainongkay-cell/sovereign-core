from collections import deque
class GovernanceBlockedError(Exception): pass
class SlidingWindowBreaker:
    def __init__(self, window_size: int = 10, error_threshold: float = 0.15):
        self.window_size = window_size
        self.error_threshold = error_threshold
        self.history = deque(maxlen=window_size)
    def record_result(self, success: bool):
        self.history.append(1 if success else 0)
    @property
    def current_error_rate(self) -> float:
        if not self.history: return 0.0
        return self.history.count(0) / len(self.history)
    def check_state(self):
        rate = self.current_error_rate
        if len(self.history) >= self.window_size and rate > self.error_threshold:
            raise GovernanceBlockedError(f'Blocked: Rate {rate:.2%} > {self.error_threshold:.2%}')
        return True