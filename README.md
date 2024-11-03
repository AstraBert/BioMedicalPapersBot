# BioMedicalPapersBot
A Telegram bot to retrieve the title, doi, authors and publication date of papers on PubMed, starting on general search terms or on specific publication names

## How to activate it
You can pull it from GitHub Docker Container registry:

```bash
docker pull ghcr.io/astrabert/biomedicalpapersbot:latest
docker run -p 7860:7860 ghcr.io/astrabert/biomedicalpapersbot:latest
```

Or you can clone the repository:

```bash
git clone https://github.com/AstraBert/BioMedicalPapersBot
cd BioMedicalPapersBot
```

Create a virtual environment and activate it:

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
```

Install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the application:

```bash
python3 scripts/app.py
```

In both cases, you will find the application on http://localhost:7860

Find a demo [here](https://huggingface.co/spaces/as-cle-bert/BioMedicalPapersBot).

## Description
It is a (bio)python-based Gradio bot that searches PubMed and returns the features of the papers that correspond to the search. 

You can find a snippet code of the functions used to retrieve and parse data from PubMed in [pubmedScraper.py](./scripts/pubmedScraper.py). The workflow is pretty simple:

- `search_pubmed` does the actual webscraping, thanks to the Entrez NCBI module, that remotely connects to online servers and communicate with them: the function returns a list of PubMed IDs
- `fetch_pubmed_details`, thanks to a faster access to paper metadata and data with the IDs from the previous function, retrieves significant information about papers and outputs it in standard text format
- `respond_to_query` outputs the information of interest in a format that is human-readable and message-sendable

You can also find the basic architecture of the python code that is used for the Gradio bot itself. 

Keep in mind that there are several ways to define a python bot: thus, if you find a faster or better implementation for it, feel free to suggest it in the `ISSUE` section.

## Funding

If you found this project useful, please consider to [fund it](https://github.com/sponsors/AstraBert) and make it grow: let's support open-source together!😊

## License and rights of usage

This project is provided under [MIT license](./LICENSE): it will always be open-source and free to use.

If you use this project, please cite the author: [Astra Clelia Bertelli](https://astrabert.vercel.app)