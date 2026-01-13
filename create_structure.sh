#!/bin/bash
# Project Structure Creator for Mac/Linux
# Save this as: create_structure.sh
# Run: bash create_structure.sh

echo "🚀 Creating Financial Intelligence Platform structure..."
echo ""

# Main directories
mkdir -p docs infrastructure config data airflow dbt_project src dashboards notebooks scripts tests monitoring great_expectations .github

# Airflow structure
mkdir -p airflow/{dags,plugins,logs}
mkdir -p airflow/plugins/{custom_operators,custom_hooks}

# dbt structure
mkdir -p dbt_project/{models,tests,macros,snapshots,seeds}
mkdir -p dbt_project/models/{staging,intermediate,marts,ml_features}
mkdir -p dbt_project/models/marts/{core,finance,analytics}

# Source code structure
mkdir -p src/{ingestion,transformation,ml,analytics,quality,utils,api}
mkdir -p src/ml/{models,training,inference}
mkdir -p src/api/{routes,schemas}

# Dashboard structure
mkdir -p dashboards/{pages,components,assets}

# Data directories
mkdir -p data/{raw,processed,models,exports}
mkdir -p data/raw/cache

# Tests structure
mkdir -p tests/{unit,integration,fixtures}

# Monitoring structure
mkdir -p monitoring/{prometheus,grafana,alerts}
mkdir -p monitoring/grafana/dashboards

# Infrastructure structure
mkdir -p infrastructure/{terraform,ansible}

# Great Expectations structure
mkdir -p great_expectations/{checkpoints,expectations}

# GitHub Actions
mkdir -p .github/workflows

# Create empty __init__.py files for Python packages
touch src/__init__.py
touch src/ingestion/__init__.py
touch src/transformation/__init__.py
touch src/ml/__init__.py
touch src/ml/models/__init__.py
touch src/ml/training/__init__.py
touch src/ml/inference/__init__.py
touch src/analytics/__init__.py
touch src/quality/__init__.py
touch src/utils/__init__.py
touch src/api/__init__.py
touch src/api/routes/__init__.py
touch src/api/schemas/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

# Create placeholder files
echo "# Financial Intelligence Platform" > README.md
echo "# Documentation" > docs/README.md
echo "# Infrastructure as Code" > infrastructure/README.md

echo ""
echo "✅ Project structure created successfully!"
echo ""
echo "📁 Directory structure:"
tree -L 2 -d 2>/dev/null || ls -R

echo ""
echo "🎯 Next steps:"
echo "1. Open this folder in VS Code: code ."
echo "2. Create virtual environment: python3 -m venv venv"
echo "3. Activate it: source venv/bin/activate"
echo ""