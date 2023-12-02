#wikidata request to ttl

import requests
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, XSD
from rdflib.namespace import DC, FOAF

# Define the SPARQL query
query = """
SELECT ?museum ?museumLabel ?npLabel ?regionLabel ?museumTypeLabel ?inception ?geo ?address ?site
WHERE 
{
  {
    ?museum wdt:P31 wd:Q33506.  
  }
  UNION
  {
    ?museum wdt:P31 ?museumType.
    ?museumType wdt:P279 wd:Q33506.
  } # instance of museum
  UNION
  {
    ?museum wdt:P31 ?museumType.
    ?museumType wdt:P31 / wdt:P8225 wd:Q33506.
  } # instance of subclass of museum
  
  ?museum wdt:P17 wd:Q212. # Ukraine
  
  { # instance of NP
    ?museum wdt:P131 ?np.
    ?np wdt:P31 / wdt:P279 wd:Q12051488.
  } 
  UNION
  {
    ?museum wdt:P131 ?np.
    ?np wdt:P31 / wdt:P279 wd:Q486972.
  }
  ?np wdt:P131 */ wdt:P131 ?region.
  ?region wdt:P31 wd:Q3348196.
  
  ?museum wdt:P571 ?inception.
  ?museum wdt:P625 ?geo.
  ?museum wdt:P6375 ?address.
  
  OPTIONAL {
    ?museum wdt:P856 ?site.  
  }
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "uk,en". } # Допомагає отримати назву вашою мовою, якщо ні, то англійською мовою
}
"""

# Define the namespaces
wd = Namespace("http://www.wikidata.org/entity/")
ex = Namespace("http://example.org/")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")

def get_museums_from_wikidata():
    # Execute the query over the Wikidata public endpoint
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Create a new graph
    g = Graph()


    # Add the namespaces to the graph
    g.bind("wd", wd)
    g.bind("ex", ex)
    g.bind("rdfs", rdfs)

    #print(results)
    museums = []

    # Add the results to the graph
    for result in results["results"]["bindings"]:
        #print(result)
        museum = URIRef(result["museum"]["value"])
        if museum in museums:
            continue
        museums.append(museum)

        museumLabel = Literal(result["museumLabel"]["value"])
        if "museumTypeLabel" in result:
            museumTypeLabel = Literal(result["museumTypeLabel"]["value"])
        npLabel = Literal(result["npLabel"]["value"])
        regionLabel = Literal(result["regionLabel"]["value"])
        address = Literal(result["address"]["value"]) #, lang="uk"
        geo = Literal(result["geo"]["value"])
        inception = Literal(result["inception"]["value"]) #, datatype=XSD.string
        if "site" in result:
            site = Literal(result["site"]["value"])

        g.add((museum, RDF.type, wd.Q33506))
        g.add((museum, rdfs.label, museumLabel))
        if "museumTypeLabel" in result:
            g.add((museum, ex.museumType, museumTypeLabel))
        g.add((museum, ex.np, npLabel))
        g.add((museum, ex.region, regionLabel))
        g.add((museum, ex.address, address))
        g.add((museum, ex.geo, geo))
        g.add((museum, ex.inception, inception))
        if "site" in result:
            g.add((museum, ex.site, site))

    data = g.serialize("museums.ttl", format="turtle")

    print('Data successfully fetched from Wikidata.')
    #print(data)
    #print(len(museums))

#get_museums_from_wikidata()