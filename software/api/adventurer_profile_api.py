from . import app
from ..services.adventurer_profile_service import get_adventurer_aos_details

@app.get("/adventurer/aos/details/{adventurer_name}")
async def get_aos_details(adventurer_name):
	return get_adventurer_aos_details(adventurer_name=adventurer_name)