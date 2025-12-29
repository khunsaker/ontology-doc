import json
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
AUTH = ("neo4j", "#ESX%TFV3esx5tfv")
DB = "Shark2"
OUTFILE = "export/json/Kind.json"

QUERY = (
    "MATCH (k:Kind) "
    "WITH collect(DISTINCT keys(k)) AS key_lists "
    "UNWIND key_lists AS kl "
    "UNWIND kl AS key "
    "WITH collect(DISTINCT key) AS all_props "
    "CALL { "
    "  MATCH (k:Kind)-[r]->(t) "
    "  RETURN collect(DISTINCT { "
    "    type: type(r), "
    "    direction: 'OUT', "
    "    target_labels: labels(t) "
    "  }) AS out_rels "
    "} "
    "CALL { "
    "  MATCH (s)-[r]->(k:Kind) "
    "  RETURN collect(DISTINCT { "
    "    type: type(r), "
    "    direction: 'IN', "
    "    source_labels: labels(s) "
    "  }) AS in_rels "
    "} "
    "RETURN all_props AS properties, out_rels AS outgoing_relationships, in_rels AS incoming_relationships"
)

driver = GraphDatabase.driver(URI, auth=AUTH)
with driver.session(database=DB) as session:
    rec = session.run(QUERY).single()
driver.close()

if rec is None:
    raise SystemExit("No :Kind nodes found. Cannot export schema.")

properties = sorted(rec["properties"] or [])
outgoing = rec["outgoing_relationships"] or []
incoming = rec["incoming_relationships"] or []

for x in outgoing:
    x["target_labels"] = sorted(x.get("target_labels") or [])
for x in incoming:
    x["source_labels"] = sorted(x.get("source_labels") or [])

def sort_key_out(x):
    return (x.get("type", ""), ",".join(x.get("target_labels") or []))

def sort_key_in(x):
    return (x.get("type", ""), ",".join(x.get("source_labels") or []))

outgoing = sorted(outgoing, key=sort_key_out)
incoming = sorted(incoming, key=sort_key_in)

doc = {
    "label": "Kind",
    "database": DB,
    "connection_uri": URI,
    "properties": [{"name": p, "type": "string"} for p in properties],
    "relationships": {"outgoing": outgoing, "incoming": incoming},
}

with open(OUTFILE, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, sort_keys=True)

print("Wrote", OUTFILE)
print("Properties:", len(properties))
print("Outgoing relationships:", len(outgoing))
print("Incoming relationships:", len(incoming))
