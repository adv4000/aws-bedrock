# ------------------------------------------------
# Program by Denis Astahov
# Generated Image from Text using AWS Bedrock and
# "amazon.titan-image-generator-v1" GenAI Model
#
# Version      Date        Info
# 1.0          2024    Initial Version
#
# ------------------------------------------------
import boto3
import json
import base64
import io
from PIL import Image

AWS_ACCESS_KEY_ID  = "xxxxxxxxxxxx"
AWS_SECRET_KEY_ID  = "yyyyyyyyyyyyyyyyyyyyyyyyyyyy"
AWS_DEFAULT_REGION = "us-east-1"

bedrock = boto3.client(service_name='bedrock-runtime', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY_ID, region_name=AWS_DEFAULT_REGION)
#bedrock = boto3.client(service_name='bedrock-runtime')

TEXT_PROMPT    = "Draw realistic Ninja riding on red Honda CBR650R"
IMAGE_HEIGHT   = 512         # See https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-image.html
IMAGE_WEIDTH   = 512         # See https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-image.html
IMAGE_QUALITY  = "premium"  # standard | premium
IMAGE_SEED     = 200         # Range:  0 - 2147483646
IMAGE_CFGSCALE = 8.0         # Range:  1.1 - 10.0

MODEL_ID = "amazon.titan-image-generator-v1"
IMAGE_REQUEST = json.dumps(
    {
     "taskType": "TEXT_IMAGE",
     "textToImageParams": {"text": TEXT_PROMPT},
     "imageGenerationConfig": {
                 "numberOfImages": 1,
                 "quality" : IMAGE_QUALITY,
                 "cfgScale": IMAGE_CFGSCALE,
                 "height"  : IMAGE_HEIGHT,
                 "width"   : IMAGE_WEIDTH,
                 "seed"    : IMAGE_SEED
     }
    }
)

print("Sending Request to generate Image from text...")
generated_reply = bedrock.invoke_model(body=IMAGE_REQUEST, modelId=MODEL_ID, accept="application/json", contentType="application/json")
print("Response Received...")

generated_body = json.loads(generated_reply.get("body").read())
base64_image   = generated_body.get("images")[0]
base64_bytes   = base64_image.encode('ascii')
image_bytes    = base64.b64decode(base64_bytes)

# Show Generated image to the screen
Image.open(io.BytesIO(image_bytes)).show()

# Save Generated Image to file
with open(IMAGE_QUALITY + "-output.png", "wb") as f:
    f.write(image_bytes)
