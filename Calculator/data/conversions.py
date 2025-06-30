class conversion:
    UNIT_FACTORS = {
        "LENGTH" : { "METER" : 1.0,"CM":0.01,"MM":0.001,
                    "KM": 1000.0, "INCH": 0.0254, "FEET": 0.3048,
                    "YARD": 0.9144, "MILE": 1609.34, "UM": 1e-6,
                      "ANGSTROM": 1e-10,"NM":1e-9,
                    },
        "MASS" :{ "KG": 1.0, "GRAM": 0.001, "MG": 1e-6, "TONNE": 1000.0,
            "POUND": 0.453592, "OUNCE": 0.0283495,
        },
        "TIME":{"SECOND": 1.0, "MS": 0.001, "MINUTE": 60.0, "HOUR": 3600.0,
            "DAY": 86400.0, "WEEK": 604800.0, "YEAR": 31536000.0,
        },
    }
    TEMPERATURE_FUNCS = { #KELVIN acts as a BASE unit , one is convert to KELVIN,another is Convert from KELVIN
         "CELSIUS":   (lambda v: v + 273.15, lambda v: v - 273.15),
        "FAHRENHEIT":(lambda v: (v - 32) * 5/9 + 273.15, lambda v: (v - 273.15) * 9/5 + 32),
        "KELVIN":    (lambda v: v, lambda v: v),
    }
    @staticmethod
    def find_category(unit : str): #
        unit = unit.upper()
        for cat,units in conversion.UNIT_FACTORS.items():
            if unit in units :
                return cat
        if unit in conversion.TEMPERATURE_FUNCS:
            return "TEMPERATURE"
        return None
    @staticmethod
    def convert_unit(value : float ,from_unit : str , to_unit :str) ->float :
        from_u,to_u = from_unit.upper(),to_unit.upper()
        cat = conversion.find_category(from_u) #
        if cat != conversion.find_category(to_u):
            raise ValueError(f"Error:Units are not in the same Category")
        if cat == "TEMPERATURE":
            to_kelvin = conversion.TEMPERATURE_FUNCS[from_u][0]
            from_kelvin = conversion.TEMPERATURE_FUNCS[to_u][1]
            return from_kelvin(to_kelvin(value))
        else:
            base = value * conversion.UNIT_FACTORS[cat][from_u]
            return base / conversion.UNIT_FACTORS[cat][to_u]