import numpy as np
import scipy.stats as si

# Black-Scholes opsiyon fiyatlandırma fonksiyonu
def black_scholes(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    C = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    return C

# Monte Carlo Simülasyonu ile fiyat tahmini
def monte_carlo_option_price(S, K, T, r, sigma, num_simulations):
    payoffs = []
    for _ in range(num_simulations):
        # Rastgele son fiyat oluşturma
        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * np.random.normal())
        payoff = max(ST - K, 0)  # Call opsiyonu için kazanç
        payoffs.append(payoff)
    
    return np.exp(-r * T) * np.mean(payoffs)

# Parametreler
S = 100  # Hisse senedi fiyatı
K = 100  # Kullanım fiyatı
T = 1    # Süre (yıl)
r = 0.05 # Faiz oranı
sigma = 0.2 # Volatilite
num_simulations = 10000 # Simülasyon sayısı

# Fiyatlandırma
bs_price = black_scholes(S, K, T, r, sigma)
mc_price = monte_carlo_option_price(S, K, T, r, sigma, num_simulations)

print(f"Black-Scholes Fiyatı: {bs_price}")
print(f"Monte Carlo Simülasyon Fiyatı: {mc_price}")
