class constants:
    SCIENTIFIC_CONSTANTS = { #dictionary 
        "PI": 3.141592653589793,
        "E": 2.718281828459045,
        "C": 299792458.0,           # Speed of light (m/s)
        "G": 6.67430e-11,           # Gravitational constant (N m^2 / kg^2)
        "H": 6.62607015e-34,        # Planck constant (J s)
        "NA": 6.02214076e23,        # Avogadro constant (1/mol)
        "K": 1.380649e-23,          # Boltzmann constant (J/K)
        "R": 8.314462618,           # Molar gas constant (J/(mol·K))
        "MU0": 1.25663706212e-6,    # Permeability of vacuum (N/A^2)
        "EPS0": 8.8541878128e-12,   # Permittivity of vacuum (F/m)
        "ME": 9.1093837015e-31,     # Electron mass (kg)
        "MP": 1.67262192369e-27,    # Proton mass (kg)
        "MN": 1.67492749804e-27,    # Neutron mass (kg
    }
    @staticmethod
    def get_scientific_constant(name : str) -> float :
        try :
            return constants.SCIENTIFIC_CONSTANTS[name.strip().upper()] # strip eads leading or trialing whitespace
        except KeyError:
            raise ValueError(f"Scientific Constant '{name}' not found")


         