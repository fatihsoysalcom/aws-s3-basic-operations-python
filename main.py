import boto3
import os
import sys

def main():
    # Initialize S3 client
    # boto3 automatically uses credentials from environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN)
    # or from ~/.aws/credentials
    try:
        s3 = boto3.client('s3')
        print("Successfully connected to AWS S3.")
    except Exception as e:
        print(f"Error connecting to AWS S3: {e}")
        print("Please ensure your AWS credentials are configured correctly (e.g., via environment variables or ~/.aws/credentials).")
        sys.exit(1)

    # --- Demonstrate listing S3 buckets --- 
    # This is a fundamental operation for exploring AWS S3 resources.
    print("\n--- Listing S3 Buckets ---")
    try:
        response = s3.list_buckets()
        if not response['Buckets']:
            print("No S3 buckets found in your account.")
        else:
            print("Your S3 Buckets:")
            for bucket in response['Buckets']:
                print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"Error listing buckets: {e}")

    # --- Demonstrate putting and getting an object in a specific bucket ---
    # This shows basic data storage and retrieval, a core cloud computing concept.
    bucket_name = os.getenv('AWS_EXAMPLE_BUCKET_NAME')
    if bucket_name:
        print(f"\n--- Interacting with bucket: '{bucket_name}' ---")
        object_key = "hello_aws_learner.txt"
        content = "Hello from your AWS learning journey! This file was uploaded via Python."

        try:
            # Upload a file (object) to the specified bucket
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=content)
            print(f"Successfully uploaded '{object_key}' to '{bucket_name}'.")

            # Download the file (object) from the specified bucket
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            downloaded_content = response['Body'].read().decode('utf-8')
            print(f"Successfully downloaded '{object_key}'. Content:\n---START---\n{downloaded_content}\n---END---")

            # Clean up: Delete the object
            s3.delete_object(Bucket=bucket_name, Key=object_key)
            print(f"Successfully deleted '{object_key}' from '{bucket_name}'.")

        except s3.exceptions.NoSuchBucket:
            print(f"Error: Bucket '{bucket_name}' does not exist. Please create it or specify an existing bucket.")
        except Exception as e:
            print(f"Error interacting with object in '{bucket_name}': {e}")
    else:
        print("\nSkipping object interaction: Set the 'AWS_EXAMPLE_BUCKET_NAME' environment variable to interact with a specific bucket.")
        print("Example: export AWS_EXAMPLE_BUCKET_NAME='your-unique-bucket-name'")

if __name__ == "__main__":
    main()
