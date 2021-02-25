from flask import Flask, request, render_template
import psycopg2


####
# Connecting to the database.
####
try: 
    conn = psycopg2.connect(database="dipps_db", user="dreyceyalbin",  
    password="", host="localhost")
    print("connected")
except:
    print ("I am unable to connect to the database")


####
# Running the DIPSS database.
####
mycursor =conn.cursor()
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/v_timestamp')
def v_timestamp():
    mycursor.execute("SELECT * FROM function_view")
    data = mycursor.fetchall()
    return render_template('v_timestamp.html', data=data)

@app.route('/query_functionstruct')
def query_functionstruct():
    return render_template('query_functionstruct.html')


CREATEVIEW1 = "DROP VIEW IF EXISTS pdbjoin; DROP VIEW IF EXISTS function_view; CREATE VIEW function_view AS select uni.*, gp.cellprocess FROM uniprot as uni INNER JOIN goprocesses as gp ON uni.uniprot_id=gp.uniprot_id;"
CREATEVIEW2 = "DROP VIEW IF EXISTS pdbjoin; CREATE VIEW pdbjoin AS select func.*, h.pdb_id FROM function_view as func INNER JOIN hasproteins as h ON func.uniprot_id=h.uniprot_id;"

"SELECT ss.pdb_id, ss.sst3 AS Secondary_Structure FROM pdbjoin AS jj INNER JOIN secondarystructure as ss ON jj.pdb_id=ss.pdb_id WHERE jj.cellprocess LIKE '%apoptosis%' GROUP BY ss.pdb_id, ss.sst3"

@app.route('/query_functionstruct', methods=['POST'])
def my_form_post():
    FUNCTION = request.form['text']
    print(FUNCTION)
    mycursor.execute(CREATEVIEW1)
    print("CREATE VIEW 1 done")
    mycursor.execute(CREATEVIEW2)
    print("CREATE VIEW 2 done")
    #mycursor.execute(f"SELECT * FROM pdbjoin;")
    mycursor.execute(f"SELECT ss.pdb_id, ss.sst3 AS Secondary_Structure FROM pdbjoin AS jj INNER JOIN secondarystructure as ss ON jj.pdb_id=ss.pdb_id WHERE jj.cellprocess LIKE '%{FUNCTION}%' GROUP BY ss.pdb_id, ss.sst3 LIMIT 100")
    data = mycursor.fetchall()
    return render_template('query_functionstruct.html', data=data)
