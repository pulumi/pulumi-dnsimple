import pulumi
import pulumi_dnsimple as dnsimple

foobar = dnsimple.Record("foobar",
                         domain="stack72.dev",
                         name="test-py",
                         ttl=3600,
                         type="A",
                         value="192.168.0.11")