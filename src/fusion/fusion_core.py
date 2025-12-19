class CerberusFusion:
    def fuse(self, rf, net, tel):
        total = rf + net + tel

        if total <= 1:
            return "SAFE", total
        elif total <= 3:
            return "SUSPICIOUS", total
        else:
            return "CRITICAL", total
