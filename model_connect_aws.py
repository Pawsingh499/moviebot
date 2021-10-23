
bucket = "sugges"
s3 = boto3.client('s3', config=Config(connect_timeout=600, read_timeout=600, retries={'max_attempts': 10}))
metadata = pd.read_csv(s3.get_object(Bucket= bucket, Key="metadata.csv")['Body'])
credits_ = pd.read_csv(s3.get_object(Bucket= bucket, Key="credits.csv")['Body'])
keywords = pd.read_csv(s3.get_object(Bucket= bucket, Key="keywords.csv")['Body'])
