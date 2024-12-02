How to Use:


Call ping_sweep() with a subnet (without the last octet) as the argument, like so:

python


ping_sweep("192.168.1")

This will check all IPs from 192.168.1.1 to 192.168.1.254.

Note:

If you run this on a large subnet, it may take a while because you're pinging each host individually.
You might want to consider adding concurrency or multi-threading if performance becomes an issue on larger networks.
