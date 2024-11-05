import gradio as gr
from pubmedScraper import respond_to_query
import time


def respond(
    message,
    history,
    email,
    max_res
):
    response = respond_to_query(message, email, max_res)
    r = ''
    for char in response:
        r+=char
        time.sleep(0.001)
        yield r

demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="your.email@example.com", label="e-mail address (optional)"),
        gr.Slider(minimum=1, maximum=15, value=5, step=1, label="Maximum number of results"),
    ],
    title="""<h1 align='center'>BioMedicalPapersBot</h1>
<h2 align='center'>Scrape PubMed faster, boost your research!🔬</h2>
<h3 align='center'>[<a href="https://github.com/AstraBert/BioMedicalPapersBot">GitHub⭐</a>] [<a href="https://github.com/sponsors/AstraBert">Funding</a>]</h3>"""
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)