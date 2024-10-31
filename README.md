# Nimbus: Your Cloud Companion

## Overview

Nimbus is an AI-powered chatbot designed to assist users with questions and information related to cloud computing. Built on the **GPT-Neo** model, Nimbus leverages advanced natural language processing (NLP) capabilities to provide informative and engaging responses. Whether you're looking for details about cloud services, technologies, or best practices, Nimbus is here to help!

## Features

- **Conversational Interface**: Engage in natural conversations about cloud computing topics.
- **Information Retrieval**: Get answers to questions about various cloud services and providers.
- **Customizable Responses**: Nimbus can adapt its responses based on user input and context.
- **User-Friendly Design**: A clean and intuitive interface for easy interaction.

## Technology Stack

### GPT-Neo

Nimbus is powered by **GPT-Neo**, an open-source language model developed by EleutherAI. GPT-Neo is designed to generate human-like text based on the input it receives. Key features of GPT-Neo include:

- **Architecture**: Similar to GPT-2, but with enhancements such as local attention in every other layer.
- **Training Data**: Trained on the Pile dataset, a large-scale dataset designed for language modeling tasks.
- **Flexibility**: Being open-source, GPT-Neo allows developers to customize and fine-tune the model for specific applications.

#### Key Specifications of GPT-Neo:
- **Model Size**: Available in various sizes (e.g., 1.3 billion parameters).
- **Max Position Embeddings**: 2048 tokens.
- **Attention Mechanism**: Local attention with a window size of 256 tokens.

For more information on GPT-Neo, refer to the [Hugging Face documentation](https://huggingface.co/docs/transformers/v4.13.0/en/model_doc/gpt_neo).

## Installation

To run Nimbus locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Nimbus.git
   cd Nimbus
(optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install streamlit transformers torch

streamlit run main.py
