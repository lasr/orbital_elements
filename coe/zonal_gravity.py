import orbital_elements.convert as convert
from orbital_elements.coe.gve import GVE
from orbital_elements.rv.zonal_gravity import ZonalGravity as rvZonalGravity


__author__ = "Nathan I. Budd"
__email__ = "nibudd@gmail.com"
__copyright__ = "Copyright 2017, LASR Lab"
__license__ = "MIT"
__version__ = "0.1"
__status__ = "Production"
__date__ = "16 Mar 2017"


class ZonalGravity(rvZonalGravity):
    """Zonal gravity dynamics for classical orbital elements."""

    def __init__(self, mu=1.0, order=2, r_earth=1.0):
        super().__init__(mu=mu, order=order, r_earth=r_earth)

    def __call__(self, T, X):
        """Calculate zonal gravity perturations in classical orbital elements.

        Args:
            T: ndarray
                (m, 1) array of times.
            X: ndarray
                (m, 6) array of states ordered as (a, e, i, W, w, f), where
                a = semi-major axis
                e = eccentricity
                i = inclination
                W = right ascension of the ascending node
                w = argument of perigee
                f = true anomaly

        Returns:
            Xdot: ndarray
                (m, 6) array of state derivatives.
        """
        super().lvlh_acceleration(T, convert.rv_coe(X))
        G = GVE()(T, X)
        m = T.shape[0]

        return (G @ self.a_lvlh.reshape((m, 3, 1))).reshape((m, 6))
