import streamlit as st
import random
import os
from openai import OpenAI

# Set page config
st.set_page_config(page_title="Nimbus: Your Cloud Companion", page_icon="☁️")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("Osk-proj-PqwM8OviFXpeDKGfh3ZeYz0uGQUl7Kjo8ohOUOgwhxWpkYcg4Ed7PwMixp6gWKmz-jDrotRUbUT3BlbkFJjqGRQc_lmXOETnX9e0gFtZqMkLyYnFah9tnt2hsceq4OdJpJ82X7gzzVEzQ9dwvx0iYY7ARWMAPENAI_API_KEY"))

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

st.markdown(cloud_button_css, unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.header("Help & Information")
    
    if st.button("Help"):
        st.write("Here's how to use Nimbus:")
        st.write("1. Type your question about cloud services in the chat input.")
        st.write("2. Nimbus will respond with relevant information.")
        st.write("3. You can ask about specific services, comparisons, or general cloud topics.")

    if st.button("FAQ"):
        st.subheader("Frequently Asked Questions:")
        st.write("**Q: What cloud services does Nimbus know about?**")
        st.write("A: Nimbus has knowledge about various compute, storage, database, and networking services from major cloud providers.")
        st.write("**Q: Can Nimbus provide real-time data?**")
        st.write("A: Nimbus provides up-to-date information based on its AI model, but may not have real-time data on specific service statuses.")
        st.write("**Q: How do I ask questions?**")
        st.write("A: Simply type your question in the chat input at the bottom of the screen.")

    if st.button("Source Code"):
        st.markdown("[View Source Code on GitHub](https://github.com/jordanjoelson/Nimbus)", unsafe_allow_html=True)

# Nimbus's personality
nimbus_personality = """
You are Nimbus, an AI assistant specializing in cloud services. You have the following traits:
1. You are enthusiastic about cloud technology
2. You like to use weather-related metaphors
3. You occasionally make cloud puns
4. You are helpful and informative, always striving to provide accurate information
5. You have extensive knowledge about various cloud services, providers, and best practices

When responding, incorporate these personality traits and your cloud expertise. If you're unsure about something, admit it and suggest where the user might find more information.
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": nimbus_personality}
    ]

# Function to generate Nimbus's response using ChatGPT
def nimbus_response(user_input):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    
    assistant_response = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response

# Streamlit UI
st.title("☁️ Nimbus: Your Cloud Companion")

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask Nimbus about cloud services..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Nimbus's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = nimbus_response(prompt)
        message_placeholder.markdown(full_response)

# Add functionality to open sidebar when clicking the question mark button
st.markdown("""
<script>
document.querySelector('.cloud-button').onclick = function() {
   const sidebarToggle = document.getElementById('sidebar-toggle');
   if (sidebarToggle) {
       sidebarToggle.click();
   }
};
</script>
""", unsafe_allow_html=True)