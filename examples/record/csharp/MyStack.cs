using Pulumi;
using Pulumi.DNSimple;

class MyStack : Stack
{
    public MyStack()
    {
        var record = new ZoneRecord("test", new ZoneRecordArgs()
        {
            Ttl = 3600,
            ZoneName = "stack72.dev",
            Name = "test-csharp",
            Type = "A",
            Value = "192.168.0.1",
        });
    }
}
