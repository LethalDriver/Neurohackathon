import brainaccess_board as bb
import pandas as pd
import neurokit2 as nk
import numpy as np


def get_and_label_data(db):
    channels = [
        "time",
        "F3",
        "F4",
        "C3",
        "C4",
        "P3",
        "P4",
        "O1",
        "O2",
        "Accel_x",
        "Accel_y",
        "Accel_z",
        "Sample",
        "Streaming",
        "Battery",
    ]
    data = db.get_mne()
    devices = list(data.keys())
    device = devices[0]
    data = data[device].get_data()
    samples_labeled = {
        channel_name: samples for samples, channel_name in zip(data, channels)
    }
    df = pd.DataFrame(samples_labeled)
    return df


def preprocess_data(df):
    eeg_channels = ["F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2"]
    preprocessed_signals = pd.DataFrame()
    for channel in eeg_channels:
        signal = df[channel].values
        filtered_signal = nk.signal_filter(
            signal, lowcut=1, highcut=50, sampling_rate=250, method="butterworth"
        )
        preprocessed_signals[channel] = filtered_signal
    return preprocessed_signals


def calculate_psd_for_bands(preprocessed_signals, n_samples):
    bands = {
        "delta": (0.5, 4),
        "theta": (4, 8),
        "alpha": (8, 12),
        "beta": (12, 30),
        "gamma": (30, 45),
    }
    brainwave_features = pd.DataFrame()

    for channel, signal in preprocessed_signals.items():
        # Select the last n_samples from the signal
        signal_window = signal[-n_samples:]

        # Compute PSD using NeuroKit2
        psd = nk.signal_psd(signal_window, sampling_rate=250, method="welch")

        # Extract Frequency and Power columns
        freqs = psd["Frequency"].values
        power = psd["Power"].values

        # Compute band powers
        band_powers = {
            band: np.trapezoid(
                power[(freqs >= low) & (freqs <= high)],
                x=freqs[(freqs >= low) & (freqs <= high)],
            )
            for band, (low, high) in bands.items()
        }

        # Add the band powers for the current channel to the DataFrame
        channel_features = pd.DataFrame(band_powers, index=[channel])
        brainwave_features = pd.concat([brainwave_features, channel_features])

    return brainwave_features

db, status = bb.db_connect()
if status:
    labeled_data = get_and_label_data(db)
    preprocessed_data = preprocess_data(labeled_data)
    features = calculate_psd_for_bands(preprocessed_data)
    print(features)
