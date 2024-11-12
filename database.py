from sqlalchemy import create_engine, text
db_connection_string = "postgresql://postgres.zpzcgloiyendcjgqpwsx:o3UhJk81SGmwCnMl@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs