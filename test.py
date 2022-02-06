import asyncio
from yamsl.meteoswiss import MeteoSwiss

async def main():

    meteo = MeteoSwiss()
    await meteo.setup(8415)

    forecast = await meteo.updateForecast()
    print(forecast)

asyncio.run(main())