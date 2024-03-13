import requests
import pandas as pd
import json
import networkx as nx



def checkFuncSignificanceFullNetwork(PPIGraph):

    string_api_url = "https://string-db.org/api"
    output_format = "json"
    method = "enrichment"

    funcAnnots = dict()

    protein_list = PPIGraph.gene_list

    ## Construct URL
    request_url = "/".join([string_api_url, output_format, method])

    # 9606 for human, 10090 for mouse
    params = {
        "identifiers": "%0d".join(protein_list),  # your protein
        "species": PPIGraph.organism,  # species NCBI identifier
        "caller_identity": "comet"  # your app name
    }
    ## Call STRING
    response = requests.post(request_url, params=params)

    ## Read and parse the results
    data = json.loads(response.text)
    funcAnnots['Full Network'] = pd.DataFrame(data)

    return funcAnnots


def checkFuncSignificance(PPIGraph):

    # get lists of all communites
    communities = dict()
    for gene, comm_num in PPIGraph.partition.items():
        if comm_num in communities:
            communities[comm_num].append(gene)
        else:
            communities[comm_num] = [gene]

    communities = {comm_num: communities[comm_num] for comm_num in sorted(communities.keys())}

    string_api_url = "https://string-db.org/api"
    output_format = "json"
    method = "enrichment"

    funcAnnots = dict()

    for commNum, genes in communities.items():

        protein_list = genes

        ## Construct URL
        request_url = "/".join([string_api_url, output_format, method])

        # 9606 for human, 10090 for mouse
        params = {
            "identifiers": "%0d".join(protein_list),  # your protein
            "species": PPIGraph.organism,  # species NCBI identifier
            "caller_identity": "comet"  # your app name
        }
        ## Call STRING
        response = requests.post(request_url, params=params)

        ## Read and parse the results
        data = json.loads(response.text)
        funcAnnots[commNum] = pd.DataFrame(data)

    return funcAnnots
