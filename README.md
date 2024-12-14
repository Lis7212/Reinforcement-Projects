# Energy-Efficient HVAC Control System

This Streamlit-based application demonstrates how a Reinforcement Learning (RL) agent can optimize energy consumption in HVAC systems while maintaining comfortable indoor conditions. The project allows users to simulate an environment, configure RL parameters, and visualize the performance of the RL agent.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This application simulates an energy-efficient HVAC control system using a mock RL agent. It focuses on balancing energy efficiency and indoor comfort. Users can:

- Configure temperature and humidity ranges.
- Define energy consumption constraints.
- Set parameters for RL training.
- Visualize results using interactive charts.

---

## Features

- **Customizable Environment Simulation**: Adjust temperature, humidity, and energy constraints.
- **Reinforcement Learning Agent Settings**: Configure learning rate, exploration rate, discount factor, and training episodes.
- **Real-Time Data Visualization**:
  - Comfort score analysis.
  - Energy consumption trends.
  - Combined performance metrics.
- **Interactive Sidebar**: Easily adjust parameters and settings.
- **Summary Statistics**: View average, minimum, and maximum performance metrics.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Interactive web application framework.
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For visualization.

---

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/energy-efficient-hvac.git
   cd energy-efficient-hvac
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Launch the App**:
   Run the Streamlit app using the command provided above.

2. **Input Parameters**:
   Use the sidebar to set:
   - Desired temperature and humidity ranges.
   - Maximum energy consumption.
   - RL agent settings (learning rate, gamma, epsilon, episodes).

3. **Simulate Environment**:
   View the simulated environment data in the main section.

4. **Train the RL Agent**:
   Click the "Train RL Agent" button to start training the mock RL agent.

5. **Analyze Results**:
   Visualize comfort scores and energy consumption metrics.

---

## How It Works

1. **Environment Simulation**:
   - Generates synthetic data for temperature, humidity, and energy consumption based on user-defined constraints.

2. **RL Agent Training**:
   - Uses a mock RL training loop to generate random performance metrics (comfort scores and energy consumption).

3. **Visualization**:
   - Line charts display the trends for comfort scores and energy consumption over episodes.
   - Summary statistics provide insights into performance metrics.

---



## Future Enhancements

- **Integration with Real RL Models**: Replace mock data with an actual RL agent.
- **Dynamic Reward Function**: Use real-time feedback from the environment for agent optimization.
- **Energy Usage Prediction**: Implement ML models to predict future energy usage.
- **Deployment**: Host the app on a cloud platform like Heroku or AWS.

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a pull request.

---



