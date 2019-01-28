import psycopg2
conn = psycopg2.connect(database="hr", user="postgres", password="pg", host="127.0.0.1", port="5432")
print("Database Connected....")
cur = conn.cursor()
cur.execute("COPY(SELECT distinct table_name, column_name,data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name != 'pg_stat_statements' AND table_name != 'pg_buffercache' AND column_name not in ('active','institution_id','created_at','updated_at') AND column_name not like '%id%') TO '/tmp/testthis.csv' (format CSV)")
#print("TABLE NAME,COLUMN NAME,DATA TYPE")
print(" file created successful") 
#rows = cur.fetchall()
#for row in rows:
#   print(row[0],' ',row[1],' ',row[2])

conn.close()