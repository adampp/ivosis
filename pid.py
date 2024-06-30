import numpy as np

class PID():
    def __init__(self, kp, ki, kd, integral_saturation=None, force_limits=None):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_saturation = integral_saturation
        if force_limits:
            self.force_lb = force_limits[0]
            self.force_ub = force_limits[1]
        else:
            self.force_lb = None
            self.force_ub = None

        self.integral = 0
        self.prior_err = 0
    
    def update(self, value, target):
        err = value - target

        p = err * self.kp
        d = (err - self.prior_err) * self.kd

        self.integral += err
        if self.integral_saturation:
            if self.integral > self.integral_saturation:
                self.integral = self.integral_saturation
            elif self.integral < -1*self.integral_saturation:
                self.integral = -1*self.integral_saturation
        
        i = self.integral * self.ki
        f = p + i + d
        
        if self.force_lb:
            if f > self.force_ub:
                f = self.force_ub
            elif f < self.force_lb:
                f = self.force_lb
        print(f"{value:0.5f},\t {target:0.3f}\t:: {p:0.3f},\t{i:0.3f},\t{d:0.3f}\t:: {self.integral:0.5f}")
        return f