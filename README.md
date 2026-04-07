# 🚦 Traffic Signal Control using Reinforcement Learning

This project implements a Reinforcement Learning (RL) based traffic signal control system using the OpenEnv framework.

## 📌 Overview
The environment simulates traffic flow and uses an agent to optimize signal actions in order to minimize congestion and maximize traffic efficiency.

## ⚙️ Features
- Custom traffic environment (`traffic_env.py`)
- Greedy baseline agent
- Step-by-step reward tracking
- Fully Dockerized setup
- Deployable on Hugging Face Spaces

## 🧠 Approach
The agent interacts with the environment by:
- Observing traffic state
- Taking actions (signal changes)
- Receiving rewards based on performance

## 📊 Output
The system logs:
- Step number
- Action taken
- Reward values
- Final score

## 🐳 Docker Support
The project is containerized using Docker for easy deployment.

## 🚀 Deployment
Deployed on Hugging Face Spaces using Docker.

## 📁 Files
- `inference.py` – Main execution script
- `traffic_env.py` – Environment logic
- `tasks.py` – Task definitions
- `grader.py` – Evaluation logic

## ✅ Status
✔ Successfully runs end-to-end  
✔ Produces valid output logs  
✔ Ready for evaluation  
