// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final RecordArgs Empty = new RecordArgs();

    /**
     * The domain to add the record to
     * 
     */
    @Import(name="domain", required=true)
    private Output<String> domain;

    /**
     * @return The domain to add the record to
     * 
     */
    public Output<String> domain() {
        return this.domain;
    }

    /**
     * The name of the record
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The name of the record
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * The priority of the record - only useful for some record types
     * 
     */
    @Import(name="priority")
    private @Nullable Output<String> priority;

    /**
     * @return The priority of the record - only useful for some record types
     * 
     */
    public Optional<Output<String>> priority() {
        return Optional.ofNullable(this.priority);
    }

    /**
     * The TTL of the record
     * 
     */
    @Import(name="ttl")
    private @Nullable Output<String> ttl;

    /**
     * @return The TTL of the record
     * 
     */
    public Optional<Output<String>> ttl() {
        return Optional.ofNullable(this.ttl);
    }

    /**
     * The type of the record
     * 
     */
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return The type of the record
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    /**
     * The value of the record
     * 
     */
    @Import(name="value", required=true)
    private Output<String> value;

    /**
     * @return The value of the record
     * 
     */
    public Output<String> value() {
        return this.value;
    }

    private RecordArgs() {}

    private RecordArgs(RecordArgs $) {
        this.domain = $.domain;
        this.name = $.name;
        this.priority = $.priority;
        this.ttl = $.ttl;
        this.type = $.type;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RecordArgs $;

        public Builder() {
            $ = new RecordArgs();
        }

        public Builder(RecordArgs defaults) {
            $ = new RecordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param domain The domain to add the record to
         * 
         * @return builder
         * 
         */
        public Builder domain(Output<String> domain) {
            $.domain = domain;
            return this;
        }

        /**
         * @param domain The domain to add the record to
         * 
         * @return builder
         * 
         */
        public Builder domain(String domain) {
            return domain(Output.of(domain));
        }

        /**
         * @param name The name of the record
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the record
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param priority The priority of the record - only useful for some record types
         * 
         * @return builder
         * 
         */
        public Builder priority(@Nullable Output<String> priority) {
            $.priority = priority;
            return this;
        }

        /**
         * @param priority The priority of the record - only useful for some record types
         * 
         * @return builder
         * 
         */
        public Builder priority(String priority) {
            return priority(Output.of(priority));
        }

        /**
         * @param ttl The TTL of the record
         * 
         * @return builder
         * 
         */
        public Builder ttl(@Nullable Output<String> ttl) {
            $.ttl = ttl;
            return this;
        }

        /**
         * @param ttl The TTL of the record
         * 
         * @return builder
         * 
         */
        public Builder ttl(String ttl) {
            return ttl(Output.of(ttl));
        }

        /**
         * @param type The type of the record
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The type of the record
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param value The value of the record
         * 
         * @return builder
         * 
         */
        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        /**
         * @param value The value of the record
         * 
         * @return builder
         * 
         */
        public Builder value(String value) {
            return value(Output.of(value));
        }

        public RecordArgs build() {
            $.domain = Objects.requireNonNull($.domain, "expected parameter 'domain' to be non-null");
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            $.type = Objects.requireNonNull($.type, "expected parameter 'type' to be non-null");
            $.value = Objects.requireNonNull($.value, "expected parameter 'value' to be non-null");
            return $;
        }
    }

}
