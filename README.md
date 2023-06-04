# Sleep-Stage-Classification
Python Streamlit program to classify different sleep stages during a person's sleep

The provided code is a Python script that implements a basic sleep stage analysis and visualization application using the Streamlit framework. The purpose of the application is to analyze and classify sleep stages based on polysomnography (PSG) data, which is typically obtained through electroencephalography (EEG) or electromyography (EMG) recordings.

Here's a breakdown of what the code does and its key components:

Libraries: The code imports several libraries:

pyedflib: A library for reading EDF (European Data Format) files commonly used for PSG data.
numpy: A library for numerical operations and array manipulation.
matplotlib: A library for data visualization, specifically for creating plots.
scipy.signal: A module from the SciPy library that provides various signal processing functions.
Data Preprocessing:

The preprocess_data function applies signal processing and filtering operations to the raw PSG data. In the provided code, a high-pass Butterworth filter is applied to remove low-frequency noise.
The plot_signals function visualizes the raw and filtered signals for each channel of the PSG data.
Sleep Stage Classification:

The main focus of the provided code is on visualizing the sleep stages. It does not explicitly perform automated sleep stage classification using machine learning techniques. Instead, it relies on annotations or labels that are present in the EDF file. These annotations indicate the sleep stages recorded during the PSG study.
The sleep stages are visualized using a simple line plot in the plot_sleep_stages function. Each sleep stage is represented as a number: 0 for deep sleep, 1 for light sleep, and 2 for REM sleep.
The x-axis of the plot represents time in seconds, with tick labels indicating the corresponding time points.
Streamlit App:

The code utilizes the Streamlit framework to create a web-based application for analyzing and visualizing the sleep stages.
The main function sets up the Streamlit app, defines the user interface, and handles the file upload of the EDF data.
When a valid EDF file is uploaded, the app reads the data, performs preprocessing, and displays the raw and filtered signals as well as the sleep stage plot.
Overall, the code provides a basic foundation for visualizing sleep stages based on PSG data. However, it does not include advanced machine learning techniques for automated sleep stage classification. It assumes that the sleep stages are already annotated or labeled in the provided EDF file. The code can be extended and enhanced with additional machine learning algorithms or sleep stage classification models to automate the classification process based on PSG data.
