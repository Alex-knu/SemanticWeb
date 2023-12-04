import requests
import re

def upload_data():
    # upload ttl to the graphdb repository
    # Define the URL of the GraphDB repository
    url = "http://graphdb:7200/repositories/first/rdf-graphs/service?graph=http://example.com/mygraph"

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
    return response.status_code


def clear_graph():
    # Construct the URL for the request
    #url = "http://graphdb:7200/repositories/first/rdf-graphs/service?default"
    url = "http://graphdb:7200/repositories/first/rdf-graphs/service?graph=http://example.com/mygraph"

    # Send the DELETE request
    response = requests.delete(url)

    # Check the response
    if response.status_code == 204:
        print("Graph deleted successfully.")
    else:
        print(f"Failed to delete graph. Status code: {response.status_code}.")
    return response.status_code


def get_all_museums():
    # Define the URL of the GraphDB repository
    url = "http://graphdb:7200/repositories/first"

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
    if response.status_code != 200:
        print(f"Failed to execute query. Status code: {response.status_code}. Response text: {response.text}")
        return -1
    else:
        print("Query successfully executed.")
        print("Response:")
        lines = response.text.split('\r\n')
        # print('\n\n', lines)
        # print('\n\n', len(lines))

        result = []
        for i in range(1, len(lines) - 1):
            props = lines[i].split(',')
            dict_j = {}
            dict_j['museum_url'] = props[0]
            dict_j['museum'] = props[1]
            dict_j['museum_type'] = props[2]
            dict_j['region'] = props[3]
            dict_j['settlement'] = props[4]
            result.append(dict_j)

        # print(len(result))
        print(result)
        return result


def get_museum(museum_url):
    # Define the URL of the GraphDB repository
    url = "http://graphdb:7200/repositories/first"

    museum_url = "<" + museum_url + ">"

    # Define the SPARQL query
    query = """
        PREFIX ex: <http://example.org/> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX wd: <http://www.wikidata.org/entity/> 

        SELECT (STR(""" + museum_url + """) AS ?museum_url) ?museumLabel ?museumType ?region ?np ?address ?geo ?inception ?site
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
    if response.status_code != 200:
        print(f"Failed to execute query. Status code: {response.status_code}. Response text: {response.text}")
        return -1
    else:
        print("Query successfully executed.")
        print("Response:")
        lines = response.text.split('\r\n')
        props = []
        j = 0
        while j < len(lines[1]):
            if lines[1][j] == '"':
                brack = lines[1].find('"', j + 1)
                props.append(lines[1][j + 1:brack])
                j = brack + 2
                continue
            coma = lines[1].find(',', j)
            if coma != -1:
                props.append(lines[1][j:coma])
                j = coma + 1
            else:
                props.append(lines[1][j:-1])
                j = len(lines[1])
            # print(props[-1])

    dict_j = {}
    dict_j['museum_url'] = props[0]
    dict_j['museum'] = props[1]
    dict_j['museum_type'] = props[2]
    dict_j['region'] = props[3]
    dict_j['settlement'] = props[4]
    dict_j['adress'] = props[5]
    #dict_j['geo'] = props[6]
    dict_j['inception'] = props[7]
    if len(props) == 9:
        dict_j['site'] = props[8]
    else:
        dict_j['site'] = ''

    pattern = r"[-+]?\d*\.\d+|\d+"
    numbers = re.findall(pattern, props[6])
    map = ''
    if len(numbers) == 2:
        lon = float(numbers[0])
        lat = float(numbers[1])
        #print(f"lon: {lon}, lat: {lat}")
        map = f"https://www.google.com/maps?ll={lat},{lon}.531111&q={lat},{lon}&hl=en&t=m&z=11"
        #print(map)
    else:
        print("Not enough numbers found in the string")

    dict_j['geo'] = '(' + str(lon) + ', ' + str(lat) + ')'
    dict_j['map_link'] = map

    print(dict_j)
    return dict_j



#upload_data()
#clear_graph()
#get_museum("http://www.wikidata.org/entity/Q105751941")#http://www.wikidata.org/entity/Q10575194
#response = get_all_museums()
#print(response)
#response = get_museum("http://www.wikidata.org/entity/Q105751941")
#print(response)
