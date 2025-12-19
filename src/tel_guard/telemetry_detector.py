import random

class TelemetryGuard:
    def score(self):
        # Gerçek MAVLink yoksa simüle et
        alt = random.uniform(-10, 150)

        if alt < -5 or alt > 120:
            return 2
        return 0