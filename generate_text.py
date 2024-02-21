# ------------------------------------------------
# Program by Denis Astahov
# Generated Text from Input using AWS Bedrock and
# "meta.llama2-70b-chat-v1" GenAI Model
#
# Version      Date        Info
# 1.0          2024    Initial Version
#
# ------------------------------------------------
import boto3
import json

AWS_ACCESS_KEY_ID  = "xxxxxxxxxxxx"
AWS_SECRET_KEY_ID  = "yyyyyyyyyyyyyyyyyyyyyyyyyyyy"
AWS_DEFAULT_REGION = "us-east-1"

bedrock = boto3.client(service_name='bedrock-runtime', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY_ID, region_name=AWS_DEFAULT_REGION)
#bedrock = boto3.client(service_name='bedrock-runtime')

TEXT_PROMPT      = "[Justin, Vlad, Petra, Masha, Misha, John, Klara, Karina] Sort by Female/Male only, no other text"
TEXT_TEMPERATURE = 0.1  # Range: 0 - 1
TEXT_TOP_P       = 0.2  # Range: 0 - 1
TEXT_MAXGENLEN   = 200  # Range: 1 - 2048


MODEL_ID = "meta.llama2-70b-chat-v1"
TEXT_REQUEST = json.dumps(
    {
     "prompt"     : TEXT_PROMPT,
     "temperature": TEXT_TEMPERATURE,
     "top_p"      : TEXT_TOP_P,
     "max_gen_len": TEXT_MAXGENLEN
     }
)

print("Sending Request to generate TEXT...")
generated_reply = bedrock.invoke_model(body=TEXT_REQUEST, modelId=MODEL_ID, accept="application/json", contentType="application/json")
print("Response Received...")

generated_body = json.loads(generated_reply.get("body").read())
generated_text = generated_body["generation"]
print(generated_text)
