from pyedflib import highlevel
from scipy.stats import entropy
from scipy.signal import firwin, filtfilt
import numpy as np

def single_import_edf(path):
    signals, signal_headers, header = highlevel.read_edf(path)
    n_channels = len(signals)
    n_samples = len(signals[0])
    sample_rate = signal_headers[0]['sample_rate']
    return signals,n_channels,n_samples,sample_rate

def import_edf(paths):
    all_signals = []
    for path in paths:
        print(path)
        signals, signal_headers, header = highlevel.read_edf(path)
        all_signals.append(signals)
    return all_signals

def avg_signal(signals):
    result_signal = []
    for i in range(len(signals)):
        n_samples = len(signals[i][0])
        n_channels = len(signals[i])
        averaged_signal = []
        all_channel_data = np.zeros((n_channels, n_samples))
        for j in range(len(signals[i])):
            all_channel_data[j, :] = signals[i][j]
        averaged_signal = np.mean(all_channel_data, axis=0)
        result_signal.extend(averaged_signal)
    return result_signal

def avg_signal_reff(signals,n_channels,n_samples):
    all_channel_data = np.zeros((n_channels, n_samples))
    for i in range(n_channels):
        all_channel_data[i, :] = signals[i]
    averaged_signal = np.mean(all_channel_data, axis=0)
    return averaged_signal 

def filtering(data,fs , lowcut=0.5, highcut=40.0):
    lowcut = lowcut  # Hz (desired lower cutoff frequency)
    highcut = highcut  # Hz (desired upper cutoff frequency)
    num_taps = 101
    fir_filter = firwin(num_taps, highcut, pass_zero=True,scale=False, fs=fs, window='hamming')
    filtered_signal = filtfilt(fir_filter , 1.0, data)

    return filtered_signal

def shannon_entropy(signal_segment):
    if len(signal_segment) == 0:
        return 0
    unique_values, counts = np.unique(signal_segment, return_counts=True)
    probabilities = counts / len(signal_segment)
    probabilities = probabilities + 1e-10
    entropy_value = entropy(probabilities, base=2)
    
    return entropy_value

def statistical_features(signal_segment):
    variance = np.var(signal_segment)
    min = np.min(signal_segment)
    max = np.max(signal_segment)      
    std = np.std(signal_segment)
    sumofsquares = np.sum(np.square(signal_segment))    
    
    return variance, std, sumofsquares , min, max

def feature_extraction(segment_duration,signal,sample_rate):
    entropy_values          = []
    variance_values         = []
    std_values              = []
    sumofsquares_values     = []
    min_values              = []
    max_values              = []
    
    segment_duration = segment_duration
    num_segments = int(np.ceil(len(signal) / (sample_rate * segment_duration)))

    for i in range(num_segments):
        start_idx = i * int(sample_rate * segment_duration)
        end_idx = (i + 1) * int(sample_rate * segment_duration)
        signal_segment = signal[start_idx:end_idx]
        
        entropy = shannon_entropy(signal_segment)
        variance, std, sumofsquares , min, max = statistical_features(signal_segment)

        entropy_values.append(entropy)
        variance_values.append(variance)
        std_values.append(std)
        sumofsquares_values.append(sumofsquares)
        min_values.append(min)
        max_values.append(max)
    
    return entropy_values,variance_values,std_values,sumofsquares_values,min_values,max_values

def knn_interval(training_intervals_A, training_intervals_B, query_point, k=5):
    distances_A = np.abs(training_intervals_A - query_point)
    distances_B = np.abs(training_intervals_B - query_point)
    
    all_distances = np.concatenate([distances_A, distances_B])
    all_labels = np.concatenate([['Normal'] * len(distances_A), ['Pre-seizure'] * len(distances_B)])

    nearest_neighbors_indices = np.argsort(all_distances)[:k]
    nearest_neighbors_labels = all_labels[nearest_neighbors_indices]
    unique_labels, counts = np.unique(nearest_neighbors_labels, return_counts=True)
    most_common_label = unique_labels[np.argmax(counts)]
    if(most_common_label == 'Normal'):
        return 0
    if(most_common_label == 'Pre-seizure'):
        return 1

def classification(nb,np,feature):
    predicted = []
    for i in range(len(feature)):
        predicted_label = knn_interval(nb, np, feature[i], k=3) 
        predicted.append(predicted_label)
    
    return predicted