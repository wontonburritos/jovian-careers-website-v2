from sqlalchemy import create_engine, text
db_connection_string = "postgresql://postgres.zpzcgloiyendcjgqpwsx:o3UhJk81SGmwCnMl@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
engine = create_engine(db_connection_string)
