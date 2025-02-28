import json
# => Write a simple JSON file 
datas = {
     "title":"Python FastAPI Batch 1",
     "price": 25.99,
     "packages":["FastAPI","Jinja2","Websocket","OpenAi"]
}

with open('files/file11.json','w') as file:
     # json.dump(datas,file)
     # json.dump(datas,file,indent=4) # indent is optional for text indentation
     # json.dump(datas,file,indent=4,sort_keys=True) # sort_key is option for a to z
     json.dump(datas,file,sort_keys=True) 
     
     print("Successfully Created")

# Error Handling
try:
     invaliddatas = {"numbers":{10,20,30}} # Set is not JSOn-serializable
     with open("files/fileerror.json","w") as file:
          json.dump(invaliddatas,file)
except TypeError as e:
     print("Error: Invalid JSON format!",str(e))
else:
     print(datas)

# 26WJ

