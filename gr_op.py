import numpy as np


def noise(x):
    x_volts = np.array(x)
    x_watts = x_volts ** 2
    target_snr_db = 20
    sig_avg_watts = np.mean(x_watts)
    sig_avg_db = 10 * np.log10(sig_avg_watts)
    noise_avg_db = sig_avg_db - target_snr_db
    noise_avg_watts = 10 ** (noise_avg_db / 10)
    mean_noise = 0
    noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(x_watts))
    y_volts = x_volts + noise_volts
    return y_volts
