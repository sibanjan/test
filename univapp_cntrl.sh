sed 's/#/,/g' univ_data_live.csv > univ_data_trans1.csv
sed 's/(,/,/g' univ_data_trans1.csv > univ_data_live.csv
cat univ_data_live.csv >> univ_data.csv
cat /dev/null > univ_data_live.csv
cat /dev/null > univ_data_live.csv
s3cmd put univ_data.csv s3://universityselapp
s3cmd setacl --acl-public --recursive s3://universityselapp
