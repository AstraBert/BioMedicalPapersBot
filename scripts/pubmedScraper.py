from Bio import Entrez

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
    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, rettype="medline", retmode="text")
    records = handle.read()
    handle.close()
    return records

def respond_to_query(query,address,max_results=10):

    # Perform the PubMed search
    pubmed_ids = search_pubmed(query, max_results,address)

    # Fetch details for the retrieved PubMed IDs
    pubmed_details = fetch_pubmed_details(pubmed_ids,address)

    pubmed_split=pubmed_details.split("\n")
    str_container=[]
    counter=-1
    for i in pubmed_split:
        str_container.append({})
        counter+=1
        if i.startswith("TI"):
            str_container[counter].update({"Title (sometimes not complete)": i.replace('TI  - ', '')})
        if i.startswith("AU  - "):
            str_container[counter].update({"Author": i.replace('AU  - ', '')})
        if i.startswith("PHST") and i.endswith("[pubmed]"):
            str_container[counter].update({"Published on PubMed on": i.replace('PHST- ', '').replace('[pubmed]','')})
        if i.endswith("[doi]") and i.startswith("AID - "):
            str_container[counter].update({"doi": f"https://doi.org/{i[6:len(i)-5]}\n"})
    results=[]
    for j in str_container:
        ls=[f"{key}: {j[key]}\n" for key in list(j.keys())]
        results.append("".join(ls))
        remove_blankets(results)
    defstr="".join(results)
    return defstr