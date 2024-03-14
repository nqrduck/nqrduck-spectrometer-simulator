import logging
from nqrduck_spectrometer.base_spectrometer_model import BaseSpectrometerModel
from nqrduck_spectrometer.pulseparameters import TXPulse, RXReadout
from nqrduck_spectrometer.settings import (
    FloatSetting,
    IntSetting,
    BooleanSetting,
    SelectionSetting,
    StringSetting,
)

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
    Q_FACTOR_TRANSMIT = "Q factor Transmit"
    Q_FACTOR_RECEIVE = "Q factor Receive"
    POWER_AMPLIFIER_POWER = "PA power (W)"
    GAIN = "Gain"
    TEMPERATURE = "Temperature (K)"
    AVERAGES = "Averages"
    LOSS_TX = "Loss TX (dB)"
    LOSS_RX = "Loss RX (dB)"
    CONVERSION_FACTOR = "Conversion factor"

    # Sample settings, this will  be done in a separate module later on
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
        number_of_points_setting = IntSetting(
            self.NUMBER_POINTS,
            8192,
            "Number of points used for the simulation. This influences the dwell time in combination with the total event simulation given by the pulse sequence.",
        )
        self.add_setting(
            number_of_points_setting,
            self.SIMULATION,
        )

        number_of_isochromats_setting = IntSetting(
            self.NUMBER_ISOCHROMATS,
            1000,
            "Number of isochromats used for the simulation. This influences the computation time.",
        )
        self.add_setting(number_of_isochromats_setting, self.SIMULATION)

        initial_magnetization_setting = FloatSetting(
            self.INITIAL_MAGNETIZATION,
            1,
            "Initial magnetization",
        )
        self.add_setting(initial_magnetization_setting, self.SIMULATION)

        # This doesn't really do anything yet
        gradient_setting = FloatSetting(
            self.GRADIENT,
            1,
            "Gradient",
        )
        self.add_setting(gradient_setting, self.SIMULATION)

        noise_setting = FloatSetting(
            self.NOISE,
            2,
            "Noise",
        )
        self.add_setting(noise_setting, self.SIMULATION)

        # Hardware settings
        coil_length_setting = FloatSetting(
            self.LENGTH_COIL,
            30e-3,
            "Length coil",
        )
        self.add_setting(coil_length_setting, self.HARDWARE)

        coil_diameter_setting = FloatSetting(
            self.DIAMETER_COIL,
            8e-3,
            "Diameter coil",
        )
        self.add_setting(coil_diameter_setting, self.HARDWARE)

        number_turns_setting = FloatSetting(
            self.NUMBER_TURNS,
            8,
            "Number turns",
        )
        self.add_setting(number_turns_setting, self.HARDWARE)

        q_factor_transmit_setting = FloatSetting(
            self.Q_FACTOR_TRANSMIT,
            80,
            "Q factor Transmit",
        )
        self.add_setting(q_factor_transmit_setting, self.HARDWARE)

        q_factor_receive_setting = FloatSetting(
            self.Q_FACTOR_RECEIVE,
            80,
            "Q factor Receive",
        )
        self.add_setting(q_factor_receive_setting, self.HARDWARE)

        power_amplifier_power_setting = FloatSetting(
            self.POWER_AMPLIFIER_POWER,
            110,
            "Power amplifier power",
        )
        self.add_setting(
            power_amplifier_power_setting, self.HARDWARE
        )

        gain_setting = FloatSetting(
            self.GAIN,
            6000,
            "Gain of the complete measurement chain",
        )
        self.add_setting(
            gain_setting, self.HARDWARE
        )

        temperature_setting = FloatSetting(
            self.TEMPERATURE,
            300,
            "Temperature",
        )
        self.add_setting(temperature_setting, self.EXPERIMENTAL_Setup)

        loss_tx_setting = FloatSetting(
            self.LOSS_TX,
            25,
            "Loss TX in dB",
        )
        self.add_setting(loss_tx_setting, self.EXPERIMENTAL_Setup)

        loss_rx_setting = FloatSetting(
            self.LOSS_RX,
            25,
            "Loss RX in dB",
        )
        self.add_setting(loss_rx_setting, self.EXPERIMENTAL_Setup)

        conversion_factor_setting = FloatSetting(
            self.CONVERSION_FACTOR,
            2884,
            "Conversion factor  (spectrometer units / V)",
        )
        self.add_setting(
            conversion_factor_setting,
            self.EXPERIMENTAL_Setup,
        )  # Conversion factor for the LimeSDR based spectrometer

        # Sample settings
        sample_name_setting = StringSetting(
            self.NAME,
            "BiPh3",
            "Name",
        )
        self.add_setting(sample_name_setting, self.SAMPLE)

        density_setting = FloatSetting(
            self.DENSITY,
            1.585e6,
            "Density",
        )
        self.add_setting(density_setting, self.SAMPLE)

        molar_mass_setting = FloatSetting(
            self.MOLAR_MASS,
            440.3,
            "Molar mass",
        )
        self.add_setting(molar_mass_setting, self.SAMPLE)

        resonant_frequency_setting = FloatSetting(
            self.RESONANT_FREQUENCY,
            83.56e6,
            "Resonant frequency",
        )
        self.add_setting(
            resonant_frequency_setting, self.SAMPLE
        )

        gamma_setting = FloatSetting(
            self.GAMMA,
            4.342e7,
            "Gamma",
        )
        self.add_setting(gamma_setting, self.SAMPLE)

        nuclear_spin_setting = FloatSetting(
            self.NUCLEAR_SPIN,
            9 / 2,
            "Nuclear spin",
        )
        self.add_setting(nuclear_spin_setting, self.SAMPLE)

        spin_factor_setting = FloatSetting(
            self.SPIN_FACTOR,
            2,
            "Spin factor",
        )
        self.add_setting(spin_factor_setting, self.SAMPLE)

        powder_factor_setting = FloatSetting(
            self.POWDER_FACTOR,
            0.75,
            "Powder factor",
        )
        self.add_setting(powder_factor_setting, self.SAMPLE)

        filling_factor_setting = FloatSetting(
            self.FILLING_FACTOR,
            0.7,
            "Filling factor",
        )
        self.add_setting(filling_factor_setting, self.SAMPLE)

        t1_setting = FloatSetting(
            self.T1,
            83.5e-5,
            "T1",
        )
        self.add_setting(t1_setting, self.SAMPLE)

        t2_setting = FloatSetting(
            self.T2,
            396e-6,
            "T2",
        )
        self.add_setting(t2_setting, self.SAMPLE)

        t2_star_setting = FloatSetting(
            self.T2_STAR,
            50e-6,
            "T2*",
        )
        self.add_setting(t2_star_setting, self.SAMPLE)

        # Pulse parameter options
        self.add_pulse_parameter_option(self.TX, TXPulse)
        # self.add_pulse_parameter_option(self.GATE, Gate)
        self.add_pulse_parameter_option(self.RX, RXReadout)

        self.averages = 1
        self.target_frequency  = 100e6

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

    @property
    def target_frequency(self):
        return self._target_frequency
    
    @target_frequency.setter
    def target_frequency(self, value):
        self._target_frequency = value

