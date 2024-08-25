
# Option Pricing Models Streamlit App

## Overview

This Streamlit app allows users to calculate the theoretical value of options using three popular pricing models: **Black-Scholes**, **Binomial Tree**, and **Monte Carlo Simulation**. The app also generates an option chain based on user-defined parameters.

## Features

- **Black-Scholes Model**: Calculates the price of European call and put options using the Black-Scholes formula.
- **Binomial Tree Model**: Computes the price of American and European options by constructing a binomial tree of possible asset prices.
- **Monte Carlo Simulation**: Estimates the price of options by simulating the random paths of asset prices and averaging the discounted payoffs.
- **Option Chain Generation**: Generates an option chain with varying strike prices and corresponding option values based on the selected model.

## Prerequisites

Ensure you have the following Python libraries installed:

- `streamlit`
- `numpy`
- `scipy`

You can install the required packages using pip:

```bash
pip install streamlit numpy scipy
```

## Usage

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/option-pricing-models.git
cd option-pricing-models
```

### 2. Run the Streamlit App

To start the Streamlit app, navigate to the project directory and run:

```bash
streamlit run app.py
```

### 3. Interact with the App

- **Model Selection**: Choose one of the three models (Black-Scholes, Binomial Tree, Monte Carlo) from the sidebar.
- **Input Parameters**: Enter the required parameters such as current stock price, strike price, time to expiration, risk-free rate, and volatility.
- **Option Type**: Select either a call or put option.
- **Option Chain**: Click the "Generate Option Chain" button to display a table of option prices for different strike prices.

### 4. Example Parameters

Here are some example parameters you can use to test the app:

- **Current Stock Price (S)**: `100`
- **Strike Price (K)**: `100`
- **Time to Expiration (T)**: `1` year
- **Risk-Free Rate (r)**: `0.05`
- **Volatility (σ)**: `0.2`

## Files

- `app.py`: The main script containing the Streamlit app code.
- `README.md`: This file, which provides an overview and instructions for the project.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
