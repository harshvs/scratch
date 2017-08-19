import json
import sys
import sqlite3
import uuid
from random import randint
import time

current_time = lambda: int(round(time.time() * 1000))

# Generate 10 conversations
convIds = [ str(uuid.uuid4()) for i in range(10) ]

typeIds = [ i for i in range(30) ]

conn = sqlite3.connect("search_full.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS search ")

# With content - 2 columns
c.execute("CREATE VIRTUAL TABLE search USING fts4(id1 TEXT, id2 TEXT, tid NUMERIC, ts NUMERIC, field1 TEXT, field2 TEXT, notindexed=id1, notindexed=id2, notindexed=tid, notindexed=ts)")
conn.commit()
with open(sys.argv[1], 'r') as file:
    for line in file:
        parsed = json.loads(line)
        id1 = str(uuid.uuid4())
        id2 = convIds[randint(0,9)]
        tid = typeIds[randint(0,29)]
        ts = current_time()
        speaker = parsed.get("speaker")
        text = parsed.get("text_entry")
        if text:
            c.execute("INSERT INTO search(id1, id2, ts, tid, field1, field2) VALUES('{0}','{1}', {2}, {3}, '{4}', '{5}')".format(id1, id2, tid, ts, speaker, text))
            # print(json.dumps(parsed, indent=4, sort_keys=True))
conn.commit()
        
        
        
