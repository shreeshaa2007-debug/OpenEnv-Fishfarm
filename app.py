import streamlit as st
from env.environment import FishFarmEnv
from agent.baseline import policy

st.title("Fish Farm Simulator")

env = FishFarmEnv()
state = env.reset()

if st.button("Run Simulation"):
    done = False
    while not done:
        action = policy(state)
        state, reward, done, _ = env.step(action)
        st.write(state)
        st.write("Reward:", reward)
