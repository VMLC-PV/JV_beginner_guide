###################################################
############### Useful function ###################
###################################################
# Author: Vincent M. Le Corre
# Github: https://github.com/VMLC-PV

# Import libraries
import numpy as np
import pandas as pd
from scipy import stats,constants

## Physics constants
q = constants.value(u'elementary charge')
eps_0 = constants.value(u'electric constant')
kb = constants.value(u'Boltzmann constant in eV/K')

def sci_notation(number, sig_fig=2):
    """Make proper scientific notation for graphs

    Parameters
    ----------
    number : float
        Number to put in scientific notation.

    sig_fig : int, optional
        Number of significant digits (Defaults = 2).

    Returns
    -------
    output : str
        String containing the number in scientific notation
    """
    if sig_fig != -1:
        if number == 0:
            output = '0'
        else:
            ret_string = "{0:.{1:d}e}".format(number, sig_fig)
            a,b = ret_string.split("e")
            if int(b) >= 0:
                b = int(b) #removed leading "+" and strips leading zeros too.
                c = ''
            else: 
                b = abs(int(b))
                c = u"\u207B" # superscript minus sign
            SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            b = str(b).translate(SUP)
            output =a + ' x 10' + c + b
    else:
        if number == 0:
            output = '0'
        else: 
            ret_string = "{0:.{1:d}e}".format(number, 0)
            a,b = ret_string.split("e")
            b = int(b) #removed leading "+" and strips leading zeros too.
            if int(b) >= 0:
                b = int(b) #removed leading "+" and strips leading zeros too.
                c = ''
            else: 
                b = abs(int(b))
                c = u"\u207B" # superscript minus sign
            SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            #SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            b = str(b).translate(SUP)
            output = '10' + c + b    
    return output


def LinearFunc(t,a,b):
    
    return a*t + b

def testfunc(t, tau, f0 , finf,lam):
    
    return (f0-finf) * np.exp(-(t/tau) ) + finf - lam * t 

def MonoExpDecay(t, tau, f0 , finf):
    """ Monoexponential decay function
    f(t) = (f0-finf) * np.exp(-(t/tau) ) + finf

    Parameters
    ----------
    t : 1-D sequence of floats
        time

    k : float
        lifetime

    f0 : float
        initial quantity

    finf : float
        offset

    Returns
    -------
    1-D sequence of floats
        f(t)
    """
    return (f0-finf) * np.exp(-(t/tau) ) + finf
    

def MonoExpInc(t, tau, f0, finf):
    """ Monoexponential Inc function
    f(t) = (finf-f0) *(1-np.exp(-(t/tau))) + f0)

    Parameters
    ----------
    t : 1-D sequence of floats
        time

    k : float
        lifetime

    f0 : float
        initial quantity

    finf : float
        offset

    Returns
    -------
    1-D sequence of floats
        f(t)
    """
    return (finf-f0) *(1-np.exp(-(t/tau))) + f0

def StretchedExp(t, tau, h, A, B):
    """ Stretched decay function
    f(t) = A * np.exp(- (t/tau)^h ) + B

    Parameters
    ----------
    t : 1-D sequence of floats
        time

    tau : float
        lifetime
    
    h : float
        heterogeneity parameter

    A : float
        initial quantity

    B : float
        offset

    Returns
    -------
    1-D sequence of floats
        f(t)
    """
    return A * np.exp(- (t/tau)**h ) + B

def Larryfunc(t, a1, a2, tau,  k, gamma):
    """Larry degradation fitting function
    f(t) = (1-a1*exp(-t/tau)) * 1 / ((1/a2)+k * t ** gamma)

    Parameters
    ----------
    t : 1-D sequence of floats
        time
    a1 : float
        [description]
    tau : float
        [description]
    a2 : float
        [description]
    k : float
        [description]
    gamma : float
        [description]

    Returns
    -------
    1-D sequence of floats
        f(t)
    """
    return (1-a1*np.exp(-t/tau)) * 1 / ((1/a2)+k * t ** gamma)

def get_Jsc(Volt,Curr):
    """Get the short-circuit current (Jsc) from solar cell JV-curve by interpolating the current at 0 V

    Parameters
    ----------
    Volt : 1-D sequence of floats
        Array containing the voltages.

    Curr : 1-D sequence of floats
        Array containing the current-densities.

    Returns
    -------
    Jsc : float
        Short-circuit current value
    """
    Jsc_dumb = np.interp(0, Volt, Curr)
    return Jsc_dumb

def get_Voc(Volt,Curr):
    """Get the Open-circuit voltage (Voc) from solar cell JV-curve by interpolating the Voltage when the current is 0

    Parameters
    ----------
    Volt : 1-D sequence of floats
        Array containing the voltages.

    Curr : 1-D sequence of floats
        Array containing the current-densities.

    Returns
    -------
    Voc : float
        Open-circuit voltage value
    """
    Voc_dumb = np.interp(0, Curr, Volt)
    return Voc_dumb

def get_FF(Volt,Curr):
    """Get the fill factor (FF) from solar cell JV-curve by calculating the maximum power point

    Parameters
    ----------
    Volt : 1-D sequence of floats
        Array containing the voltages.

    Curr : 1-D sequence of floats
        Array containing the current-densities.

    Returns
    -------
    FF : float
        Fill factor value
    """
    power = []
    Volt_oc = get_Voc(Volt,Curr)
    Curr_sc = get_Jsc(Volt,Curr)
    for i,j in zip(Volt,Curr):
        if (i < Volt_oc and j > Curr_sc):
            power.append(i*j)
    power_max = min(power)
    FF_dumb = power_max/(Volt_oc*Curr_sc)
    return abs(FF_dumb)

def get_PCE(Volt,Curr,suns=1):
    """Get the power conversion efficiency (PCE) from solar cell JV-curve

    Parameters
    ----------
    Volt : 1-D sequence of floats
        Array containing the voltages.

    Curr : 1-D sequence of floats
        Array containing the current-densities.

    Returns
    -------
    PCE : float
        Power conversion efficiency value.
    """
    Voc_dumb = get_Voc(Volt,Curr)
    Jsc_dumb = get_Jsc(Volt, Curr)
    FF_dumb = get_FF(Volt, Curr)
    PCE_dumb = Voc_dumb*Jsc_dumb*FF_dumb/suns
    return abs(PCE_dumb)

def get_ideality_factor(suns,Vocs,T=295):
    """Returns ideality factor from suns-Voc data linear fit of Voc = (nIF/Vt)*log(suns) + intercept

    Parameters
    ----------
    suns : 1-D sequence of floats
        Array containing the intensity in sun.

    Vocs : 1-D sequence of floats
        Array containing the open-circuit voltages.
    
    T : float optional
        Temperature in Kelvin (Default = 295 K).

    Returns
    -------
    nIF : float
        Ideality factor value.

    intercept : float
        Intercept of the regression line.

    rvalue : float
        Correlation coefficient.

    pvalue : float
        Two-sided p-value for a hypothesis test whose null hypothesis is
        that the slope is zero, using Wald Test with t-distribution of
        the test statistic.

    stderr : float
        Standard error of the estimated gradient.
    """
    Vt = kb*T
    suns = np.log(suns)
    slope_d, intercept_d, r_value_d, p_value_d, std_err_d = stats.linregress(suns,Vocs)
    nIF = slope_d/Vt
    return nIF,intercept_d, r_value_d**2, p_value_d, std_err_d

def get_alpha_factor(suns,Jscs):
    """Returns alpha from suns-Jsc data linear fit of log(Jsc) = alpha*log(suns) + b

    Parameters
    ----------
    suns : 1-D sequence of floats
        Array containing the intensity in sun.

    Vocs : 1-D sequence of floats
        Array containing the open-circuit voltages.
    
    Returns
    -------
    alpha : float
        Alpha value.

    intercept : float
        Intercept of the regression line.

    rvalue : float
        Correlation coefficient.

    pvalue : float
        Two-sided p-value for a hypothesis test whose null hypothesis is
        that the slope is zero, using Wald Test with t-distribution of
        the test statistic.

    stderr : float
        Standard error of the estimated gradient.
    """
    suns = np.log(suns)
    Jscs = np.log(Jscs)
    alpha, intercept_d, r_value_d, p_value_d, std_err_d = stats.linregress(suns,Jscs)
    return alpha,intercept_d, r_value_d**2, p_value_d, std_err_d

def get_random_value(val_min,val_max,scale='lin'):
    """Get random value between two boundaries

    Parameters
    ----------
    val_min : float
        min value
    
    val_max : float
        max value

    scale : str, optional
        scale type, by default 'lin'

    Returns
    -------
    float
        random value
    """
    if val_min > val_max:
        dum_min = min(val_min,val_max)
        dum_max =  max(val_min,val_max)
        val_min = dum_min
        val_max = dum_max
        print('Careful, the val_min > val_max, check the input for get_random_value')

    random_val = random.uniform(0, 1)
    if scale == 'lin':
        val = (val_max - val_min) * random_val + val_min
    elif scale == 'log':
        val = np.sign(val_max) * np.exp( random_val * ( np.log(abs(val_max)) - np.log(abs(val_min)) ) +np.log(abs(val_min)) )
    elif scale == 'int':
        val = int(round((val_max - val_min) * random_val + val_min))
    else:
        print('The program will stop')
        sys.exit('Wrong scale for the input parameters')
    return val
