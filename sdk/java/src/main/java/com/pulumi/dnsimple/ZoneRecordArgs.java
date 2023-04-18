// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ZoneRecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final ZoneRecordArgs Empty = new ZoneRecordArgs();

    @Import(name="name", required=true)
    private Output<String> name;

    public Output<String> name() {
        return this.name;
    }

    @Import(name="priority")
    private @Nullable Output<String> priority;

    public Optional<Output<String>> priority() {
        return Optional.ofNullable(this.priority);
    }

    @Import(name="ttl")
    private @Nullable Output<String> ttl;

    public Optional<Output<String>> ttl() {
        return Optional.ofNullable(this.ttl);
    }

    @Import(name="type", required=true)
    private Output<String> type;

    public Output<String> type() {
        return this.type;
    }

    @Import(name="value", required=true)
    private Output<String> value;

    public Output<String> value() {
        return this.value;
    }

    @Import(name="zoneName", required=true)
    private Output<String> zoneName;

    public Output<String> zoneName() {
        return this.zoneName;
    }

    private ZoneRecordArgs() {}

    private ZoneRecordArgs(ZoneRecordArgs $) {
        this.name = $.name;
        this.priority = $.priority;
        this.ttl = $.ttl;
        this.type = $.type;
        this.value = $.value;
        this.zoneName = $.zoneName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneRecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneRecordArgs $;

        public Builder() {
            $ = new ZoneRecordArgs();
        }

        public Builder(ZoneRecordArgs defaults) {
            $ = new ZoneRecordArgs(Objects.requireNonNull(defaults));
        }

        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder priority(@Nullable Output<String> priority) {
            $.priority = priority;
            return this;
        }

        public Builder priority(String priority) {
            return priority(Output.of(priority));
        }

        public Builder ttl(@Nullable Output<String> ttl) {
            $.ttl = ttl;
            return this;
        }

        public Builder ttl(String ttl) {
            return ttl(Output.of(ttl));
        }

        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        public Builder type(String type) {
            return type(Output.of(type));
        }

        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        public Builder value(String value) {
            return value(Output.of(value));
        }

        public Builder zoneName(Output<String> zoneName) {
            $.zoneName = zoneName;
            return this;
        }

        public Builder zoneName(String zoneName) {
            return zoneName(Output.of(zoneName));
        }

        public ZoneRecordArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            $.type = Objects.requireNonNull($.type, "expected parameter 'type' to be non-null");
            $.value = Objects.requireNonNull($.value, "expected parameter 'value' to be non-null");
            $.zoneName = Objects.requireNonNull($.zoneName, "expected parameter 'zoneName' to be non-null");
            return $;
        }
    }

}