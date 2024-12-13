from PricePredictionMethods import methods
import yfinance as yf

#ticker = input("Welcome! Please enter the stock you are looking for! ")
#deneme kolaylığı olsun diye ticker input kısmı yoruma alındı yerine sabit
#ticker konuldu 

ticker = "BTC-USD"
stock = yf.Ticker(ticker)
data = stock.history(period= '1mo')
S = data["Close"].iloc[-1]

K = 100509  # Kullanım fiyatı
T = 1    # Süre (yıl)
r = 5 # Faiz oranı
sigma = 0.2 # Volatilite
num_simulations = 1000000 # Simülasyon sayısı

# Fiyatlandırma
bs_price = methods.black_scholes(S, K, T, r, sigma)
mc_price = methods.monte_carlo_option_price(S, K, T, r, sigma, num_simulations)

print(f"Black-Scholes Fiyati: {bs_price}")
print(f"Monte Carlo Simulasyon Fiyati: {mc_price}")