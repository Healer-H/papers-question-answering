from __future__ import annotations

import chainlit as cl


@cl.on_chat_start
async def start():
    markdown_content = """
    # Welcome to the Research Chatbot! 📘✨

    ### Our chatbot is designed to assist researchers and students by providing a range of tools to enhance your understanding and interaction with academic papers, especially in the fields of AI, NLP, and LLM. Here's what you can do with our chatbot:

    ### 🔍 Question Answering
    Upload your research papers, and ask any question. Our chatbot will provide precise answers by understanding the context embedded within your documents.

    ### 📄 Summarization
    Get concise summaries of lengthy papers to grasp key concepts and findings quickly, saving you time and effort.

    ### 🔄 Flow Capture and Explanation
    Visualize the argumentative or logical flow of the papers to better understand the progression and structure of complex ideas.

    ### 🔗 Search and Recommendation
    Use our advanced semantic search to find related papers or let our chatbot recommend articles that align with your current research interests.

    ### 📚 Interactive Explanations
    Access interactive content like tutorials and diagrams to get clear explanations of sophisticated concepts.

    ### 📝 Shared Annotations and Collaboration Tools
    Annotate papers, save your notes, and easily share these with peers or collaborators directly through the interface.

    ### 💬 Discussion Threads
    Start or join discussion threads linked to specific segments of a paper to engage with the academic community and broaden your understanding.

    To begin, simply upload a paper or type in your question or command into the chat. You can also select from the available functionalities displayed as buttons on your screen.

    Let's dive into your research with an enhanced, supportive experience! 🚀
    """

    markdown_chunks = markdown_content.split('###')
    msg = cl.Message(
        content='',
        author='Bot',
    )

    for chunk in markdown_chunks:
        await msg.stream_token(chunk)

    await msg.send()


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    # Send a response back to the user ...
    response = 'Here is the response to your message: ' + message.content
    author = 'Bot'
    await cl.Message(
        content=response,
        author=author,
        elements=[],
        actions=[],
    ).send()
