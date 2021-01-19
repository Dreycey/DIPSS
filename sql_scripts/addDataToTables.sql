

/*
Description:

This SQL script is used for constructing all of the tables in the database 
from the availiable csvs. The CSV files must be downloaded from the portal 
before running this script.
*/


\copy crystalstructuresequence FROM 'curated_csvs/crystalstructuresequence_COMP533.csv' WITH (FORMAT csv);
\copy crystalstructure FROM 'curated_csvs/structure.csv' WITH (FORMAT csv);
\copy secondarystructure FROM 'curated_csvs/secondarystructure_COMP533.csv' WITH (FORMAT csv);
\copy uniprot FROM 'curated_csvs/uniprot_2.csv' WITH (FORMAT csv);
\copy hasproteins FROM 'curated_csvs/hasproteins_COMP533.csv' WITH (FORMAT csv);
\copy refseq FROM 'curated_csvs/refseqTable.csv' WITH (FORMAT csv);
\copy goprocesses FROM 'curated_csvs/processTable.csv' WITH (FORMAT csv);                     
\copy gofunctions FROM 'curated_csvs/functionTable.csv' WITH (FORMAT csv);
