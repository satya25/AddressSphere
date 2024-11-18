#!/bin/bash

# Create directories
mkdir -p app/templates
mkdir -p app/services
mkdir -p tests/unit
mkdir -p tests/system
mkdir -p ci_cd/kubernetes
mkdir -p ci_cd/scripts
mkdir -p doc/sql

# Create empty files
touch app/__init__.py
touch app/models.py
touch app/routes.py
touch app/services/__init__.py
touch app/services/address_service.py
touch app/templates/base.html
touch app/templates/create_address.html
touch app/templates/edit_address.html
touch app/templates/index.html
touch app/templates/view_address.html
touch tests/unit/__init__.py
touch tests/unit/test_models.py
touch tests/unit/test_routes.py
touch tests/system/__init__.py
touch tests/system/test_create_address.py
touch tests/system/test_edit_address.py
touch tests/system/test_view_address.py
touch ci_cd/Jenkinsfile
touch ci_cd/Dockerfile
touch ci_cd/kubernetes/deployment.yaml
touch ci_cd/kubernetes/service.yaml
touch ci_cd/scripts/build.sh
touch ci_cd/scripts/deploy.sh
touch ci_cd/scripts/test.sh
touch doc/sql/create_database.sql
touch doc/sql/create_tables.sql
touch doc/sql/populate_tables.sql
touch doc/design_document.md
touch doc/other_docs.md
touch .gitignore
touch requirements.txt
touch config.py
touch .env
touch run.py
touch README.md

# Add doc/ to .gitignore
echo "/doc/" >> .gitignore 

echo "Directory structure and empty files created successfully."
## Before executing grant the permission :  $ chmod +x setup_project.sh
## and the execute it :  $ ./setup_project.sh
