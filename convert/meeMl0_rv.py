from .meeMl0_mee import meeMl0_mee
from .mee_rv import mee_rv

__author__ = "Nathan I. Budd"
__email__ = "nibudd@gmail.com"
__copyright__ = "Copyright 2017, LASR Lab"
__license__ = "MIT"
__version__ = "0.1"
__status__ = "Production"
__date__ = "30 Mar 2017"


def meeMl0_rv(T, rv, mu=1.0):
    """Convert RV to MEEs with mean longitude at epoch.

    Args:
        T: ndarray
            (m, 1) array of times.
        rv: ndarray
            (m, 6) array of position-velocity elements ordered as
            (rx, ry, rz, vx, vy, vz),
            where
            rx = position x-component
            ry = position y-component
            rz = position z-component
            vx = velocity x-component
            vy = velocity y-component
            vz = velocity z-component
        mu: float, optional
            Standard Gravitational Parameter. Defaults to 1.0, the standard
            value in canonical units.

    Returns:
        meeMl0: ndarray
            (m, 6) array of modified equinoctial elements ordered as
            (p, f, g, h, k, Ml0), where
            p = semi-latus rectum
            f = 1-component of ecentricity vector in perifocal frame
            g = 2-component of eccentricity vector in perifocal frame
            h = 1-component of the ascending node vector in equinoctial frame
            k = 2-component of the ascending node vector in equinoctial frame
            Ml0 = mean longitude at epoch
    """
    return meeMl0_mee(T, mee_rv(rv))
