# Documentación de Pruebas de Endpoints

## Descripción General

**Nombre del Proyecto:** HBnB Evolution  
**Fecha de Documentación:** 27/10/2024  
**Autores:** Bryan Alemán, Luna Leguisamo, Julieta Bobadilla  
**Versión del Proyecto:** 1.0

**Objetivo de la Prueba:**  
Verificar que los endpoints respondan correctamente a peticiones válidas e inválidas, siguiendo las reglas de validación establecidas y devolviendo los códigos de estado HTTP correspondientes.

---

## Resumen de Pruebas Realizadas Utilizando cURL

Probar la validación de los datos en los endpoints

- Pruebas de respuesta con datos válidos
- Pruebas de manejo de errores con datos inválidos
- Verificación de códigos de respuesta HTTP esperados

---

## Prueba de Creación de Usuario Válida



| **Endpoint** | `/api/v1/users/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo usuario. |
| **Cuerpo de la Petición** | JSON con atributos `first_name`, `last_name`, `email`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea correctamente el usuario.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un usuario y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
     "first_name": "Lidia",
     "last_name": "Butterley",
     "email": "lbutterley0@bravesites.com"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
       "id": "<generated_id>", // ID generado automáticamente
       "first_name": "Lidia",
       "last_name": "Butterley",
       "email": "lbutterley0@bravesites.com"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
       "id": "a4ec44b7-8734-4116-9492-9aeb44eec988", // ID generado
       "first_name": "Lidia",
       "last_name": "Butterley",
       "email": "lbutterley0@bravesites.com"
     }
     ```


## Prueba de Creación de Usuario Inválida



| **Endpoint** | `/api/v1/users/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo usuario con datos inválidos. |
| **Cuerpo de la Petición** | JSON con atributos `first_name`, `last_name`, `email`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas inválidas, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con campos vacíos y un formato de correo electrónico inválido, y retornar código de estado.   

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
     "first_name": "",
     "last_name": "",
     "email": "invalid-email"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
     
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "9511d94b-e374-4165-9f76-a5a5b6064987", // ID generado
     "first_name": "",
     "last_name": "",
     "email": "invalid-email"
     }
     ```
     Descripción del error: El sistema aceptó datos inválidos (`first_name` y `last_name` vacíos y formato de `email` incorrecto) y generó un nuevo usuario en lugar de rechazar la solicitud.


## Prueba de Creación de Lugar Válida



| **Endpoint** | `/api/v1/places/` |
|--------------|-------------------------|
| **Descripción** | Crear un nuevo lugar. |
| **Cuerpo de la Petición** | JSON con los atributos `title`, `description`, `price`, `latitude`, `longitude`, `owner_id` y `amenities`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea correctamente un lugar.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un lugar y retornar el código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/places/" \
     -H "Content-Type: application/json" \
     -d '{
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.00,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": ["54bd4f2b-b122-4706-93f6-9b0952dce101"]
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.0,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
           "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
           "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.0,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
           "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
           "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```


## Prueba de Creación de Lugar Inválida



| **Endpoint** | `/api/v1/places/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear un nuevo lugar con un precio negativo y coordenadas fuera de rango. |
| **Cuerpo de la Petición** | JSON con los atributos `title`, `description`, `price`, `latitude`, `longitude`, `owner_id` y `amenities`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas inválidas, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos inválidos para crear un lugar y retornar el código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/places/" \
     -H "Content-Type: application/json" \
     -d '{
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": -150.00,
     "latitude": 95.0,
     "longitude": -200.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": ["54bd4f2b-b122-4706-93f6-9b0952dce101"]
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "330c9a51-4ab4-4e40-b39f-6aa77f621f8c",
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": -50.0,
     "latitude": 95.0,
     "longitude": -200.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
            "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
            "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`price` negativo y `latitude` y `longitude` fuera de rango) y generó un nuevo lugar en lugar de rechazar la solicitud.



## Prueba de Creación de Reseña Válida



| **Endpoint** | `/api/v1/reviews/` |
|--------------|-------------------------|
| **Descripción** | Crea una nueva reseña asociada a un usuario y un lugar. |
| **Cuerpo de la Petición** | JSON con atributos `test`, `rating`, `place_id` y `user_id`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint crea una reseña con datos válidos.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear una reseña y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
     -H "Content-Type: application/json" \
     -d '{
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "4f763cc8-a23e-46c1-8087-aeb44ad8b2fc",
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `200 OK`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "4f763cc8-a23e-46c1-8087-aeb44ad8b2fc",
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
Notas: El servidor procesó la solicitud, pero no devolvió el código `201 Created` que sería el más adecuado para indicar la creación de un nuevo recurso.



## Prueba de Creación de Reseña Inválida



| **Endpoint** | `/api/v1/reviews/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear una reseña con datos inválidos. |
| **Cuerpo de la Petición** | JSON con atributos `test`, `rating`, `place_id` y `user_id`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas inválidas, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con `rating` fuera del rango permitido y sin `text`, y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
     -H "Content-Type: application/json" \
     -d '{
     "text": "",
     "rating": 6,
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `200 OK`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "f5da6870-ba21-4121-9ae6-61c7e09493c9",
     "text": "",
     "rating": 6,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`text` vacío y `rating` fuera de rango) y generó una nueva reseña en lugar de rechazar la solicitud.



## Prueba de Creación de Amenity Válida



| **Endpoint** | `/api/v1/amenities/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo "Amenity" (servicio) que luego puede ser asociado a un lugar. |
| **Cuerpo de la Petición** | JSON con atributo `name`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea el servicio correctamente.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un amenity y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" \
     -H "Content-Type: application/json" \
     -d '{
     "name": "Estacionamiento"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "<generated_id>", // ID generado automáticamente
     "name": "Estacionamiento"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "204d1b70-c817-4ae4-9c30-82fc7a995a08", // ID generado
     "name": "Estacionamiento"
     }
     ```


## Prueba de Creación de Amenity Inválida



| **Endpoint** | `/api/v1/amenities/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear una amenity con datos inválidos. |
| **Cuerpo de la Petición** | JSON con atributo `name`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos inválidos y muestra un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos inválidos (`name` exceda el límite permitido) para crear un amenity y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" \
     -H "Content-Type: application/json" \
     -d '{
     "name": "Amenity con un nombre demasiado largo para probar la validación en el sistema"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Name is too long"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "fec550ce-c10d-499d-9380-ea7234d972f3",
     "name": "Amenity con un nombre demasiado largo para probar la validación en el sistema"
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`name` demasiado largo) y generó un nuevo amenity en lugar de rechazar la solicitud.
