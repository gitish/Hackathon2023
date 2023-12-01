import numpy as np

def generate_synthetic_data(num_samples=1000, num_features=5):
    # Generating synthetic data for house prices
    np.random.seed(42)  # Set seed for reproducibility
    
    # Generating features (X)
    features = np.random.rand(num_samples, num_features)  # Random features
    
    # Generating synthetic prices (target variable - y)
    # Assuming a simple relationship between features and prices
    true_weights = np.random.rand(num_features) * 10  # Random weights for features
    true_intercept = np.random.rand() * 10  # Random intercept
    
    prices = np.dot(features, true_weights) + true_intercept + np.random.randn(num_samples) * 2.5  # Adding noise
    
    return features, prices

# Generate synthetic data
synthetic_features, synthetic_prices = generate_synthetic_data()

# Displaying the shapes of the generated data
print("Synthetic Features shape:", synthetic_features.shape)
print("Synthetic Prices shape:", synthetic_prices.shape)
