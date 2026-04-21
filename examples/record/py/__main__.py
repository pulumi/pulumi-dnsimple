import pulumi
import pulumi_dnsimple as dnsimple

record = dnsimple.ZoneRecord(
    "record",
    zone_name="dnsimple.test.pulumi.com",
    name="test-py",
    ttl=3600,
    type="A",
    value="192.168.0.11",
)

pulumi.export("record_urn", record.urn)
