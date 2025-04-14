# The Hammer of Genes

## Overview

This project implements a containerized Flask API connected to a Redis database, allowing users to interact with the **HGNC (HUGO Gene Nomenclature Committee)** dataset. The application supports loading, retrieving, and deleting gene data through API endpoints, and querying information about individual genes using their HGNC IDs.

## File Descriptions

- **`gene_api.py`** – The main Flask application that exposes five API routes to interact with HGNC data.
- **`requirements.txt`** – Lists Python dependencies (`flask`, `redis`, `requests`) needed to run the Flask app.
- **`Dockerfile`** – Builds a Python container to run the Flask application.
- **`docker-compose.yaml`** – Implements the Flask app and Redis server as services.
- **`README.md`** – This file; Provides an overview of the application along with instructions on how to run it.

---

## How to Launch (Docker Compose)

1. Make sure Docker and Docker Compose are installed.
2. From the `homework06` directory, run:

```bash
docker-compose up --build
```

3. The Flask app will be available at `http://localhost:5000`, and Redis will run on port `6379`.

---

## API Endpoints and Example Usage

### Load HGNC Data into Redis
```bash
curl -X POST http://localhost:5000/data
```
**Expected Output:**
```
Data loaded into Redis
```

---

### Get All Gene Data
```bash
curl http://localhost:5000/data
```
**Expected Output (partial):**
```json
[
  {
    "hgnc_id": "HGNC:5",
    "symbol": "A1BG",
    "name": "alpha-1-B glycoprotein",
    ...
  },
  ...
]
```

---

### Delete All Gene Data
```bash
curl -X DELETE http://localhost:5000/data
```
**Expected Output:**
```
All HGNC data deleted from Redis
```

---

### List All HGNC IDs
```bash
curl http://localhost:5000/genes
```
**Expected Output:**
```json
["HGNC:5", "HGNC:7", "HGNC:8", ...]
```

---

### Get Data for a Specific Gene
```bash
curl http://localhost:5000/genes/HGNC:5
```
**Expected Output:**
```json
{
  "hgnc_id": "HGNC:5",
  "symbol": "A1BG",
  "name": "alpha-1-B glycoprotein",
  "locus_group": "protein-coding gene",
  "location": "19q13.43",
  ...
}
```

---

## About the Data

This project uses the [HGNC Complete Set](https://www.genenames.org/download/archive/) in JSON format. The dataset is maintained by the **HUGO Gene Nomenclature Committee**, part of the **Human Genome Organization**. Each record includes detailed data for a human gene, including:

- `hgnc_id` – Unique identifier for the gene.
- `symbol` – Official short symbol for the gene.
- `name` – Full name of the gene.
- `locus_group`, `locus_type` – Classification details.
- `location` – Chromosomal location.
- Other IDs like `entrez_id`, `ensembl_gene_id`, `ucsc_id`, and `pubmed_id`.

Not all fields are populated for every gene, as the dataset is sparsely filled.

**Citation:**  
*Human Genome Organisation Gene Nomenclature Committee (HGNC). Retrieved from https://www.genenames.org/download/archive/*

---

## AI Usage Statement

AI assistance was used to parse the data from the dataset and list out relevant information.  I used AI for this by uploading the raw JSON file into ChatGPT and asking it to return the first entry in a readable format.  By doing this, I was better able to understand the data and see what all it entails.  I used AI for this out of convenience because I was looking at the data on my iPad instead of my laptop and don't have a JSON editor/something like Notepad installed where I could read it better.
