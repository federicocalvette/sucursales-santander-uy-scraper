import request
import json
from datetime import datetime


class Scrapper:

    date = datetime.now()

    branch_response = {
        'banco': 'Santander',
        'pais': 'Uruguay',
        'fechaConsulta': str(date),
        'sucursales': {}
    }

    def run(self):
        branch_content = request.bank_request()
        branch_json_content = json.loads(branch_content.text)
        for branch in branch_json_content:

            if branch['type']['valueName'] != "branch":
                continue

            else:
                name_splited = branch['name'].split("-")
                localidad = branch.get('city', {}).get('name', '')
                direccion = branch['address']


                branch_data = {
                    "nombreSucursal": name_splited[1].strip(),
                    "numeroSucursal": name_splited[0].strip(),
                    "localidad": localidad,
                    "direccion": direccion,
                    "horarios": branch['workingHours'].split("|"),
                    "telefono": branch['telephone'],
                }

                self.branch_response['sucursales'][name_splited[0].strip()] = branch_data

        return self.branch_response