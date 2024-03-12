from .cloud_model import CloudModel 
from scipy import interpolate
from scipy import optimize
import numpy as np 
from cmath import sqrt
from pathlib import Path

class RelScalar(CloudModel):
    """
    Relativistic (alpha~1) model for scalar bosons

    All in inputs are in units where black hole mass=1
    alpha is boson mass (times black hole mass)
    abh is black hole dimensionless spin
    Mcloud is boson cloud mass (as fraction of black hole mass) 
    m is azimuthal number of cloud
    """
    def __init__(self):
        """Caching tabulated and fit data"""

        """ 
        m=1 modes: 
        """
        m1_data = np.load(Path(__file__).parent.joinpath('data/m1_sc_mds.npz'))
        m1_wr = m1_data['wr'].flatten()
        m1_wi = m1_data['wi'].flatten()
        m1_a = m1_data['a'].flatten()
        m1_y = m1_data['y'].flatten()
        m1_dwr = m1_data['dwr'].flatten()
        self._f1wr = interpolate.LinearNDInterpolator(list(zip(m1_y,m1_a)),m1_wr)
        self._f1dwr = interpolate.LinearNDInterpolator(list(zip(m1_y,m1_a)),m1_dwr)
        self._f1wi = interpolate.LinearNDInterpolator(list(zip(m1_y,m1_a)),m1_wi)

        """ 
        m=2 modes: 
        """
        m2_data = np.load(Path(__file__).parent.joinpath('data/m2_sc_mds.npz'))
        m2_wr = m2_data['wr'].flatten()
        m2_wi = m2_data['wi'].flatten()
        m2_a = m2_data['a'].flatten()
        m2_y = m2_data['y'].flatten()
        m2_dwr = m2_data['dwr'].flatten()
        self._f2wr = interpolate.LinearNDInterpolator(list(zip(m2_y,m2_a)),m2_wr)
        self._f2dwr = interpolate.LinearNDInterpolator(list(zip(m2_y,m2_a)),m2_dwr)
        self._f2wi = interpolate.LinearNDInterpolator(list(zip(m2_y,m2_a)),m2_wi)

        """
        Fit coefficients
        """
        fit_data = np.load(Path(__file__).parent.joinpath('data/sc_fits.npz'))
        self._amat1 = fit_data['amat1']
        self._bmat1 = fit_data['bmat1']
        self._cmat1 = fit_data['cmat1']
        self._amat2 = fit_data['amat2']
        self._bmat2 = fit_data['bmat2']
        self._cmat2 = fit_data['cmat2']

        """
        Radiation data
        """
        sat_flux_data = np.load(Path(__file__).parent.joinpath('data/sc_sat_gw.npz'))
        m1_flux = sat_flux_data['m1_flux']
        m1_mu = sat_flux_data['m1_mu']
        m1_Z2r = sat_flux_data['m1_z2r']
        m1_Z2i = sat_flux_data['m1_z2i']
        m1_Z3r = sat_flux_data['m1_z3r']
        m1_Z3i = sat_flux_data['m1_z3i']
        m2_flux = sat_flux_data['m2_flux']
        m2_mu = sat_flux_data['m2_mu']
        m2_Z4r = sat_flux_data['m2_z4r']
        m2_Z4i = sat_flux_data['m2_z4i']
        m2_Z5r = sat_flux_data['m2_z5r']
        m2_Z5i = sat_flux_data['m2_z5i']

        self._pwm1 = interpolate.interp1d(m1_mu, m1_flux, kind='cubic')
        self._z2rm1 = interpolate.interp1d(m1_mu, m1_Z2r, kind='cubic')
        self._z2im1 = interpolate.interp1d(m1_mu, m1_Z2i, kind='cubic')
        self._z3rm1 = interpolate.interp1d(m1_mu, m1_Z3r, kind='cubic')
        self._z3im1 = interpolate.interp1d(m1_mu, m1_Z3i, kind='cubic')
        self._pwm2 = interpolate.interp1d(m2_mu, m2_flux, kind='cubic')
        self._z4rm2 = interpolate.interp1d(m2_mu, m2_Z4r, kind='cubic')
        self._z4im2 = interpolate.interp1d(m2_mu, m2_Z4i, kind='cubic')
        self._z5rm2 = interpolate.interp1d(m2_mu, m2_Z5r, kind='cubic')
        self._z5im2 = interpolate.interp1d(m2_mu, m2_Z5i, kind='cubic')

    def max_azi_num(self):
        """Maximum azimuthal number the model is defined for"""
        return 2
    def max_spin(self):
        """Maximum spin the model is defined for"""
        return 0.995 
    def omega_real(self, m, alpha, abh, Mcloud):
        """Returns real frequency of cloud oscillation"""
        yl, alphamax, Oh = self._y(m, alpha, abh)
        dwr = self._deltaomega(m, alpha, abh)
        if (m==1):
            if (alpha>=0.05 and abh>=self._aswitch(m)):
                wr = alpha*self._f1wr(yl, abh)
            else:
                # Ensures output fails sup. condition if alpha too large
                if (not(self._maxalphaInterp(m, alpha))):
                    return np.nan
                wr = alpha*(1.0-alpha**2/8.0-17.0*alpha**4/128.0+abh*alpha**5/12.0)
                wr += alpha*0.0028391854462700*alpha**5*(abh*np.sqrt(1-abh**2)-abh)
                for p in range(6, 9):
                    for q in range(0, 4):
                        wr += alpha**(p+1)*(1.0-abh**2)**(q/2.0)*self._amat1[p-6,q]
            return wr+Mcloud*dwr
        elif (m==2):
            if (alpha>=0.25 and abh>=self._aswitch(m)):
                wr = alpha*self._f2wr(yl, abh)
            else:
                # Ensures output fails sup. condition if alpha too large
                if (not(self._maxalphaInterp(m, alpha))):
                    return np.nan
                wr = alpha*(1.0-alpha**2/18.0-23.0*alpha**4/1080.0+4.0*abh*alpha**5/405.0)
                wr += alpha*0.0024403837275569847*alpha**5*(abh*np.sqrt(1-abh**2)-abh)
                for p in range(6, 9):
                    for q in range(0, 4):
                        wr += alpha**(p+1)*(1.0-abh**2)**(q/2.0)*self._amat2[p-6,q]
            return wr+Mcloud*dwr
        else:
            raise ValueError("Azimuthal index too large")
    def domegar_dmc(self, m, alpha, abh, Mcloud):
        """Returns derivative of real frequency of cloud w.r.t. cloud mass"""
        return self._deltaomega(m, alpha, abh)
    def omega_imag(self, m, alpha, abh):
        """Returns imaginary frequency, 
           i.e. growth rate of superradiant instability"""
        yl, alphamax, Oh = self._y(m, alpha, abh)
        wr = self.omega_real(m, alpha, abh, 0)
        if (m==1):
            if (alpha>=0.05 and abh>=self._aswitch(m)):
                return -np.exp(self._f1wi(yl, abh))*(wr-m*Oh)
            else:
                wi = 1.0
                glm = 1-abh**2+(abh*m-2.0*wr*(1.0+np.sqrt(1.0-abh**2)))**2
                for p in range(1, 4):
                    for q in range(0, 4):
                        wi += alpha**p*(abh**(q+1)*self._bmat1[q,p-1]+self._cmat1[q,p-1]*(1.0-abh**2)**(q/2.0))
                wi *= -2.0*(1.0+np.sqrt(1.0-abh**2))*glm*alpha**9*(wr-m*Oh)/48.0
                return wi
        elif (m==2):
            if (alpha>=0.25 and abh>=self._aswitch(m)):
                return -np.exp(self._f2wi(yl, abh))*(wr-m*Oh)
            else:
                wi = 1.0
                glm = 1-abh**2+(2.0*abh-2.0*wr*(1.0+np.sqrt(1.0-abh**2)))**2
                glm *= 4.0*(1-abh**2)+(2.0*abh-2.0*wr*(1.0+np.sqrt(1.0-abh**2)))**2
                wi += -1.1948426572069112e11*alpha**12+2.609027546773062e12*alpha**13
                for p in range(12, 23):
                    wi += self._cmat2[p-12]*alpha**p*(1.0-abh**2)**0.5
                    for q in range(0, 3):
                        wi += alpha**(p+2)*abh**q*self._bmat2[q,p-12]
                wi *= -2.0*(1.0+np.sqrt(1.0-abh**2))*glm*alpha**13*(wr-m*Oh)*4.0/885735.0
                return wi
        else:
            raise ValueError("Azimuthal index too large")
    def power_gw(self, m, alpha, abh):
        """Returns gravitational wave power, scaled to Mcloud=1 
        Using: omega_R(Mcloud=0), valid only at saturation"""
        if (m==1):
            if (alpha<0.2):
                a14 = 0.0109289473739731
                a15 = -0.0290105840870259
                return a14*alpha**14+a15*alpha**15
            else:
                return self._pwm1(alpha)
        elif (m==2):
            if (alpha<0.34):
                a18 = 6.46575425669374e-7
                a19 = -1.12205283686066e-6
                return a18*alpha**18+a19*alpha**19
            else:
                return self._pwm2(alpha)
        else:
            raise ValueError("Azimuthal index too large")
    def strain_sph_harm(self, m, alpha, abh):
        """Returns e^{iwt}R h^{\ell 2m} (-2-weighted spherical harmonic components)"""
        spsat = self._spinsat(m, alpha)
        wr = 2.0*self.omega_real(m, alpha, spsat, 0)
        if (m==1):
            if (alpha<0.2):
                z2abs = 2.0*np.pi*np.sqrt(wr**2*self.power_gw(m, alpha, spsat))
                return 2.0*np.array([z2abs,0])/(np.sqrt(2.0*np.pi)*wr**2)
            else:
                z2 = self._z2rm1(alpha)+1j*self._z2im1(alpha)
                z3 = self._z3rm1(alpha)+1j*self._z3im1(alpha)
                return -2.0*np.array([z2, z3])/(np.sqrt(2.0*np.pi)*wr**2)
        elif (m==2):
            if (alpha<0.34):
                z4abs = 2.0*np.pi*np.sqrt(wr**2*self.power_gw(m, alpha, spsat))
                return 2.0*np.array([z4abs,0])/(np.sqrt(2.0*np.pi)*wr**2)
            else:
                z4 = self._z4rm2(alpha)+1j*self._z4im2(alpha)
                z5 = self._z5rm2(alpha)+1j*self._z5im2(alpha)
                return -2.0*np.array([z4, z5])/(np.sqrt(2.0*np.pi)*wr**2)
        else:
            raise ValueError("Azimuthal index too large")
    def _aswitch(self, m):
        return 0.6
    def _maxalphaInterp(self, m, alpha):
        """Returns True if alpha is below the saturation-alpha for each m at abh=aswitch(m)"""       
        if (m==1):
            return alpha<0.18
        elif (m==2):
            return alpha<0.4
        else:
            raise ValueError("Azimuthal index too large") 
    def _y(self, m, alpha, abh, beta=0.9):
        """Returns utility parameter y, approximate maximal alpha, horizon frequency"""
        if (m==1):
            alpha0 = 0.05
        else:
            alpha0 = 0.25
        Oh = 0.5*abh/(1.0+np.sqrt(1.0-abh**2))
        temp = 9.0*m*(m+1)**2*Oh*beta**2+sqrt(81*m**2*(1+m)**4*Oh**2*beta**4-24*(1+m)**6*beta**6)
        alphamaxC = ((3**(1.0/3.0)+1j*3**(5.0/6.0))*temp**(2.0/3.0)-4.0*(-3.0)**(2.0/3.0)*(m+1)**2*beta**2)/(6.0*temp**(1.0/3.0)*beta)
        alphamax = alphamaxC.real
        yl = (alpha-alpha0)/(alphamax-alpha0)
        return yl, alphamax, Oh
    def _deltaomega(self,m,alpha,abh):
        """Returns the cloud mass-independent frequency shift due to self-gravity"""
        yl, alphamax, Oh = self._y(m, alpha, abh)
        #Factor of 2 below is to go from gravitational potential energy to frequency shift
        if (m==1):
            if (alpha>=0.05 and abh>=self._aswitch(m)):
                return -2.0*alpha*self._f1dwr(yl, abh)
            else:
                dwr = -93*alpha**3/1024.0
                dwr += -alpha*(-0.0040394234400504087576*alpha**3 + 0.67372467642478683914*alpha**4 - 3.5059737204226921747*alpha**5 + 5.2355803557173512530*alpha**6)
                return 2.0*dwr
        elif (m==2):
            if (alpha>=0.25 and abh>=self._aswitch(m)):
                return -2.0*alpha*self._f2dwr(yl, abh)
            else:
                dwr = -793*alpha**3/18432.0
                dwr += alpha*(-0.13855421027039729887*alpha**3 + 1.159105481278182692*alpha**4 - 3.1372867270252249305*alpha**5 + 2.8141844762025582938*alpha**6)
                return 2.0*dwr
        else:
            raise ValueError("Azimuthal index too large")
    def _alphasat(self, m, abh):
        """Bisection to find saturation point, returns alpha at saturation"""
        yh, amaxh, Ohh = self._y(m, 0, abh)
        yl, amaxl, Ohl = self._y(m, 0, abh, 1.1)
        def _sat(al):
            satout = self.omega_real(m, al, abh, 0)-m*0.5*abh/(1.0+np.sqrt(1.0-abh**2))
            if (np.isnan(satout)): satout = 1e10
            return satout
        return optimize.bisect(_sat, amaxl, amaxh)
    def _spinsat(self, m, al):
        """Bisection to find saturation point, returns spin at saturation"""
        def _sat(abh):
            satout = self.omega_real(m, al, abh, 0)-m*0.5*abh/(1.0+np.sqrt(1.0-abh**2))
            if (np.isnan(satout)): satout = 1e10
            return satout
        return optimize.bisect(_sat, self.max_spin(), 0)       
