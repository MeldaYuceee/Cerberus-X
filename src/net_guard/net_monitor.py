import os

class NetGuard:
    def score(self):
        try:
            out = os.popen("ping -n 1 8.8.8.8").read()
            if "Average" in out:
                delay = int(out.split("Average = ")[1].replace("ms", ""))
                return 1 if delay > 80 else 0
        except:
            return 2
        return 0