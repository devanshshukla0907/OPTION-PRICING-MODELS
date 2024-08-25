import streamlit as st
import numpy as np
import math

# Define the CDF function using a numerical approximation (error function)
def cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S * cdf(d1) - K * np.exp(-r * T) * cdf(d2)
    else:
        price = K * np.exp(-r * T) * cdf(-d2) - S * cdf(-d1)
    return price

def binomial_tree(S, K, T, r, sigma, N=100, option_type='call'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)
    
    prices = np.zeros((N+1, N+1))
    prices[0, 0] = S
    
    for i in range(1, N+1):
        prices[i, 0] = prices[i-1, 0] * u
        for j in range(1, i+1):
            prices[i, j] = prices[i-1, j-1] * d
    
    option = np.zeros((N+1, N+1))
    
    for j in range(N+1):
        if option_type == 'call':
            option[N, j] = max(0, prices[N, j] - K)
        else:
            option[N, j] = max(0, K - prices[N, j])
    
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            option[i, j] = np.exp(-r * dt) * (q * option[i+1, j] + (1 - q) * option[i+1, j+1])
    
    return option[0, 0]

def monte_carlo(S, K, T, r, sigma, simulations=10000, option_type='call'):
    np.random.seed(0)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    if option_type == 'call':
        payoff = np.maximum(0, ST - K)
    else:
        payoff = np.maximum(0, K - ST)
    
    price = np.exp(-r * T) * np.mean(payoff)
    return price

st.title('Option Pricing Models')

model = st.sidebar.selectbox('Select Model', ('Black-Scholes', 'Binomial Tree', 'Monte Carlo'))

S = st.number_input('Current Stock Price', min_value=1.0)
K = st.number_input('Strike Price', min_value=1.0)
T = st.number_input('Time to Expiration (years)', min_value=0.01)
r = st.number_input('Risk-Free Rate', min_value=0.0, max_value=1.0, step=0.01)
sigma = st.number_input('Volatility (σ)', min_value=0.01, max_value=1.0, step=0.01)
option_type = st.sidebar.selectbox('Option Type', ('call', 'put'))

if model == 'Black-Scholes':
    price = black_scholes(S, K, T, r, sigma, option_type)
elif model == 'Binomial Tree':
    N = st.number_input('Steps', min_value=1, step=1, value=100)
    price = binomial_tree(S, K, T, r, sigma, N, option_type)
else:
    simulations = st.number_input('Simulations', min_value=1000, step=1000, value=10000)
    price = monte_carlo(S, K, T, r, sigma, simulations, option_type)

st.write(f'The {option_type} option price using the {model} model is: ${price:.2f}')

def generate_option_chain(S, T, r, sigma, model, option_type='call', strikes=10):
    strikes_range = np.linspace(S * 0.8, S * 1.2, strikes)
    chain = []
    
    for K in strikes_range:
        if model == 'Black-Scholes':
            price = black_scholes(S, K, T, r, sigma, option_type)
        elif model == 'Binomial Tree':
            N = 100
            price = binomial_tree(S, K, T, r, sigma, N, option_type)
        else:
            simulations = 10000
            price = monte_carlo(S, K, T, r, sigma, simulations, option_type)
        chain.append((K, price))
    
    return chain

if st.button('Generate Option Chain'):
    chain = generate_option_chain(S, T, r, sigma, model, option_type)
    st.write('Option Chain:')
    for strike, price in chain:
        st.write(f'Strike: {strike:.2f}, Price: {price:.2f}')
