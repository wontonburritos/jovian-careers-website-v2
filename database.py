import sqlalchemy
from sqlalchemy import create_engine, text
engine = create_engine("postgresql://postgres.zpzcgloiyendcjgqpwsx:o3UhJk81SGmwCnMl@aws-0-us-west-1.pooler.supabase.com:6543/postgres", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row))
    print(result_dicts)

