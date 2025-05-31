class Satellite:
    def __init__(self, initial_temp=25.0, ambient_temp=4.0, heat_capacity=1000.0):
        self.temp = initial_temp
        self.ambient_temp = ambient_temp
        self.heat_capacity = heat_capacity
        self.heat_input = 50.0
        self.cooling_power = 0.0
        self.reaction_coeff = 0.1

    def update(self, cooling_power, dt=1.0):
        self.cooling_power = cooling_power
        heat_loss = self.reaction_coeff * (self.temp - self.ambient_temp)
        net_heat = self.heat_input - heat_loss - self.cooling_power
        temp_change = net_heat / self.heat_capacity
        self.temp += temp_change
        return self.temp
