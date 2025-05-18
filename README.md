# AWS Sandbox

A personal sandbox for experimenting with AWS services using Python scripts. This repository contains various utilities and scripts for automating, managing, and testing AWS resources such as S3, DynamoDB, EC2, and Lambda.

## Contents

Sample scripts included (partial list):
- S3 bucket creation, listing, and deletion
- DynamoDB table creation and entry management
- EC2 instance automation (creation, starting, stopping)
- Lambda function authorizers and demo integrations
- API Gateway-related utility scripts

Browse the full contents here: [aws_sandbox directory](https://github.com/ErikPohl444/aws_sandbox/tree/main)

## Prerequisites

- Python 3.x
- boto3 (`pip install boto3`)
- AWS credentials set up (via `~/.aws/credentials` or environment variables)

## Installing

1. Clone the repo:
   ```bash
   git clone https://github.com/ErikPohl444/aws_sandbox.git
   cd aws_sandbox
   ```
2. Install requirements as needed (edit/add `requirements.txt` as appropriate):
   ```bash
   pip install boto3
   ```

## Running the Scripts

Each script is standalone. Review the docstrings or comments in each file for usage instructions and required arguments. Example:
```bash
python createS3Bucket.py
```

## Contributing

Pull requests are welcome! If you have improvements or new AWS experiments, feel free to share.

## Authors

- **Erik Pohl** - Initial work

See the list of GitHub contributors for more.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- Thanks to everyone whose questions and challenges inspired these AWS experiments.
