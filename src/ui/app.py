import gradio as gr

def chatbot(message, history):
    return f"Response to: {message}"

interface = gr.ChatInterface(fn=chatbot, title="Car Sales RAG Chatbot")

if __name__ == "__main__":
    interface.launch()