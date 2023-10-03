// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.DNSimple
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("dnsimple");

        private static readonly __Value<string?> _account = new __Value<string?>(() => __config.Get("account"));
        /// <summary>
        /// The account for API operations.
        /// </summary>
        public static string? Account
        {
            get => _account.Get();
            set => _account.Set(value);
        }

        private static readonly __Value<bool?> _prefetch = new __Value<bool?>(() => __config.GetBoolean("prefetch"));
        /// <summary>
        /// Flag to enable the prefetch of zone records.
        /// </summary>
        public static bool? Prefetch
        {
            get => _prefetch.Get();
            set => _prefetch.Set(value);
        }

        private static readonly __Value<bool?> _sandbox = new __Value<bool?>(() => __config.GetBoolean("sandbox"));
        /// <summary>
        /// Flag to enable the sandbox API.
        /// </summary>
        public static bool? Sandbox
        {
            get => _sandbox.Get();
            set => _sandbox.Set(value);
        }

        private static readonly __Value<string?> _token = new __Value<string?>(() => __config.Get("token"));
        /// <summary>
        /// The API v2 token for API operations.
        /// </summary>
        public static string? Token
        {
            get => _token.Get();
            set => _token.Set(value);
        }

        private static readonly __Value<string?> _userAgent = new __Value<string?>(() => __config.Get("userAgent"));
        /// <summary>
        /// Custom string to append to the user agent used for sending HTTP requests to the API.
        /// </summary>
        public static string? UserAgent
        {
            get => _userAgent.Get();
            set => _userAgent.Set(value);
        }

    }
}
