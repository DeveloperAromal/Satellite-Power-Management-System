class PidController:
    def __init__(self, setTemp=30.0, kp=10.0, ki=10.0, kd=0.05):
        self.setTemp = setTemp
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.0
        self.integral = 0.0

    def compute(self, currentTemp, dt=1.0):
        error = self.setTemp - currentTemp
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return max(0.0, min(output, 100.0))
