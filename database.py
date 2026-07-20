from motor.motor_asyncio import AsyncIOMotorClient

from config import DATABASE_URL, DATABASE_NAME


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(DATABASE_URL)
        self.db = self.client[DATABASE_NAME]

        self.users = self.db.users
        self.payments = self.db.payments
        self.links = self.db.links

    # ---------------- Users ---------------- #

    async def add_user(self, user_id: int):
        user = await self.users.find_one({"user_id": user_id})

        if not user:
            await self.users.insert_one({
                "user_id": user_id
            })

    async def get_user(self, user_id: int):
        return await self.users.find_one({
            "user_id": user_id
        })

    # ---------------- Payment Links ---------------- #

    async def create_link(self, token: str, amount: int, description: str):
        await self.links.insert_one({
            "token": token,
            "amount": amount,
            "description": description,
            "paid": False,
            "user_id": None,
            "created_at": None,
            "paid_at": None
        })

    async def get_link(self, token: str):
        return await self.links.find_one({
            "token": token
        })

    async def mark_paid(self, token: str, user_id: int):
        await self.links.update_one(
            {"token": token},
            {
                "$set": {
                    "paid": True,
                    "user_id": user_id,
                    "paid_at": __import__("datetime").datetime.utcnow()
                }
            }
        )

    # ---------------- Payments ---------------- #

    async def save_payment(
        self,
        user_id: int,
        amount: int,
        charge_id: str
    ):
        await self.payments.insert_one({
            "user_id": user_id,
            "amount": amount,
            "charge_id": charge_id,
            "timestamp": __import__("datetime").datetime.utcnow()
        })

    async def get_payment(self, charge_id: str):
        return await self.payments.find_one({
            "charge_id": charge_id
        })


db = Database()
