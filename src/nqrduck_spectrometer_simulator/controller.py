from nqrduck_spectrometer.base_spectrometer_controller import BaseSpectrometerController

class SimulatorController(BaseSpectrometerController):
    def __init__(self, module):
        super().__init__(module)
