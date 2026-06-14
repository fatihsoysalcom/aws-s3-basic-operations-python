# AWS S3 Basic Operations Python

This Python script demonstrates fundamental interactions with Amazon S3, a core AWS cloud storage service. It lists all S3 buckets in your account and, if a bucket name is provided via an environment variable, it uploads a simple text file, downloads it, and then deletes it. This serves as a basic introduction to programmatic AWS interaction for learners.

## Language

`python`

## How to Run

1. Install boto3: `pip install boto3`
2. Configure AWS credentials (e.g., via environment variables or `~/.aws/credentials`).
3. Run: `python main.py` (Optionally, set `AWS_EXAMPLE_BUCKET_NAME` env var for object operations, e.g., `export AWS_EXAMPLE_BUCKET_NAME="your-bucket-name"`)

## Original Article

This example accompanies the Turkish article: [Sıfırdan AWS Bulut Öğrenme Yolculuğum: 90 Günde Uzmanlığa Adım Adım](https://fatihsoysal.com/blog/sifirdan-aws-bulut-ogrenme-yolculugum-90-gunde-uzmanliga-adim-adim/).

## License

MIT — see [LICENSE](LICENSE).
