import json
import sys
import sqlite3

conn = sqlite3.connect("search_contentless.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS search ")

# With content - 2 columns
c.execute("CREATE VIRTUAL TABLE search USING fts4(content="", field1 TEXT, field2 TEXT)")
conn.commit()
with open(sys.argv[1], 'r') as file:
    id = 0
    for line in file:
        parsed = json.loads(line)
        speaker = parsed.get("speaker")
        text = parsed.get("text_entry")
        if text:
            c.execute("INSERT INTO search(docid, field1, field2) VALUES({0}, '{1}','{2}')".format(id, speaker, text))
            id = id + 1
            # print(json.dumps(parsed, indent=4, sort_keys=True))
conn.commit()
        
        
        
