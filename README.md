# GeoLocalizer

**How to use**

* Needed python3.8

* chmod +x createapp.sh

* ./createapp.sh

* Add yours Ipstack and django private keys to geolocalizer/.env

* python manage.py runserver

* In other tab: python initialfill.py

Endpoints:

* **/register/**
  * **POST** - Register. Fields: username, password
  * **PUT** / **PATCH** - Change password. Access token required. Fields: username, password. Id required (/register/<id>/)
* **/delete-user/**
  * **DELETE** - Delete user. Only access token required.
* **/token/**
  * **POST** - Generate JWT token. Fields: username, password
* **/token/refresh/**
  * **POST** - Refresh JWT access token. Refresh token required.
* **/fetch-address/**
  * **GET** - Display short geolocations list. Only access token required.
  * **POST** - Fetch Ipstack. Access token required.  Fields: address
* **/geolocations/**
  * **GET** - Display full geolocations list. Only access token required.
  * **POST** - Manually add geolocation entry. Access token required. Fields: same as single entry from **GET**
  * **PUT** / **PATCH** - Edit single geolocation entry. Access token required. Fields: any from single **GET** entry. Id required(/geolocations/<id>/)
  * **DELETE** - Delete single geolocation entry. Access token required. Id required(/geolocations/<id>/)
* **/locations/**
  * **GET** - Display full locations list. Only access token required.
  * **PUT** / **PATCH** - Edit single location entry. Access token required. Fields: any from single **GET** entry. Id required(/locations/<id>/)
* **/languages/**
  * **GET** - Display full languages list. Only access token required.
  * **PUT** / **PATCH** - Edit single language entry. Access token required. Fields: any from single **GET** entry. Id required(/languages/<id>/)
