import numpy as np

def powerSpectrum(xx, dt, frange):
    fmin, fmax = frange                            # 角振動数の範囲
    xx -= np.mean(xx)                              # 平均値を差し引く
    ndat = len(xx)
    w = np.hanning(ndat)                           # 窓関数
    xx_fft = np.fft.fft(xx*w)/(ndat/2)             # FFT
    xx_fft /= np.sum(w)/ndat                       # 窓関数の補正
    freq = np.fft.fftfreq(ndat, dt)*2*np.pi        # 角振動数の配列
    idx = np.where((fmin < freq) & (freq < fmax))  # 配列のindex
    xx_pow = np.abs(xx_fft[idx])**2                # パワースペクトル
    return freq[idx], xx_pow

