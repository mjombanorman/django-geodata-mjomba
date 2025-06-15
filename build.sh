#!/bin/bash
set -e  # Exit on error

echo "Preparing geodata package for distribution..."

# Ensure __init__.py exists in migrations directory
mkdir -p geodata/migrations
touch geodata/migrations/__init__.py

# Check if we need to create migrations
if [ "$1" == "--with-migrations" ]; then
    echo "Setting up temporary Django project for migration generation..."
    TMP_DIR=$(mktemp -d)
    cd $TMP_DIR
    
    # Create a minimal Django project
    django-admin startproject geodata_project .
    
    # Add geodata to INSTALLED_APPS
    sed -i '' "s/INSTALLED_APPS = \[/INSTALLED_APPS = [\n    'geodata',/" geodata_project/settings.py
    
    # Create a symlink to our geodata package
    PACKAGE_DIR=$(cd "$(dirname "$0")" && pwd)
    ln -s $PACKAGE_DIR/geodata .
    
    # Generate migrations
    echo "Generating migrations..."
    python manage.py makemigrations geodata
    
    # Copy migrations back to our package
    echo "Copying migrations to package..."
    cp -r geodata/migrations/* $PACKAGE_DIR/geodata/migrations/
    
    # Clean up
    cd $PACKAGE_DIR
    rm -rf $TMP_DIR
    echo "Migrations created successfully."
fi

# Build the package
echo "Building distribution packages..."
python -m build

echo "Build complete! Distribution files are in the dist/ directory."
echo "To upload to PyPI, run: python -m twine upload dist/*"
