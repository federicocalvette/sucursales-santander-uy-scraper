# sucursales-santander-uy-scraper
-------------------------------------------

## Run with: 

`uvicorn app:app --reload`

-------------------------------------------
### Request:
`curl -X 'GET'   'http://127.0.0.1:8000/santander/sucursales'   -H 'accept: application/json'`

### Documentation
http://127.0.0.1:8000/docs

### Response:
```json
{
  "banco": "Santander",
  "pais": "Uruguay",
  "fechaConsulta": "2023-01-25 15:42:14.281992",
  "sucursales": {
    "21": {
      "nombreSucursal": "Paysandú",
      "numeroSucursal": "21",
      "localidad": "Paysandú",
      "direccion": "Av. 18 de Julio 1139",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 212"
    },
    "79": {
      "nombreSucursal": "Península Express",
      "numeroSucursal": "79",
      "localidad": "Punta Del Este",
      "direccion": "Av. Gorlero y 25",
      "horarios": [
        "Horario sucursal: L a V 13 - 18 hs.",
        " Horario ZonaPlus: 6:00 - 22:00 hs."
      ],
      "telefono": "(2) 1747 792"
    },
    "32": {
      "nombreSucursal": "Salto",
      "numeroSucursal": "32",
      "localidad": "Salto",
      "direccion": "Uruguay 599",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 322"
    },
    "23": {
      "nombreSucursal": "San José",
      "numeroSucursal": "23",
      "localidad": "San José",
      "direccion": "18 de Julio 461",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 232"
    },
    "26": {
      "nombreSucursal": "Tacuarembó",
      "numeroSucursal": "26",
      "localidad": "Tacuarembó",
      "direccion": "18 de Julio 258",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 262"
    },
    "72": {
      "nombreSucursal": "Nuevo Centro Hipotecario & Coche",
      "numeroSucursal": "72",
      "localidad": "Pocitos",
      "direccion": "Br. España 2903",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 722"
    },
    "17": {
      "nombreSucursal": "Ciudad de la Costa",
      "numeroSucursal": "17",
      "localidad": "Ciudad de la Costa",
      "direccion": "Av. Giannattasio Km 21200",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 172"
    },
    "2": {
      "nombreSucursal": "18 de Julio",
      "numeroSucursal": "2",
      "localidad": "Centro",
      "direccion": "18 de Julio 1321",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 17470220"
    },
    "75": {
      "nombreSucursal": "Aguada",
      "numeroSucursal": "75",
      "localidad": "Aguada",
      "direccion": "Av. San Martín 2108",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 752"
    },
    "73": {
      "nombreSucursal": "Arocena",
      "numeroSucursal": "73",
      "localidad": "Carrasco",
      "direccion": "Av. Arocena 1577",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 732"
    },
    "84": {
      "nombreSucursal": "Biarritz",
      "numeroSucursal": "84",
      "localidad": "Punta Carretas",
      "direccion": "21 de Setiembre 3021",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 842"
    },
    "7": {
      "nombreSucursal": "Bvar. Artigas",
      "numeroSucursal": "7",
      "localidad": "Jacinto Vera",
      "direccion": "Av. Gral. Flores 3208",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 072"
    },
    "19": {
      "nombreSucursal": "Carrasco",
      "numeroSucursal": "19",
      "localidad": "Carrasco",
      "direccion": "Blanes Viale 6399",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 192"
    },
    "71": {
      "nombreSucursal": "Casa Central",
      "numeroSucursal": "71",
      "localidad": "Centro",
      "direccion": "18 de Julio 999",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 712"
    },
    "61": {
      "nombreSucursal": "Ciudad Vieja",
      "numeroSucursal": "61",
      "localidad": "Ciudad Vieja",
      "direccion": "25 de Mayo 501",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 612"
    },
    "12": {
      "nombreSucursal": "Comercio",
      "numeroSucursal": "12",
      "localidad": "Malvín",
      "direccion": "Av. Italia 3830",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 122"
    },
    "70": {
      "nombreSucursal": "Golf",
      "numeroSucursal": "70",
      "localidad": "Punta Carretas",
      "direccion": "Br. Artigas 380",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 702"
    },
    "5": {
      "nombreSucursal": "Ombú",
      "numeroSucursal": "5",
      "localidad": "Pocitos",
      "direccion": "Br. España 2640",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 052"
    },
    "81": {
      "nombreSucursal": "Pablo de María",
      "numeroSucursal": "81",
      "localidad": "Cordón",
      "direccion": "Av. 18 de Julio 2002",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 812"
    },
    "67": {
      "nombreSucursal": "Parque Batlle",
      "numeroSucursal": "67",
      "localidad": "Parque Batlle",
      "direccion": "Av. 8 de Octubre 2699",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 672"
    },
    "74": {
      "nombreSucursal": "Paso Molino",
      "numeroSucursal": "74",
      "localidad": "Paso Molino",
      "direccion": "Av. Agraciada 4228",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 17477420"
    },
    "60": {
      "nombreSucursal": "Centro SELECT Puerto de Buceo",
      "numeroSucursal": "60",
      "localidad": "Buceo",
      "direccion": "26 de Marzo 3540",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(+598) 26226"
    },
    "16": {
      "nombreSucursal": "Universidad Católica",
      "numeroSucursal": "16",
      "localidad": "Larrañaga",
      "direccion": "Av. 8 de Octubre 2738",
      "horarios": [
        "L a V 11 - 13 hs y 15 - 18 hs. ",
        " Autoservicio: L a V 11 - 18 hs."
      ],
      "telefono": "(2) 1747 675"
    },
    "37": {
      "nombreSucursal": "Roosevelt",
      "numeroSucursal": "37",
      "localidad": "Punta Del Este",
      "direccion": "Av. Roosevelt y Parada 11",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 372"
    },
    "30": {
      "nombreSucursal": "Colonia",
      "numeroSucursal": "30",
      "localidad": "Colonia",
      "direccion": "Av. Gral. Flores 544",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 302"
    },
    "31": {
      "nombreSucursal": "Colonia Valdense",
      "numeroSucursal": "31",
      "localidad": "Colonia Valdense",
      "direccion": "Ruta 1 y Av. Armand Ugon",
      "horarios": [
        "Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": ""
    },
    "25": {
      "nombreSucursal": "Durazno",
      "numeroSucursal": "25",
      "localidad": "Durazno",
      "direccion": "18 de Julio 442",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 252"
    },
    "34": {
      "nombreSucursal": "Las Piedras",
      "numeroSucursal": "34",
      "localidad": "Las Piedras",
      "direccion": "Av. Gral Artigas 601",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 342"
    },
    "27": {
      "nombreSucursal": "Mercedes",
      "numeroSucursal": "27",
      "localidad": "Mercedes",
      "direccion": "Eusebio Giménez 723",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 17472720"
    },
    "15": {
      "nombreSucursal": "Pando",
      "numeroSucursal": "15",
      "localidad": "Pando",
      "direccion": "Gral. Artigas 953",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: L a V 09 - 19 hs."
      ],
      "telefono": "(2) 1747 152"
    },
    "24": {
      "nombreSucursal": "Melo",
      "numeroSucursal": "24",
      "localidad": "Melo",
      "direccion": "Justino Muniz 750 esq. Florencio Sanchez",
      "horarios": [
        "Horario sucursal: L a V 13 - 17 hs. ",
        " Horario ZonaPlus: 06 - 22 hs."
      ],
      "telefono": "(2) 1747 242"
    },
    "1": {
      "nombreSucursal": "PAGO A PROVEEDORES CENTRALIZADO",
      "numeroSucursal": "1",
      "localidad": "",
      "direccion": "PISO 1 - 25 De Mayo 501",
      "horarios": [
        "Lunes a viernes de 14 a 17 hs."
      ],
      "telefono": "(598) 291607"
    },
    "86": {
      "nombreSucursal": "CarOne",
      "numeroSucursal": "86",
      "localidad": "Ciudad de la Costa",
      "direccion": " Cam. de Los Horneros, 15800 Ciudad de la Costa, Departamento de Canelones",
      "horarios": [
        "L a V 14 - 18 hs - Autoservicio: 09 - 00 hs."
      ],
      "telefono": "1747 8601"
    },
    "85": {
      "nombreSucursal": "Paso de los Toros (SUMO)",
      "numeroSucursal": "85",
      "localidad": "",
      "direccion": "",
      "horarios": [
        "Lunes a Viernes de 14 a 18 hs / Zona de autoservicios de 9 a 20 hs."
      ],
      "telefono": "1747 8500"
    }
  }
}
```
