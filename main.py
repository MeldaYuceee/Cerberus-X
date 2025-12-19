import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from rf_guard.rf_detector import RFGuard
from net_guard.net_monitor import NetGuard
from tel_guard.telemetry_detector import TelemetryGuard
from fusion.fusion_core import CerberusFusion
import time

rf = RFGuard()
net = NetGuard()
tel = TelemetryGuard()
fusion = CerberusFusion()

while True:
    rf_s = rf.score()
    net_s = net.score()
    tel_s = tel.score()

    status, total = fusion.fuse(rf_s, net_s, tel_s)
    print(f"RF={rf_s:.2f} | NET={net_s} | TEL={tel_s} → {status} ({total:.2f})")

    time.sleep(1)
