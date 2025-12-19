import numpy as np

class RFGuard:
    def __init__(self):
        self.baseline = None

    def get_fft_value(self):
        # Gerçek SDR yokken basit rastgele veri üret
        data = np.random.rand(256)
        return data

    def score(self):
        spec = self.get_fft_value()
        if self.baseline is None:
            self.baseline = spec
            return 0

        diff = np.mean(abs(spec - self.baseline))
        return diff
