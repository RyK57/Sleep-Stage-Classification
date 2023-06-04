import pyedflib
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import streamlit as st
import tempfile
import os

def preprocess_data(data, fs):
    # Apply signal processing and filtering operations here
    # Example: Apply a high-pass filter
    cutoff = 1  # High-pass filter cutoff frequency (modify as needed)
    b, a = signal.butter(4, cutoff / (fs / 2), 'highpass', analog=False)
    filtered_data = signal.filtfilt(b, a, data, axis=0)
    return filtered_data

def classify_sleep_stages(data):
    # Define threshold values for different sleep stages
    deep_sleep_threshold = 0.5  # Example threshold for deep sleep stage
    light_sleep_threshold = 1.0  # Example threshold for light sleep stage

    sleep_stages = []
    for sample in data:
        if sample < deep_sleep_threshold:
            sleep_stages.append("Deep Sleep")
        elif sample < light_sleep_threshold:
            sleep_stages.append("Light Sleep")
        else:
            sleep_stages.append("REM")

    return sleep_stages

def plot_sleep_stages(sleep_stages, fs):
    time = np.arange(len(sleep_stages)) / fs

    plt.figure(figsize=(24, 6))
    plt.plot(time, sleep_stages)
    plt.title('Sleep Stages')
    plt.xlabel('Time (m)')
    plt.ylabel('Sleep Stage')
    plt.ylim([-0.5, 2.5])  # Set y-axis limits to match the sleep stage labels
    plt.yticks([0, 1, 2], ['Light Sleep', 'Deep Sleep', 'REM'])
    plt.tight_layout()
    st.pyplot(plt.gcf())

def main():
    st.title("Sleep Stage Classification App")
    st.write("-Rithvik Sabnekar")
    st.write("Please wait at least 1 minute for detailed analytical graphs")
    st.markdown(f'<a href="https://drive.google.com/file/d/1TjXY6Ip_W_jfpFTThWZ2DmOIJ1OF99ZH/view?usp=sharing" download>Example Input file (S001R03.edf), source: https://www.physionet.org/content/eegmmidb/1.0.0/</a>', unsafe_allow_html=True)


    # Step 2: Data Upload
    uploaded_file = st.file_uploader("Upload PSG data file (.edf type)", type=["edf"])

    if uploaded_file is not None:
        # Step 3: Data Preprocessing
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_filename = tmp_file.name
            uploaded_file.seek(0)
            tmp_file.write(uploaded_file.read())

            edf_data = pyedflib.EdfReader(tmp_filename)
            num_channels = edf_data.signals_in_file
            channel_names = edf_data.getSignalLabels()
            raw_data = []
            min_length = float('inf')  # Initialize minimum length with a large value
            for channel in range(num_channels):
                channel_data = edf_data.readSignal(channel)
                raw_data.append(channel_data)
                min_length = min(min_length, len(channel_data))

            # Truncate the channels to have the same length (minimum length)
            raw_data = [channel[:min_length] for channel in raw_data]

            raw_data = np.array(raw_data).T  # Transpose to have channels in columns
            fs = edf_data.samplefrequency(0)  # Get the sampling frequency from the first channel
            filtered_data = preprocess_data(raw_data, fs)

        # Step 4: Sleep Stage Classification
        sleep_stages = classify_sleep_stages(filtered_data[:, 0])  # Classify sleep stages using the first channel

        # Step 5: Visualizations
        plot_sleep_stages(sleep_stages, fs)

        # Close the EDF file
        edf_data.close()

        # Delete the temporary file
        os.remove(tmp_filename)

if __name__ == '__main__':
    main()
