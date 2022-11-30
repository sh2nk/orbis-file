# Orbis File
##### Simple fileserver with db serialization.
##### Storage synchronyzes with db on every app start.
##### Some file extensions can be disabled.

### Configuration

Make sure that you created `config.env` file. 
Use `config.env.example` as template:

```dosini
FLASK_APP=run.py
FLASK_DEBUG=1
DB_URI=postgresql://user:passwd@localhost:5432/orbisfile
UPLOAD_FOLDER=/home/storage/
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
POSTGRES_USER=user
POSTGRES_PASSWORD=passwd
POSTGRES_DB=orbisfile
```

### Deploy with Docker

When deploying this setup, the fileserver will be available at port 8880

`docker compose up`

In some cases `chmod +x ./entrypoint.sh` on host system may be required

### Quick API Description

##### Get all files

```
GET /files
```

Response format:
```json
[
    {
        "comment": "image file",
        "created_at": "2022-11-30 12:03:12.111262",
        "extension": ".jpg",
        "id": "2897d34c-02c2-4315-b4cf-377d5d5ecf40",
        "name": "img",
        "path": "/home/storage/",
        "size": "34594",
        "updated_at": "2022-11-30 12:03:12.111262"
    },
    ...
]
```

##### Get specific file

```
GET /file/<uuid4>
```

Response format:
```json
{
    "comment": "image file",
    "created_at": "2022-11-30 12:03:12.111262",
    "extension": ".jpg",
    "id": "2897d34c-02c2-4315-b4cf-377d5d5ecf40",
    "name": "img",
    "path": "/home/storage/",
    "size": "34594",
    "updated_at": "2022-11-30 12:03:12.111262"
}
```

##### Upload new file

```
POST /file/<your_comment_string>

Content-Type: multipart/form-data
"file": <file_data>
```

Response format:
```json
{
    "id": "f98b3d3f-301c-4902-ba8e-a113daa43a02",
    "message": "Added file succsesfully"
}
```

##### Edit file data

```
PUT /file/<uuid4>

Content-Type: application/json
```
```json
{
    "name": "new_filename",
    "comment": "example comment",
    "path": "/home/storage/subdir"
}
```

Response format:
```json
{
    "id": "f98b3d3f-301c-4902-ba8e-a113daa43a02",
    "message": "Edited file succsesfully"
}
```

##### Delete file

```
DELETE /file/<uuid4>
```

Response format:
```json
{
    "id": "f98b3d3f-301c-4902-ba8e-a113daa43a02",
    "message": "Deleted file succsesfully"
}
```

##### Search files

```
GET /file/search/<search_query>
```
Search query can be either filepath and any keywords from file comments.

Response format:
```json
[
    {
        "comment": "image file",
        "created_at": "2022-11-30 12:03:12.111262",
        "extension": ".jpg",
        "id": "2897d34c-02c2-4315-b4cf-377d5d5ecf40",
        "name": "img",
        "path": "/home/storage/",
        "size": "34594",
        "updated_at": "2022-11-30 12:03:12.111262"
    },
    ...
]
```

##### Download file

```
GET /file/download/<uuid4>
```

Response format:
```
Content-Type: application/octet-stream
<file_attachment>
```

##### Error message example

```json
{
    "error": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
```