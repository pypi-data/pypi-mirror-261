"""The client for Webmin XML-RPC."""

from typing import Any

from aiohttp import ClientSession

from .xmlrpc import XMLRPCClient


class WebminInstance:
    """Represent a Webmin instance."""

    data: dict[str, Any]

    def __init__(self, session: ClientSession):
        """Initialize the WebMin instance."""
        self._client = XMLRPCClient(session)

    async def collect_system_info(self) -> dict[str, Any]:
        """Retrieve system info.

        Includes:
        - cpu: [0, 8, 92, 0, 0] (cpu percent [user, kernel, idle, io, vm])
        - cpufans: [{'fan': 1, 'rpm': 0}, {'rpm': 1393, 'fan': 2}...]
        - cputemps: [{'temp': 48, 'core': 0}, {'core': 1, 'temp': 50}...]
        - disk_free: 90000000000
        - disk_fs: [{'used': 100000000000, 'free': 400000000000, 'iused_percent': 4, 'dir': '/', 'ifree': 100000000000, 'device': 'UUID=', 'itotal': 100000000000, 'type': 'ext4', 'iused': 500000000000, 'total': 200000000000, 'used_percent': 80}...]
        - disk_total: 90000000000
        - disk_used: 90000000000
        - drivetemps: [{'errors': '', 'failed': '', 'device': '/dev/sda', 'temp': 48}...]
        - io: [912, 80]
        - kernel: {'version': '6.6.18-1-lts', 'os': 'Linux', 'arch': 'x86_64'}
        - load: [1.6, 1.35, 1.26, 3589, 'Intel(R) Core(TM) i7-5820K CPU @ 3.30GHz', 'GenuineIntel', 15728640, 12] ([load_1m, load_5m, load_15m, cpu mhz, model name, vendor_id, cache size, cpu count])
        - mem: [32766344, 28516484, 1953088, 1944384, 27872880, ''] ([memtotal, memfree + buffers + cached, swaptotal, swapfree, buffers + cached, memburst])
        - procs: 310
        """
        result: dict[str, Any] = await self._client.call(
            "system-status.collect_system_info"
        )
        return (
            result
            | {
                "load_1m": result["load"][0],
                "load_5m": result["load"][1],
                "load_15m": result["load"][2],
            }
            | {
                "mem_total": result["mem"][0],
                "mem_free": result["mem"][1],
                "swap_total": result["mem"][2],
                "swap_free": result["mem"][3],
            }
        )

    async def get_webmin_version(self) -> dict[str, Any]:
        """Retrieve the Webmin version."""
        return {
            "webmin_version": str(await self._client.call("webmin.get_webmin_version"))
        }

    async def get_cpu_info(self) -> dict[str, Any]:
        """Retrieve the CPU load."""
        result = await self._client.call("proc.get_cpu_info")
        return {"load_1m": result[0], "load_5m": result[1], "load_15m": result[2]}

    async def get_memory_info(self) -> dict[str, Any]:
        """Retrieve memory info."""
        result = await self._client.call("proc.get_memory_info")
        return {
            "mem_total": result[0],
            "mem_free": result[1],
            "swap_total": result[2],
            "swap_free": result[3],
        }

    async def get_network_interfaces(self) -> dict[str, Any]:
        """Retrieve active network interfaces."""
        result = await self._client.call("net.active_interfaces")
        return {"active_interfaces": result}

    async def get_system_uptime(self) -> dict[str, Any]:
        """Retrieve uptime."""
        result = await self._client.call("proc.get_system_uptime")
        return {
            "uptime": {"days": result[0], "minutes": result[1], "seconds": result[2]}
        }

    async def local_disk_space(self) -> dict[str, Any]:
        """Retrieve local disk space."""
        result = await self._client.call("mount.local_disk_space")
        return {
            "total_space": result[0],
            "free_space": result[1],
            "fs": result[2],
            "used_space": result[3],
        }

    async def update(self) -> dict[str, Any]:
        """Retrieve the current data."""
        self.data = (
            (await self.collect_system_info())
            | (await self.get_system_uptime())
            | (await self.get_network_interfaces())
        )
        return self.data
