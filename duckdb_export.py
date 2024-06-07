import duckdb
from minio import Minio
from minio.error import S3Error
import json

def main():

    city = 'Berlin'
    nation = 'Deutschland'

    con = duckdb.connect("data/stage_data.db")
    con.sql("COPY transform_data TO 'data/transformed.csv'")

    f =  open('key/dev_credentials.json')
    data = json.load(f)
    access_key = data['accessKey']
    secret_key=data['secretKey']

    client = Minio("localhost:9000",
            access_key=access_key,
            secret_key=secret_key,
            secure=False
        )
    
    source_file = 'data/' + 'transformed.csv'

    bucket_name = "scraphouse"

    destination_file = 'transformed' + '/' + city + '.csv'

    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")
        
    client.fput_object(
            bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )
    
if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
