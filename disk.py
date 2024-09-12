import numpy as np


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    if height <= 0 or length <= 0 or incline <= 0 or incline >= 90 or mass <= 0 or friction <= 0 or radius <= 0:
        print("Please ensure all values given are positive and incline is between 0 and 90")
        return None

    # Use work energy theorem
    # Rotational kinetic, translational kinetic and gravitational energy should be conserved
    # Starting rotational kinetic and translational kinetic energy is 0
    # Ending graviational energy is 0
    # Therefore, we have 0 = Kr_end + Kt_end - Ug_start

    # Moment of inertia is 1/2 mass * radius^2
    moment = 0.5 * mass * radius**2
    g = 9.81


    # Ending rotational energy is 1/2 * moment * omega^2 which I will change to 
    # 1/2 * moment * (1/radius)^2 * velocity^2 which has term of velocity^2
    rotational_end = 0.5 * moment * (1/radius)**2

    # Ending translational energy is 1/2 * mass * velocity^2 which has term of
    # velocity^2
    translational_end = 0.5 * mass

    # Starting gravitational energy is mass * g * height which is constant term
    gravity_start = mass * g * height

    coeffs = [translational_end + rotational_end, 0, gravity_start]
    roots = np.roots(coeffs)

    # We will get two complex roots, which only have a j value, so we can take
    # absolute magnitude of the roots
    for root in roots:
        if abs(root) > 0:
            return abs(root)

    # In case we have no positive roots, return None
    return None
