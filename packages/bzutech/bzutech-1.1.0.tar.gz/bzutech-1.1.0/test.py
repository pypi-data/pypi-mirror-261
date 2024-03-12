from bzutech import BzuTech
import asyncio

bzu = BzuTech("admin@email.com", "bzutech123")
asyncio.run(bzu.start())
asyncio.run(bzu.send_reading('HA-GEN-14', 'HA-81964', float(22.4), '2024-03-08 17:20:09'))