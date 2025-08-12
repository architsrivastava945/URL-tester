import re

# Extract features from a single URL
def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_https'] = int('https' in url.lower())
    features['num_dots'] = url.count('.')
    features['has_ip'] = int(bool(re.search(r'[0-9]+(?:\.[0-9]+){3}', url)))
    features['num_special_chars'] = sum(url.count(c) for c in ['@', '=', '&', '%', '-', '_'])
    return features

# Convert list of URLs to feature rows
def extract_features_from_series(url_series):
    return [extract_features(url) for url in url_series]
