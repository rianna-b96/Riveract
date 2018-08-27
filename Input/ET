# A series of functions to calculate the relevant variables to
# determine the Evapotranspiration

import math


# Mean Daily Temperature
def t_mean(t_max: float, t_min: float) -> float:

    """
    :param t_max: Maximum Daily Air Temperature - Degrees Celsius
    :param t_min: Minimum Daily Air Temperature - Degrees Celsius
    :return: Mean Daily Air Temperature - Degrees Celsius
    """
    return (t_max+t_min)/2


# Mean Daily Solar Radiation Conversion
def solar_rad_conversion(rs: float) -> float:
    """
    Use this function to convert Solar Radiation
    from W/m^2/day - Watts per metres squared per day
    to MJ/m^2/day - MJ per metres squared per day
    :param rs: Solar Radiation W/m^2/day
    :return:
    """
    return rs*0.0864


# Wind Speed
def wind_speed(u_h: float, h: float) -> float:
    """
    Converts wind speed taken at 'h' meters above the ground surface 
    and adjusts it to a wind speed to 2m above the ground surface
    :param u_h: Wind speed 'h' meters above the ground surface - ms^-1
    :param h: Height of the measurement above the ground surface - m 
    :return: Wind speed 2m above the ground surface
    """
    denominator = math.log(67.8*h-5.42)
    return (u_h*4.87)/denominator


# Wind Speed Conversion
def wind_speed_conversion(u2: float) -> float:
    """
    Converts wind speed given in miles per hour to wind speed in
    metres per second
    :param u2: Wind speed - miles per hour
    :return: Wind speed - metres per second
    """
    return u2*0.447


# Slope of Saturation Vapour Pressure Curve
def svpc(t_mean: float) -> float:
    """
    Calculates the slope of the relationship between saturation and
    vapour pressure and temperature
    :param t_mean: Mean Daily Air Temperature - Degrees Celsius
    :return: Slope of the Saturation Vapour Pressure Curve
    """
    numerator = 4098*(0.6108*math.exp((17.27*t_mean)/(t_mean+237.3)))
    denominator = (t_mean+237.3)**2
    return numerator/denominator


# Atmospheric Pressure
def atmos_pressure(z: float) -> float:
    """
    A simplification of the ideal gas law, assuming 20 degrees Celsius for
    a standard atmosphere, calculating Atmospheric Pressure at a particular
    elevation
    :param z: Elevation Above Sea Level - metres
    :return: Atmospheric Pressure - kPa
    """
    bracket = ((293-0.0065*z)/293)**5.26
    return 101.3*bracket


# Psychrometric Constant
def psychrometric_const(P: float) -> float:
    """
    As an average atmospheric pressure is used for each location, the
    psychrometric constant is kept constant for each location depending
    on the altitude
    :param P: Atmospheric Pressure - kPa
    :return: Psychometric Constant - kPa
    """
    return 0.000665*P


# Delta Term
def delta_term(delta: float, gamma: float, u2: float) -> float:
    """
    Auxillary calculation for Radiation Term
    :param delta: Slope of Saturation Vapor Curve
    :param pc: Psychrometric Constant - kPa Degrees Celsius ^-1
    :param u2: Wind Speed 2m Above Ground Surface - m s-1
    :return: 'Radiation Term' of overall ET0 equation
    """
    denominator = delta+gamma*(1+0.34*u2)
    return delta/denominator


# PSI Term
def psi_term(delta: float, gamma: float, u2: float) -> float:
    """
    Auxillary Calculation for Wind Term
    :param delta: Slope of Saturation Vapor Curve
    :param gamma: Psychrometric Constant - kPa Degrees Celsius ^-1
    :param u2: Wind Speed 2m Above Ground Surface -m s-1
    :return: 'Wind Term' of the ET0 equation
    """
    denominator = delta + gamma*(1+0.34*u2)
    return gamma/denominator


# Temperature Term
def temperature_term(t_mean: float, u2: float) -> float:
    """
    Auxillary calculation for Wind Term
    :param t_mean: Mean Daily Air Temperature - Degrees Celsius
    :param u2: Wind Speed 2m Above Ground Surface -m s-1
    :return: 'Wind Term' of the overall ET0 equation
    """
    brackets = (900/(t_mean+273))
    return brackets*u2


