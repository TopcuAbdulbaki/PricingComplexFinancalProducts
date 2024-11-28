from PricePredictionMethods import methods

S = 100  # Hisse senedi fiyatı
K = 100  # Kullanım fiyatı
T = 1    # Süre (yıl)
r = 0.05 # Faiz oranı
sigma = 0.2 # Volatilite
num_simulations = 10000 # Simülasyon sayısı

# Fiyatlandırma
bs_price = methods.black_scholes(S, K, T, r, sigma)
mc_price = methods.monte_carlo_option_price(S, K, T, r, sigma, num_simulations)

print(f"Black-Scholes Fiyatı: {bs_price}")
print(f"Monte Carlo Simülasyon Fiyatı: {mc_price}")
