from nqrduck_spectrometer.base_spectrometer_model import BaseSpectrometerModel

class SimulatorModel(BaseSpectrometerModel):
    def __init__(self, module):
        super().__init__(module)