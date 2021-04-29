using Pulumi;
using Pulumi.DNSimple;

class MyStack : Stack
{
    public MyStack()
    {
        var record = new Record("test", new RecordArgs()
        {
            Ttl = "3600",
            Domain = "stack72.dev",
            Name = "test-csharp",
            Type = "A",
            Value = "192.168.0.1",
        });
    }
}
