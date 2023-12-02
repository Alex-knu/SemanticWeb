import requests

def upload_data():
    # upload ttl to the graphdb repository
    # Define the URL of the GraphDB repository
    url = "http://localhost:7200/repositories/first/rdf-graphs/service?graph=http://example.com/mygraph"

    # Define the path to the TTL file
    ttl_file_path = "museums.ttl"

    # Open the TTL file
    with open(ttl_file_path, "rb") as file:
        ttl_file = file.read()

    # Define the headers for the request
    headers = {
        "Content-Type": "application/x-turtle",
    }

    # Send a POST request to the GraphDB repository to import the TTL graph
    response = requests.post(url, headers=headers, data=ttl_file)

    # Check the response
    if response.status_code == 204:
        print("Graph successfully imported.")
    else:
        print(f"Failed to import graph. Status code: {response.status_code}. Response text: {response.text}")


def clear_graph():
    # Construct the URL for the request
    #url = "http://localhost:7200/repositories/first/rdf-graphs/service?default"
    url = "http://localhost:7200/repositories/first/rdf-graphs/service?graph=http://example.com/mygraph"

    # Send the DELETE request
    response = requests.delete(url)

    # Check the response
    if response.status_code == 204:
        print("Graph deleted successfully.")
    else:
        print(f"Failed to delete graph. Status code: {response.status_code}.")


def get_all_museums():
    # Define the URL of the GraphDB repository
    url = "http://localhost:7200/repositories/first"

    # Define the SPARQL query
    query = """
        PREFIX ex: <http://example.org/> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/> 
            
        SELECT ?museum ?museumLabel ?museumType ?region ?np ?address ?geo ?inception ?site
        WHERE {
            GRAPH <http://example.com/mygraph> {
                ?museum a wd:Q33506 ;
                    rdfs:label ?museumLabel ;
                    ex:address ?address ;
                    ex:geo ?geo ;
                    ex:inception ?inception ;
                    ex:np ?np ;
                    ex:region ?region .
                
                OPTIONAL
                {
                    ?museum ex:site ?site ;
                        ex:museumType ?museumType .
                }
            }
        }
        #LIMIT 10
    """

    # Define the parameters for the request
    params = {
        "query": query,
    }

    # Send a GET request to the GraphDB repository to execute the SPARQL query
    response = requests.get(url, params=params)

    # Check the response
    if response.status_code == 200:
        print("Query successfully executed.")
        print("Response:")
        print(response.text)
        #print(len(response.text))
    else:
        print(f"Failed to execute query. Status code: {response.status_code}. Response text: {response.text}")


def get_museum(museum_url):
    # Define the URL of the GraphDB repository
    url = "http://localhost:7200/repositories/first"

    museum_url = "<" + museum_url + ">"

    # Define the SPARQL query
    query = """
        PREFIX ex: <http://example.org/> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/> 

        SELECT ?museumLabel ?museumType ?region ?np ?address ?geo ?inception ?site
        WHERE {
            GRAPH <http://example.com/mygraph> {
                """ + museum_url + """ a wd:Q33506 ;
                    rdfs:label ?museumLabel ;
                    ex:address ?address ;
                    ex:geo ?geo ;
                    ex:inception ?inception ;
                    ex:np ?np ;
                    ex:region ?region .

                OPTIONAL
                {
                    """ + museum_url + """ ex:site ?site ;
                        ex:museumType ?museumType .
                }
            }
        }
        #LIMIT 10
    """

    # Define the parameters for the request
    params = {
        "query": query,
    }

    # Send a GET request to the GraphDB repository to execute the SPARQL query
    response = requests.get(url, params=params)

    # Check the response
    if response.status_code == 200:
        print("Query successfully executed.")
        print("Response:")
        print(response.text)
    else:
        print(f"Failed to execute query. Status code: {response.status_code}. Response text: {response.text}")


#upload_data()
#get_all_museums()
#clear_graph()
#get_museum("http://www.wikidata.org/entity/Q105751941")#http://www.wikidata.org/entity/Q10575194
