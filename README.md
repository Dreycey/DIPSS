# DIPSS


## About/ Description

## Usage

### Example Queries

#### Loooking at function

* create a view
```
psql -c "CREATE VIEW function_view AS select uni.*, gp.cellprocess FROM uniprot as uni INNER JOIN goprocesses as gp ON uni.uniprot_id=gp.uniprot_id;" -d dipps_db
```
                                                                                
* create a view                                                                 
```                                                                             
psql -c "CREATE VIEW pdbjoin AS select func.*, h.pdb_id FROM function_view as func INNER JOIN hasproteins as h ON func.uniprot_id=h.uniprot_id; " -d dipps_db
``` 

* look at cellular function on the view
```
psql -c "SELECT ss.pdb_id, ss.sst3 AS Secondary_Structure FROM pdbjoin AS jj INNER JOIN secondarystructure as ss ON jj.pdb_id=ss.pdb_id WHERE jj.cellprocess LIKE '%apoptosis%' GROUP BY ss.pdb_id, ss.sst3" -d dipps_db
```

## Dependencies // setting up the database

### Setting up the environment.
1. The first step is to download conda

2. Create a conda environment for DIPSS
```
conda create --name DIPPS
```

3. Download postgres SQL
```
conda install -c anaconda postgresql 
```

### Constructing the database.

1. Create the local database                                                    
```                                                                             
initdb -D dipps_db                                                              
```

2. Start the database server
```
pg_ctl -D dipps_db -l logfile start
```

3. Then create the database
```
createdb dipps_db
```

4. Create the database in psql
```
psql -c "CREATE DATABASE dipss_db" -d dipps_db
```

5. list the database to ensure it exists.
```
psql -c "\list" -d dipps_db 
```

6. Connect to the DIPSS database
```
psql -c "\connect dipps_db" -d dipps_db
```

7. Build the tables
```
psql -f sql_scripts/create_database_tables.sql -d dipps_db
```

8. List the tables to make sure they were contructed.
```
psql -c "\dt" -d dipps_db
```

9. Add data to the tables.
```
psql -f sql_scripts/addDataToTables.sql -d dipps_db
```


