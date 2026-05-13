import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from database import Base
import models # Ensure models are loaded

# The exact URL from your .env
DATABASE_URL = "postgresql+asyncpg://neondb_owner:npg_3rVnUHAp1zsN@ep-polished-frost-aocpoonn.c-2.ap-southeast-1.aws.neon.tech/neondb"

async def main():
    print(f"🚀 Connecting to Neon Cloud (Fixing SSL)...")
    try:
        # Pass ssl=True in connect_args for asyncpg
        engine = create_async_engine(DATABASE_URL, connect_args={"ssl": True})
        async with engine.begin() as conn:
            print("📡 Connection established! Creating tables...")
            await conn.run_sync(Base.metadata.create_all)
            print("✅ SUCCESS: Tables created in Neon!")
        await engine.dispose()
    except Exception as e:
        print(f"❌ ERROR: Could not create tables.")
        print(f"Details: {e}")

if __name__ == "__main__":
    asyncio.run(main())
