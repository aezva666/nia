from setuptools import setup, find_packages

setup(
    name="nia",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "openai==1.3.0",
        "python-dotenv==1.0.0",
        "pydantic==2.4.2",
        "python-multipart==0.0.6",
        "httpx==0.25.1",
        "python-jose==3.3.0",
        "passlib==1.7.4",
        "bcrypt==4.0.1",
        "sqlalchemy==2.0.23",
        "alembic==1.12.1",
        "psycopg2-binary==2.9.9",
        "redis==5.0.1",
        "requests==2.31.0",
        "aiohttp==3.9.1"
    ],
    python_requires=">=3.10",
) 