import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Nimbus: Your Cloud Companion", page_icon="☁️")

# Custom CSS for the cloud-shaped button
cloud_button_css = """
<style>
.cloud-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: #4a4a4a;
    cursor: pointer;
    z-index: 9999;
}
.cloud-button::before {
    content: "?";
}
</style>
"""

# Add the custom CSS to the page
st.markdown(cloud_button_css, unsafe_allow_html=True)

# Add the cloud-shaped button
st.markdown("""
<div class="cloud-button" onclick="document.getElementById('sidebar-toggle').click();"></div>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.header("Help & Information")
    
    if st.button("Help & FAQ"):
        st.write("Frequently Asked Questions:")
        st.write("Q: What cloud services does Nimbus know about?")
        st.write("A: Nimbus has knowledge about various compute, storage, database, and networking services from major cloud providers.")
        st.write("Q: Can Nimbus provide real-time data?")
        st.write("A: No, Nimbus provides general information based on its pre-defined knowledge base.")

    if st.button("Source Code"):
        st.code("""
# This is a simplified version of the source code
import streamlit as st
import random

def nimbus_response(user_input):
    # Response generation logic here
    pass

# Streamlit UI
st.title("☁️ Nimbus: Your Cloud Companion")

# Chat interface logic here
        """, language="python")

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
        trait = random.choice(personality_traits)
        return f"Hello there! I'm Nimbus, your friendly neighborhood cloud expert. I'm {trait}! How can I help you today?"
    
    elif "cloud service" in user_input:
        service_type = random.choice(list(cloud_services.keys()))
        services = ", ".join(cloud_services[service_type])
        return f"Talking about cloud services always makes me feel on cloud nine! 😄 For {service_type}, you might want to look into {services}. Need more info on any of these?"
    
    elif any(service in user_input for service in sum(cloud_services.values(), [])):
        return f"Ah, that service rings a bell! It's like a ray of sunshine through the clouds. ☀️ What specific information are you looking for about it?"
    
    elif "compare" in user_input:
        return "Comparing cloud services is like comparing different types of clouds - each has its own beauty and purpose! What specific aspects would you like to compare?"
    
    else:
        trait = random.choice(personality_traits)
        return f"I'm afraid that query is a bit foggy to me. Could you clarify or ask about a specific cloud service? By the way, I {trait}!"

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