from flask import Flask, render_template
import boto3
import json
 
app = Flask(__name__)
 
S3_BUCKET = 'bucket-for-result-of-iam-checker'
S3_KEY = 'scan-results.json'
 
def get_scan_results():
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    data = json.loads(obj['Body'].read().decode('utf-8'))
    return data
 
@app.route('/')
def index():
    data = get_scan_results()
    return render_template('index.html', data=data)
 
if __name__ == '__main__':
    app.run(debug=True)
 
