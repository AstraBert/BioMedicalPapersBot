from Bio import Entrez
import xml.etree.ElementTree as ET

def remove_blankets(ls):
    for i in range(len(ls)):
        if i<len(ls):
            if ls[i]=="" or ls[i]==" ":
                ls.remove(ls[i])
            else:
                pass
        else:
            pass

def search_pubmed(query, max_results, address):
    Entrez.email = address  # Replace with your email
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def fetch_pubmed_details(pubmed_ids, address):
    Entrez.email = address  # Replace with your email
    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, rettype="medline", retmode="xml")
    records = handle.read()
    handle.close()
    recs = records.decode("utf-8")
    f = open("articles.xml", "w")
    f.write(recs)
    f.close()
    return "articles.xml"

def fetch_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    articles = {}

    # Iterate over each article and extract title, authors, and DOI
    for article in root.findall('PubmedArticle'):
        # Extract the article title
        title = article.find('.//ArticleTitle').text if article.find('.//ArticleTitle') is not None else "No title"

        # Extract the authors
        authors = []
        for author in article.findall('.//Author'):
            last_name = author.find('LastName').text if author.find('LastName') is not None else ""
            fore_name = author.find('ForeName').text if author.find('ForeName') is not None else ""
            authors.append(f"{fore_name} {last_name}".strip())

        # Extract the DOI
        doi = None
        for elocation_id in article.findall('.//ELocationID'):
            if elocation_id.get('EIdType') == 'doi':
                doi = elocation_id.text
                break
        pub_date = article.find('.//PubDate')
        if pub_date is not None:
            year = pub_date.find('Year').text if pub_date.find('Year') is not None else ""
            month = pub_date.find('Month').text if pub_date.find('Month') is not None else ""
            day = pub_date.find('Day').text if pub_date.find('Day') is not None else ""
            publication_date = f"{year}-{month}-{day}".strip("-")
        else:
            publication_date = "No publication date"
        articles.update({doi: {"Title": title, "Authors": authors, "PubDate": publication_date}})
    return articles

def respond_to_query(query,address,max_results=10):
    pubmed_ids = search_pubmed(query, max_results,address)
    pubmed_details = fetch_pubmed_details(pubmed_ids,address)
    articles = fetch_xml(pubmed_details)
    final_res = ""
    for doi in articles:
        auths = [f"- <kbd> {author} </kbd>" for author in articles[doi]["Authors"]] if len(articles[doi]["Authors"]) > 0 else ["- <kbd> No authors listed </kbd>",""]
        authorrs = '\n'.join(auths)
        res = f"**Title**: {articles[doi]['Title']}\n**Publication date**: {articles[doi]['PubDate']}\n<details>\n\t<summary><b>Authors</b></summary>\n\n{authorrs}\n\n</details>\n\n**DOI**: [{doi}🔗](https://doi.org/{doi}) \n\n-----------------------\n"
        final_res+=res
    return final_res

# if __name__ == "__main__":
#     pub_ids = search_pubmed("Drosophila evolution over space and time", 5, "astraberte9@gmail.com")
#     recs = fetch_pubmed_details(pub_ids, "astraberte9@gmail.com")
#     r = recs.decode("utf-8")
#     f = open("articles.xml", "w")
#     f.write(r)
#     f.close()
