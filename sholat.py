#!/bin/python
import os
import json
import subprocess
from datetime import datetime

now = datetime.now()
current_date = now.strftime("%Y/%m/%d")
city_code = "0404" 
os.system("sh logosholat.sh")
rgg = input("Masukan Kode Daerah :")
result = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/jadwal/{rgg}/{current_date}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result_json = json.loads(result.stdout)
print(result_json["data"]["lokasi"])
print(result_json["data"]["daerah"])
print(f'Hari/Tanggal: {result_json["data"]["jadwal"]["tanggal"]}')
print(f'- imsak {result_json["data"]["jadwal"]["imsak"]}')
print(f'- subuh {result_json["data"]["jadwal"]["subuh"]}')
print(f'- terbit {result_json["data"]["jadwal"]["terbit"]}')
print(f'- dhuha {result_json["data"]["jadwal"]["dhuha"]}')
print(f'- dzuhur {result_json["data"]["jadwal"]["dzuhur"]}')
print(f'- ashar {result_json["data"]["jadwal"]["ashar"]}')
print(f'- maghrib {result_json["data"]["jadwal"]["maghrib"]}')
print(f'- isya {result_json["data"]["jadwal"]["isya"]}')

