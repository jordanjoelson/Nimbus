import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Nimbus: Your Cloud Companion", page_icon="☁️")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Nimbus's knowledge base
cloud_services = {
    "compute": ["EC2", "Lambda", "Azure VMs", "Google Compute Engine"],
    "storage": ["S3", "Azure Blob Storage", "Google Cloud Storage"],
    "database": ["RDS", "DynamoDB", "Cosmos DB", "Cloud Spanner"],
    "networking": ["VPC", "Azure Virtual Network", "Google VPC"]
}

# Nimbus's personality traits
personality_traits = [
    "enthusiastic about cloud technology",
    "likes to use weather-related metaphors",
    "occasionally makes cloud puns"
]

# Function to generate Nimbus's response
def nimbus_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return f"Hello there! I'm Nimbus, your friendly neighborhood cloud expert. {random.choice(personality_traits.capitalize())}! How can I help you today?"
    
    elif "cloud service" in user_input:
        service_type = random.choice(list(cloud_services.keys()))
        services = ", ".join(cloud_services[service_type])
        return f"Talking about cloud services always makes me feel on cloud nine! 😄 For {service_type}, you might want to look into {services}. Need more info on any of these?"
    
    elif any(service in user_input for service in sum(cloud_services.values(), [])):
        return f"Ah, that service rings a bell! It's like a ray of sunshine through the clouds. ☀️ What specific information are you looking for about it?"
    
    elif "compare" in user_input:
        return "Comparing cloud services is like comparing different types of clouds - each has its own beauty and purpose! What specific aspects would you like to compare?"
    
    else:
        return f"I'm afraid that query is a bit foggy to me. Could you clarify or ask about a specific cloud service? {random.choice(personality_traits.capitalize())}!"

# Streamlit UI
st.title("☁️ Nimbus: Your Cloud Companion")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask Nimbus about cloud services..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Nimbus's response
    response = nimbus_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)