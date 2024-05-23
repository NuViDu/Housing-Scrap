from minio import Minio
from minio.error import S3Error
import datetime
import json


def main():
    
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.timestamp()
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    f =  open('key/dev_credentials.json')
    data = json.load(f)
    access_key = data['accessKey']
    secret_key=data['secretKey']
    
    city = 'Berlin'
    nation = 'Deutschland'
    
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("localhost:9000",
        access_key=access_key,
        secret_key=secret_key,
        secure=False
    )

    # The file to upload, change this path if needed
    source_file = 'data/' + nation + '/' + city + '_housing_data.csv'

    # The destination bucket and filename on the MinIO server
    bucket_name = "scraphouse"
    destination_file = nation + '/' + city + '/'+ timestamp + '_housing_data.csv'

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
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