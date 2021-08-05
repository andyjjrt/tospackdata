import requests

param = {"sheet_id": "1gCcD0hF1RLlh8_v8uX1bp2DfgdvJglpGaGogw4CCeho"}
r = requests.get('https://script.google.com/macros/s/AKfycbwkF870A5T_uLDzWh56d86yd3gAL3rdOvj4R1AKsfoD-k1kXW_J/exec', params = param)
with open('data/jumbodata.json', 'w') as f:
    f.write(r.text)