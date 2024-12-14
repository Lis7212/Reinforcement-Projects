import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Page configuration
st.set_page_config(page_title="Energy-Efficient HVAC Control", layout="wide")
st.title("Energy-Efficient HVAC Control System")
st.markdown("""This application uses a Reinforcement Learning (RL) agent to optimize energy consumption 
in HVAC systems while maintaining comfortable indoor conditions.""")

# Sidebar for user input
st.sidebar.header("User Input Parameters")

# Input parameters
temperature_range = st.sidebar.slider("Desired Temperature Range (°C):", 18, 30, (22, 25))
humidity_range = st.sidebar.slider("Desired Humidity Range (%):", 30, 70, (40, 60))
max_energy = st.sidebar.number_input("Maximum Energy Consumption (kW):", value=5.0, min_value=0.1, step=0.1)

time_steps = st.sidebar.number_input("Number of Time Steps (Minutes):", value=60, min_value=10, step=10)
st.sidebar.markdown("---")

st.sidebar.markdown("### RL Agent Settings")
learning_rate = st.sidebar.number_input("Learning Rate:", value=0.01, min_value=0.001, step=0.001, format="%.3f")
gamma = st.sidebar.number_input("Discount Factor (Gamma):", value=0.95, min_value=0.1, max_value=1.0, step=0.05)
epsilon = st.sidebar.number_input("Exploration Rate (Epsilon):", value=0.1, min_value=0.01, max_value=1.0, step=0.01)
episodes = st.sidebar.number_input("Number of Training Episodes:", value=100, min_value=10, step=10)

st.sidebar.markdown("---")
st.sidebar.markdown("### Visualization Settings")
show_comfort_chart = st.sidebar.checkbox("Show Comfort Score Chart", value=True)
show_energy_chart = st.sidebar.checkbox("Show Energy Consumption Chart", value=True)

# Placeholder for real-time RL performance visualization
performance_placeholder = st.empty()
comfort_placeholder = st.empty()
energy_placeholder = st.empty()

# Placeholder for data
rl_performance_data = []
comfort_scores = []
energy_consumption_data = []

@st.cache_data
def simulate_environment(time_steps, temperature_range, humidity_range, max_energy):
    """Simulate environment data for the HVAC system."""
    time_series = np.arange(1, time_steps + 1)
    temperatures = np.random.uniform(temperature_range[0], temperature_range[1], size=time_steps)
    humidities = np.random.uniform(humidity_range[0], humidity_range[1], size=time_steps)
    energy_usage = np.random.uniform(0.5, max_energy, size=time_steps)
    return pd.DataFrame({
        "Time Step": time_series,
        "Temperature (°C)": temperatures,
        "Humidity (%)": humidities,
        "Energy Usage (kW)": energy_usage
    })

def train_rl_agent(temperature_range, humidity_range, max_energy, learning_rate, gamma, epsilon, episodes):
    """Mock function to simulate RL agent training."""
    global rl_performance_data, comfort_scores, energy_consumption_data
    rl_performance_data = []
    comfort_scores = []
    energy_consumption_data = []

    for episode in range(episodes):
        comfort_score = np.random.uniform(0.7, 1.0)  # Random comfort score
        energy_consumed = np.random.uniform(0.5, max_energy)  # Random energy consumption
        comfort_scores.append(comfort_score)
        energy_consumption_data.append(energy_consumed)
        rl_performance_data.append((comfort_score, energy_consumed))

# Simulate environment
data = simulate_environment(time_steps, temperature_range, humidity_range, max_energy)

st.write("### Simulated Environment Data")
st.dataframe(data)

# Run RL agent training
if st.button("Train RL Agent"):
    st.write("### Training RL Agent...")
    train_rl_agent(temperature_range, humidity_range, max_energy, learning_rate, gamma, epsilon, episodes)
    st.success("Training completed!")

# Visualization of energy consumption and comfort score
if len(energy_consumption_data) > 0:
    st.write("### Energy Consumption and Comfort Score Analysis")
    if show_comfort_chart:
        st.write("#### Chart 1: Comfort Score Over Episodes")
        st.markdown("This chart displays the comfort score achieved by the RL agent during each episode. A higher score indicates better maintenance of comfortable indoor conditions.")
        st.line_chart(pd.DataFrame({"Comfort Score": comfort_scores}))

    if show_energy_chart:
        st.write("#### Chart 2: Energy Consumption Over Episodes")
        st.markdown("This chart illustrates the energy consumption by the HVAC system during each episode. Lower energy consumption indicates more efficient operation.")
        st.line_chart(pd.DataFrame({"Energy Consumed (kW)": energy_consumption_data}))

    st.write("#### Chart 3: Combined Performance Metrics")
    st.markdown("This chart provides a combined view of both comfort scores and energy consumption metrics, helping to visualize the trade-offs between maintaining comfort and minimizing energy usage.")
    st.line_chart(pd.DataFrame({
        "Comfort Score": comfort_scores,
        "Energy Consumed (kW)": energy_consumption_data
    }))

    # Summary statistics
    st.write("#### Summary Statistics")
    st.write(pd.DataFrame({
        "Metric": ["Average Comfort Score", "Average Energy Consumed (kW)", "Minimum Energy Consumed (kW)", "Maximum Energy Consumed (kW)"],
        "Value": [
            np.mean(comfort_scores),
            np.mean(energy_consumption_data),
            np.min(energy_consumption_data),
            np.max(energy_consumption_data)
        ]
    }))
