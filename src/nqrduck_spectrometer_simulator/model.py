import logging
from nqrduck_spectrometer.base_spectrometer_model import BaseSpectrometerModel
from nqrduck_spectrometer.pulseparameters import TXPulse, RXReadout

logger = logging.getLogger(__name__)


class SimulatorModel(BaseSpectrometerModel):
    # Simulation settings
    NUMBER_POINTS = "N. simulation points"
    NUMBER_ISOCHROMATS = "N. of isochromats"
    INITIAL_MAGNETIZATION = "Initial magnetization"
    GRADIENT = "Gradient (mT/m))"
    NOISE = "Noise (uV)"

    # Hardware settings
    LENGTH_COIL = "Length coil (m)"
    DIAMETER_COIL = "Diameter coil (m)"
    NUMBER_TURNS = "Number turns"
    Q_FACTOR_TRANSMITT = "Q factor Transmitt"
    Q_FACTOR_RECEIVE = "Q factor Receive"
    POWER_AMPLIFIER_POWER = "PA power (W)"
    GAIN = "Gain"
    TEMPERATURE = "Temperature (K)"
    AVERAGES = "Averages"
    LOSS_TX = "Loss TX (dB)"
    LOSS_RX = "Loss RX (dB)"
    CONVERSION_FACTOR = "Conversion factor"

    # Sample settinggs, this will  be done in a seperate module later on
    NAME = "Name"
    DENSITY = "Density (g/cm^3)"
    MOLAR_MASS = "Molar mass (g/mol)"
    RESONANT_FREQUENCY = "Resonant freq. (Hz)"
    GAMMA = "Gamma (Hz/T)"
    NUCLEAR_SPIN = "Nuclear spin"
    SPIN_FACTOR = "Spin factor"
    POWDER_FACTOR = "Powder factor"
    FILLING_FACTOR = "Filling factor"
    T1 = "T1 (s)"
    T2 = "T2 (s)"
    T2_STAR = "T2* (s)"
    ATOM_DENSITY = "Atom density (1/cm^3)"
    SAMPLE_VOLUME = "Sample volume (m^3)"
    SAMPLE_LENGTH = "Sample length (m)"
    SAMPLE_DIAMETER = "Sample diameter (m)"

    # Categories of the settings
    SIMULATION = "Simulation"
    HARDWARE = "Hardware"
    EXPERIMENTAL_Setup = "Experimental Setup"
    SAMPLE = "Sample"

    # Pulse parameter constants
    TX = "TX"
    RX = "RX"

    def __init__(self, module):
        super().__init__(module)

        # Simulation settings
        self.add_setting(
            self.NUMBER_POINTS,
            4096,
            "Number of points used for the simulation. This influences the dwell time in combination with the total event simulation given by the pulse sequence. ",
            self.SIMULATION,
        )
        self.add_setting(
            self.NUMBER_ISOCHROMATS, 1000, "Number of isochromats", self.SIMULATION
        )
        self.add_setting(
            self.INITIAL_MAGNETIZATION, 1, "Initial magnetization", self.SIMULATION
        )
        self.add_setting(self.GRADIENT, 1, "Gradient", self.SIMULATION)
        self.add_setting(self.NOISE, 2, "Noise", self.SIMULATION)
        self.add_setting(self.LENGTH_COIL, 6e-3, "Length coil", self.HARDWARE)
        self.add_setting(self.DIAMETER_COIL, 3e-3, "Diameter coil", self.HARDWARE)
        self.add_setting(self.NUMBER_TURNS, 9, "Number turns", self.HARDWARE)
        self.add_setting(self.Q_FACTOR_TRANSMITT, 100, "Q factor Transmitt", self.HARDWARE)
        self.add_setting(self.Q_FACTOR_RECEIVE, 100, "Q factor Receive", self.HARDWARE)
        self.add_setting(
            self.POWER_AMPLIFIER_POWER, 110, "Power amplifier power", self.HARDWARE
        )
        self.add_setting(
            self.GAIN, 6000, "Gain of the complete measurement chain", self.HARDWARE
        )
        self.add_setting(self.TEMPERATURE, 300, "Temperature", self.EXPERIMENTAL_Setup)
        self.add_setting(self.LOSS_TX, 30, "Loss TX", self.EXPERIMENTAL_Setup)
        self.add_setting(self.LOSS_RX, 30, "Loss RX", self.EXPERIMENTAL_Setup)
        self.add_setting(
            self.CONVERSION_FACTOR, 2884, "Conversion factor  (spectrometer units / V)", self.EXPERIMENTAL_Setup
        ) # Conversion factor for the LimeSDR based spectrometer

        # Sample settings
        self.add_setting(self.NAME, "BiPh3", "Name", self.SAMPLE)
        self.add_setting(self.DENSITY, 1.585e6, "Density", self.SAMPLE)
        self.add_setting(self.MOLAR_MASS, 440.3, "Molar mass", self.SAMPLE)
        self.add_setting(
            self.RESONANT_FREQUENCY, 83.56e6, "Resonant frequency", self.SAMPLE
        )
        self.add_setting(self.GAMMA, 4.342e7, "Gamma", self.SAMPLE)
        self.add_setting(self.NUCLEAR_SPIN, 9 / 2, "Nuclear spin", self.SAMPLE)
        self.add_setting(self.SPIN_FACTOR, 2, "Spin factor", self.SAMPLE)
        self.add_setting(self.POWDER_FACTOR, 0.75, "Powder factor", self.SAMPLE)
        self.add_setting(self.FILLING_FACTOR, 0.7, "Filling factor", self.SAMPLE)
        self.add_setting(self.T1, 83.5e-5, "T1", self.SAMPLE)
        self.add_setting(self.T2, 396e-6, "T2", self.SAMPLE)
        self.add_setting(self.T2_STAR, 50e-6, "T2*", self.SAMPLE)

        # Pulse parameter options
        self.add_pulse_parameter_option(self.TX, TXPulse)
        # self.add_pulse_parameter_option(self.GATE, Gate)
        self.add_pulse_parameter_option(self.RX, RXReadout)

        self.averages = 1

        # Try to load the pulse programmer module
        try:
            from nqrduck_pulseprogrammer.pulseprogrammer import pulse_programmer

            self.pulse_programmer = pulse_programmer
            logger.debug("Pulse programmer found.")
            self.pulse_programmer.controller.on_loading(self.pulse_parameter_options)
        except ImportError:
            logger.warning("No pulse programmer found.")

    @property
    def averages(self):
        return self._averages

    @averages.setter
    def averages(self, value):
        self._averages = value
